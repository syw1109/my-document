import os
import time
import pandas as pd
import xlwings as xw
import pyautogui

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1번: 셀레니움을 이용한 엑셀 다운로드 함수
def selenium_download():
    print("[1] selenium_download 시작")
    service = Service(executable_path=r"C:\chromedriver-win64\chromedriver.exe")

    options = webdriver.ChromeOptions()

    # 보안인증서 오류 무시 옵션
    options.add_experimental_option("prefs", {
        "acceptInsecureCerts": True,
        "acceptSslCerts": True,
    })

    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("http://WP 주소")
        time.sleep(6)

        login = {"id": "yw0.seo", "pw": "tjdud1516!"}
        driver.find_element(By.XPATH, '//*[@id="userNameInput"]').send_keys(login.get('id'))
        driver.find_element(By.XPATH, '//*[@id="passwordInput"]').send_keys(login.get('pw'))
        driver.find_element(By.XPATH, '//*[@id="submitButton"]').click()
        time.sleep(12)

        # 불발통 300mm 다운로드
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get("http://불발통300mm주소")

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/form/div/div/div[1]/div[1]/div/div/button[2]'))
        )
        element.click()
        time.sleep(1)
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/form/div/div/div[1]/div[1]/div/div/button[3]'))
        )
        element.click()
        time.sleep(4)

        # 이미지 클릭 처리 (다운로드 파일 안전경고 처리)
        image_path2 = r'C:\Users\yw0.seo\Desktop\vscode-test\programing\1.Project\2.rff adder report\continue.png'
        region = (713, 97, 822, 139)

        try:
            image_location2 = pyautogui.locateOnScreen(image_path2, region=region, confidence=0.9)
            if image_location2:
                pyautogui.click(pyautogui.center(image_location2))
                time.sleep(2)
        except Exception as e:
            print(f"[1] 불발통300mm 다운로드 경고 처리 오류: {e}")

        # 불발통 M 다운로드
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[2])
        driver.get("http://불발통M 주소")

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/form/div/div/div[1]/div[1]/div/div/button[2]'))
        )
        element.click()
        time.sleep(1)
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/form/div/div/div[1]/div[1]/div/div/button[3]'))
        )
        element.click()
        time.sleep(4)

        image_path2_2 = r'C:\Users\yw0.seo\Desktop\vscode-test\programing\1.Project\2.rff adder report\continue.png'
        region2 = (526, 47, 931, 276)

        try:
            image_location2 = pyautogui.locateOnScreen(image_path2_2, region=region2, confidence=0.9)
            if image_location2:
                pyautogui.click(pyautogui.center(image_location2))
                time.sleep(2)
        except Exception as e:
            print(f"[1] 불발통M 다운로드 경고 처리 오류: {e}")

    except Exception as e:
        print(f"[1] selenium_download 오류: {e}")

    finally:
        driver.quit()
        time.sleep(2)
        print("[1] selenium_download 완료")


