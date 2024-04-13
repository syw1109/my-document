import pyautogui
pyautogui.sleep(3) # 움직일 수 있는 시간3초 대기 
# print(pyautogui.position())  file 좌표 68  26

#pyautogui.click(68, 26, duration=1) # 1초 동안 (68, 16) 좌표로 이동 후 마우스 클릭
# pyautogui.click()
# pyautogui.mouseDown()
# pyautogui.mouseUp()

#pyautogui.doubleClick()  # 더블클릭
#pyautogui.click(clicks=500)  #clicks =2 더블클릭, 500이면 마구 클릭 

# pyautogui.move(200, 200)
# pyautogui.mouseDown() # 마우스 버튼 누른 상태
# pyautogui.move(300, 300)
# pyautogui.mouseUp() # 마우스 버튼 뗀 상태

#pyautogui.sleep(3) # 3초 대기
#pyautogui.rightClick()
#pyautogui.middleClick()

# print(pyautogui.position()) #드래그할 특정위치 좌표 구함 1366 184
# pyautogui.moveTo(1336, 184) 
# pyautogui.drag(100, 0) # 현재 위치 기준으로 x 100 만큼, y 0 만큼 드래그
# pyautogui.drag(100, 0, duration=0.25) # 너무 빠른 동작으로 drag 수행이 안될때는 duration 값 설정
# pyautogui.dragTo(1514, 349, duration=0.25) # 절대 좌표 기준으로 x 1514, y 349 로 드래그

pyautogui.scroll(300) # 300  양수이면 위 방향으로, -300 음수이면 아래 방향으로 300만큼 스크롤.