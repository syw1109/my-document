import pyautogui  # 이미지 파일을 저장해서 전체 윈도우 화면중에 해당 이미지를 찾는다
# file_menu = pyautogui.locateOnScreen("file_menu.png")  # file_menu.png 파일을 만든다. 이미지는 PNG로, 화면에서 파일에 있는 이미지 찾아서 반환
# print(file_menu)  # 윈도우 화면상에서 해당 이미지를 찾아서 좌표로 표시하고 가로,세로 길이도 표시. 좌표 left, top
# pyautogui.click(file_menu) #해당 이미지를 클릭

# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon) #트래쉬 아이콘으로 이동한다 마우스, 내 PC에서는 쓰레기통이 사라져서 못찾음 

# screen = pyautogui.locateOnScreen("screenshot.png") # 화면중에 해당 이미지 못찾으면 안뜬다고 뜸 None 혹은 pyautogui.ImageNotFoundException 
# print(screen)


#---------------------------------------------------------------------------------
# 체크 박스 클릭 예제
# 화면 해상도가 바뀌어도 이미지 인식 못할 수 있다. 똑같은 이미지가 2개 이상이라면?  
# **구글 - w3schools checkbox 검색
# 주소 : https://www.w3schools.com/tags/att_input_type_checkbox.asp
# → try it yourself 클릭

#----------------------------------------------------------------------------------




# for i in pyautogui.locateAllOnScreen("checkbox.png"):  # locateAllOnScreen 윈도우 화면 내에서 지정한 모든 이미지를 불러온다. 다중 그림 
#     print(i)
#     pyautogui.click(i, duration=0.25)   # 3개의 동일한 이미지의 체크 박스를 클릭
 
# checkbox = pyautogui.locateOnScreen("checkbox.png") # 그냥 locateOnScreen 기능을 썼을때는 최초 한개만 클릭한다
# pyautogui.click(checkbox)

# trash_icon = pyautogui.locateOnScreen("trash_icon.png")  # 아이콘을 찾는데 시간이 많이 걸릴 수도 있다. 화면이 커서. 영역을 줄여줄 필요가 있다
# pyautogui.moveTo(trash_icon)

# ----->

# 속도 개선
# 1. GrayScale   # 컬러 이미지를 흑백으로 전환 한다
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True) # grayscale=True 흑백 전환, 정확도가 조금 떨어짐
# pyautogui.moveTo(trash_icon)

# 2. 범위 지정 (범위를 좁혀줌)
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(1488, 623, 1881 - 1488, 137)) # region=(x, y, width, height), mouseInfo 기능을 활용해서 좌표 알아낼수 있다.
# pyautogui.moveTo(trash_icon)    # 사칙연산도 가능 1881-1488 =  마이너스연산


# 3. 정확도 조정/ 
# run_btn = pyautogui.locateOnScreen("run_btn.png", confidence=0.9) # confidence 사용 위해 pip install opencv-python 설치, 이미지 정확도 90% 
# pyautogui.moveTo(run_btn)




#-----------------------
# 오 류 문구 1  발 생
# Traceback (most recent call last):
#   File "c:/cripto/rpa_basic/2_desktop/6.image recognition.py", line 84, in <module>
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#   File "C:\python38-32\lib\site-packages\pyautogui\__init__.py", line 174, in wrapper
#     raise ImageNotFoundException  # Raise PyAutoGUI's ImageNotFoundException.
# pyautogui.ImageNotFoundException

# PyScreeze를 0.1.19에서 0.1.18로 다운그레이드하기만 하면 다시 잘 작동합니다.
# pip install --upgrade [package]==[version]
# 이렇게 작성하면 원하는 모듈을 다운그레이드 할 수 있다. 나는 statsmodels의 버전을 0.13.2에서 0.11.1로 바꾸고 싶어서 이렇게 작성했다.
# pip install --upgrade statsmodels==0.11.1
# pip install --upgrade pyscreeze==0.1.18   

# pip install --upgrade pyscreeze==0.1.27 로 다운그레이드
# 해결이 안되어 pyscreeze와 pyautogui를 제거후 다시 설치
# pip uninstall pyscreeze pyautogui   y누르고 삭제
# pip install pyautogui==0.9.35

# 오류 문구2
# AttributeError: module 'pyautogui' has no attribute 'locateOnScreen'
#방법 1. (정상 동작 확인)

# pyautogui 라이브러리의 __init__.py 파일의 
# 221번째 줄을
# locateOnWindow.__doc__ = pyscreeze.locateOnWindow.__doc__
# 에서 
# locateOnWindow.__doc__ = pyscreeze.locateOnScreen.__doc__
# 위와 같이 수정 
# 라이브러리를 가는 방법을 모음;;

# 파이썬 3.9.** 버전에서는 괜찮다고 해서 버전 업그레이드 해봄  py -m pip install --upgrade pip  -> 안됨 ;

# ******* 최종적으로  pip install --upgrade pyscreeze==0.1.27 로 다운그레이드했더니 문제가 해결 되었다*****


# 자동화 대상이 바로 보여지지 않는 경우
# 1. 계속 기다리기
file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# if file_menu_notepad: #메모장 파일 메뉴가 있으면~ 
#     pyautogui.click(file_menu_notepad)
# else:
#     print("발견 실패")

# while file_menu_notepad is None:  # 와일문으로 발견이 안되도 반복문 작업을 계속 한다
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     print("발견 실패")
# pyautogui.click(file_menu_notepad)

# 2. 일정 시간동안 기다리기 (TimeOut) # 5초안에 안나오면 프로그램 종료
import time
import sys

# timeout = 10 # 10초 대기
# start = time.time() # 시작 시간 설정
# file_menu_notepad = None   # 메모장 메뉴창이 none 없는 경우
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     end = time.time() # 종료 시간 설정
#     if end - start > timeout: # 지정한 10초를 초과하면
#         print("시간 종료")
#         sys.exit() # 프로그램 종료

# pyautogui.click(file_menu_notepad)    

#---------> 위와 같이 하면 코딩 쓰기가 힘들어서 아래와 같이 함수로 쓴다.

#오류 문구 발생 
# NameError: name 'time' is not defined -> time 모듈이 없어서 그런것
# NameError: name 'sys' is not defined -> sys 모듈이 없어서 그런것
# import time 을 주석처리해서 그런것. 
# import sys 을 주석처리 해제


def find_target(img_file, timeout=30): # find 타겟 함수
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break # while문 탈출
    return target

def my_click(img_file, timeout=30):    # 클릭함수 30초
    target = find_target(img_file, timeout)  # target 함수, find_target 변수에 이미지파일과 타임아웃 정보 기입
    if target:
        pyautogui.click(target) #타겟이 있으면 클릭
    else:
        print(f"[Timeout {timeout}s] Target not found ({img_file}). Terminate program.") # f스트링 { } 안에 변수를 넣는 문구
        sys.exit() #프로그램 종료

# #pyautogui.click(file_menu_notepad)

my_click("file_menu_notepad.png", 10)  # 함수의 img file에 file_menu_notepad.png 가 들어감