# 2번: 엑셀 전처리 함수, 반환값은 전처리된 DataFrame
def preprocess_data():
    print("[2] preprocess_data 시작")

    DOWNLOAD_FOLDER = r"C:\Users\yw0.seo\Downloads"
    FILE_INFOS = [
        {"prefix": "(_)_yw0.seo", "old_filename": "Foundry_old.xlsx",
         "col_key1": 2, "col_key2": 13, "col_cond": 19, "col_atc": 6},
        {"prefix": "(_0)_yw0.seo", "old_filename": "Memory_old.xlsx",
         "col_key1": 1, "col_key2": 9, "col_cond": 15, "col_atc": 5}
    ]
    FILE_EXTENSION = '.xlsx'
    ROW_OFFSET = 5

    def find_latest_excel_file(folder: str, prefix: str, extension: str) -> str:
        files = [
            os.path.join(folder, f)
            for f in os.listdir(folder)
            if f.endswith(extension) and prefix in f
        ]
        if files:
            return max(files, key=os.path.getctime)
        return None

    def load_old_data(file_path: str, col_key1: int, col_key2: int) -> set:
        try:
            with xw.App(visible=False) as app:
                wb = xw.Book(file_path)
                sheet = wb.sheets[0]
                start_cell = f'A{ROW_OFFSET + 1}'
                end_cell = f'Z{sheet.used_range.last_cell.row}'
                rng = sheet.range(f'{start_cell}:{end_cell}')
                df = rng.options(pd.DataFrame, index=False, header=1).value
                old_set = set(zip(df.iloc[:, col_key1], df.iloc[:, col_key2]))
                wb.close()
                return old_set
        except Exception as e:
            print(f"[2] {file_path} 읽기 오류: {e}")
            return set()

    def extract_key1_atc_pairs(file_path: str, old_set: set, col_key1: int, col_key2: int,
                               col_cond: int, col_atc: int, prefix: str):
        try:
            with xw.App(visible=False) as app:
                wb = xw.Book(file_path)
                sheet = wb.sheets[0]
                start_cell = f'A{ROW_OFFSET + 1}'
                end_cell = f'Z{sheet.used_range.last_cell.row}'
                rng = sheet.range(f'{start_cell}:{end_cell}')
                df = rng.options(pd.DataFrame, index=False, header=1).value
                pair_list = []
                for _, row in df.iterrows():
                    key_tuple = (row.iloc[col_key1], row.iloc[col_key2])
                    cond_str = str(row.iloc[col_cond])
                    if (('#' in cond_str) or ('rff' in cond_str.lower())) and key_tuple not in old_set:
                        pair = {
                            'prefix': prefix,
                            'col_key1': row.iloc[col_key1],
                            'col_atc': row.iloc[col_atc]
                        }
                        pair_list.append(pair)
                wb.close()
                return pair_list
        except Exception as e:
            print(f"[2] 오류가 발생했습니다: {e}")
            return []

    all_pairs = []
    for file_info in FILE_INFOS:
        latest_file = find_latest_excel_file(DOWNLOAD_FOLDER, file_info["prefix"], FILE_EXTENSION)
        old_path = os.path.join(DOWNLOAD_FOLDER, file_info["old_filename"])

        old_set = set()
        if os.path.exists(old_path):
            old_set = load_old_data(old_path, file_info["col_key1"], file_info["col_key2"])

        if latest_file:
            pair_list = extract_key1_atc_pairs(
                latest_file,
                old_set,
                file_info["col_key1"],
                file_info["col_key2"],
                file_info["col_cond"],
                file_info["col_atc"],
                file_info["prefix"]
            )
            all_pairs.extend(pair_list)
        else:
            print(f"[2] '{file_info['prefix']}'에 해당하는 파일이 없습니다.")

    if all_pairs:
        df = pd.DataFrame(all_pairs)
        save_path = os.path.join(DOWNLOAD_FOLDER, "all_key1_atc_pairs.xlsx")
        df.to_excel(save_path, index=False)
        print(f"[2] 모든 짝 값들이 {save_path}에 저장되었습니다.")
        print("[2] preprocess_data 완료")
        return df
    else:
        print("[2] 저장할 짝 값이 없습니다.")
        return pd.DataFrame()


