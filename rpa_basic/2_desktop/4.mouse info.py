import pyautogui
#pyautogui.FAILSAFE = False  # 네 귀퉁이로 마우스를 넣어도 끝나지 않음. 추천하지는 않음
pyautogui.PAUSE = 1 # 모든 동작에 1초씩 sleep 적용
# pyautogui.mouseInfo()  # F1누르면 현재 마우스 위치와 색깔 정보를 얻을수 있다. 복붙 1729,61 45,45,45 #2D2D2D

for i in range(5):   # 중간에 실패 할떄 마우스를 네 귀퉁이로 보내면 프로그램이 멈춘다.
    pyautogui.move(100, 100)
    pyautogui.sleep(1) # 해당 동작에 1초씩 쉬는 시간을 준다. 위에 줄에 PAUSE를 하면 전체 동작에 1초씩 쉬는시간을 준다