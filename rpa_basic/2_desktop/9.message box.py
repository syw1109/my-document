import pyautogui
# print("곧 시작합니다...")
# pyautogui.countdown(3) #3초동안 카운트 다운해줌
# print("자동화 시작")

# pyautogui.alert("자동화 수행에 실패하였습니다.", "경고") # 확인 버튼만 있는 팝업  ("문구", "타이틀")
# pyautogui.confirm("계속 진행하시겠습니까?", "확인") # 확인 취소 메세지 박스 띄워줌
# result = pyautogui.confirm("계속 진행하시겠습니까?", "확인") # 확인, 취소 버튼
# print(result) # 확인시 OK, 취소시 Cancel, OK면 어떻게 진행 분기문 가능

# result = pyautogui.prompt("파일명을 무엇으로 하시겠습니까?", "입력") # 사용자 입력
# print(result)
result = pyautogui.password("암호를 입력하세요") # 암호 입력  ****로 표시가 된다
print(result)