# 3번: 이미지 기반 마우스 클릭, 키보드 입력, 인자로 DataFrame 받음
def image_based_interaction(df):
    print("[3] image_based_interaction 시작")

    if df.empty:
        print("[3] 전처리된 데이터가 없습니다. 종료합니다.")
        return

    # 이미지 및 region 경로 설정
    image_path1 = r'C:\Users\yw0.seo\Desktop\vscode-test\programing\1.Project\2.rff adder report\MaskID.png'
    image_path2 = r'C:\Users\yw0.seo\Desktop\vscode-test\programing\1.Project\2.rff adder report\view.png'
    image_path3 = r'C:\Users\yw0.seo\Desktop\vscode-test\programing\1.Project\2.rff adder report\check.png'
    image_path4 = r'C:\Users\yw0.seo\Desktop\vscode-test\programing\1.Project\2.rff adder report\search.png'
    image_path5 = r'C:\Users\yw0.seo\Desktop\vscode-test\programing\1.Project\2.rff adder report\blue.png'
    image_path6 = r'C:\Users\yw0.seo\Desktop\vscode-test\programing\1.Project\2.rff adder report\sem_trans.png'
    image_path7 = r'C:\Users\yw0.seo\Desktop\vscode-test\programing\1.Project\2.rff adder report\ATC_SEM.png'
    image_path8 = r'C:\Users\yw0.seo\Desktop\vscode-test\programing\1.Project\2.rff adder report\insp_time.png'
    image_path9 = r'C:\Users\yw0.seo\Desktop\vscode-test\programing\1.Project\2.rff adder report\left.png'
    image_path10 = r'C:\Users\yw0.seo\Desktop\vscode-test\programing\1.Project\2.rff adder report\SEM.png'
    image_path11 = r'C:\Users\yw0.seo\Desktop\vscode-test\programing\1.Project\2.rff adder report\DateInitial.png'

    region = (160, 180, 1117, 570)

    col2 = df.columns[0]
    col3 = df.columns[1]

    for idx, row in df.iterrows():
        reticle_id = str(row[col2])
        sem_value = str(row[col3])
        SEM = 'ATC_SEM' if 'ATC' in sem_value else 'SEM'

        print(f"[3] {idx+1} / reticle_id: {reticle_id}, SEM: {SEM}")

        try:
            # 날짜 초기화 클릭
            image_location11 = pyautogui.locateOnScreen(image_path11, region=region, confidence=0.9)
            if image_location11:
                pyautogui.click(pyautogui.center(image_location11))
                time.sleep(0.5)
            else:
                print("[3] DateInitial 이미지 못 찾음")

            # 검사시간 화살표 클릭
            image_location8 = pyautogui.locateOnScreen(image_path8, region=region, confidence=0.9)
            if image_location8:
                pos = pyautogui.center(image_location8)
                pyautogui.click(pos[0] + 159, pos[1])
                time.sleep(0.5)

            # 달력 이전달로 이동 클릭
            image_location9 = pyautogui.locateOnScreen(image_path9, region=region, confidence=0.9)
            if image_location9:
                pyautogui.click(pyautogui.center(image_location9))
                time.sleep(0.5)

            # 화살표 아래 클릭 - 한달 이전 날짜 이동
            image_location8 = pyautogui.locateOnScreen(image_path8, region=region, confidence=0.9)
            if image_location8:
                pos = pyautogui.center(image_location8)
                pyautogui.click(pos[0] + 159, pos[1]+109)
                time.sleep(0.5)

            # MaskID 입력 영역 클릭 및 입력
            image_location = pyautogui.locateOnScreen(image_path1, region=region, confidence=0.9)
            if image_location:
                pyautogui.click(pyautogui.center(image_location).x, pyautogui.center(image_location).y + 20)
                time.sleep(0.5)

                pyautogui.hotkey('ctrl', 'a')
                pyautogui.press('backspace')
                time.sleep(0.2)

                pyautogui.typewrite(reticle_id)
            else:
                print("[3] MaskID 이미지 못 찾음")

            # 돋보기(view) 클릭
            image_location2 = pyautogui.locateOnScreen(image_path2, confidence=0.9)
            if image_location2:
                pyautogui.click(pyautogui.center(image_location2))
                time.sleep(0.5)

            # 체크박스 클릭
            image_location3 = pyautogui.locateOnScreen(image_path3, confidence=0.9)
            if image_location3:
                pyautogui.click(pyautogui.center(image_location3))
                time.sleep(0.5)

            # search 클릭
            image_location4 = pyautogui.locateOnScreen(image_path4, confidence=0.9)
            if image_location4:
                pyautogui.click(pyautogui.center(image_location4))
                time.sleep(1.5)

            # 파란색 행 우클릭
            image_location5 = pyautogui.locateOnScreen(image_path5, confidence=0.9)
            if image_location5:
                pyautogui.click(pyautogui.center(image_location5), button='right')
                time.sleep(0.5)

            # SEM 전송 클릭
            image_location6 = pyautogui.locateOnScreen(image_path6, confidence=0.9)
            if image_location6:
                pyautogui.moveTo(pyautogui.center(image_location6))
                time.sleep(1)

            # SEM/ATC_SEM 클릭
            if SEM == 'SEM':
                image_location_click_sem = pyautogui.locateOnScreen(image_path10, confidence=0.9)
            else:
                image_location_click_sem = pyautogui.locateOnScreen(image_path7, confidence=0.9)

            if image_location_click_sem:
                pyautogui.click(pyautogui.center(image_location_click_sem))
                time.sleep(0.5)
            else:
                print(f"[3] {SEM} 이미지 못 찾음")

            # enter 전화 연타 4회
            for _ in range(4):
                pyautogui.press('enter')
                time.sleep(0.2)

        except Exception as e:
            print(f"[3] 오류 발생: {e}")

    print("[3] image_based_interaction 완료")


# 전체 1~3번 반복 main_loop (5분 간격)
def main_loop():
    while True:
        print("="*20)
        print("작업 시작:", time.strftime("%Y-%m-%d %H:%M:%S"))

        selenium_download()    # 1번 다운로드
        df_processed = preprocess_data()  # 2번 전처리
        image_based_interaction(df_processed)   # 3번 화면 조작

        print("작업 완료. 5분 대기")
        print("="*20)
        time.sleep(300)  # 300초 = 5분


if __name__ == "__main__":
    main_loop()
