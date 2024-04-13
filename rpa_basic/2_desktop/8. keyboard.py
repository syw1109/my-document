import pyautogui
w = pyautogui.getWindowsWithTitle("제목 없음")[0] # 메모장 1개 띄운 상태에서 가져옴
w.activate()

# pyautogui.write("12345",interval=0.25) # 메모장 띄우고 따로 마우스 클릭없어도 커서 깜빡여서 바로 12345 입력 가능
# pyautogui.write("NadoCoding", interval=0.25)
# pyautogui.write("나도코딩") #한글은 안먹힘, 영어, 숫자

# pyautogui.write(["t","e","s","t","left","left","right","l","a","enter","right","backspace"], interval=0.25)
# t e s t 순서대로 적고 왼쪽 방향키 2번, 오른쪽 방향키 2번, l a 순서대로 적고 enter 입력 후 오른쪽 키 backspace

# ---------------------------------------------
### 사이트 주소 : automate the boring stuff with python 
# -> Table of contents -> 20. Controlling the keyboard and mouse with GUI Automation 클릭
# Ctrl + F -> keyboard attribute 검색 -> table 20-1 : 키의 의미 기능 정의 정리
#-------------------------------------------------

# 특수 문자
# shift 4 -> $
# pyautogui.keyDown("shift") # shift 키를 누른 상태에서
# pyautogui.press("4") # 숫자 4를 입력하고
# pyautogui.keyUp("shift") # shift 키를 뗀다

# 조합키 (Hot Key)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a") # 컨트롤+ a 동시에 누르고
# pyautogui.keyUp("a") # press("a")
# pyautogui.keyUp("ctrl") # Ctrl + A

# 간편한 조합키 매번 4단계로 치기 귀찮으니
# pyautogui.hotkey("ctrl", "alt", "shift", "a") 
# Ctrl 누르고 > Alt 누르고 > Shift 누르고 > A 누르고 > A 떼고 > Shift 떼고 > Alt 떼고 > Ctrl 떼고
# pyautogui.hotkey("ctrl", "a")


#---------------------
# 한글 입력 가능하게 하기
# 터미널 보드에 pip install pyperclip

import pyperclip  # 특정 문장을 클립보드에 집어 넣음
# pyperclip.copy("나도코딩") # "나도코딩" 글자를 클립보드에 저장
# pyautogui.hotkey("ctrl", "v") # 클립보드에 있는 내용을 붙여넣기

#함수로 쓰기
def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

my_write("나도코딩")

# 자동화 프로그램 종료
# win : ctrl + alt + del
# mac : cmd + shift + option + q