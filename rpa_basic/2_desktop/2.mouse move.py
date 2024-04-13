import pyautogui

# "절대 좌표"로 마우스 이동
#pyautogui.moveTo(200, 100) # 지정한 위치(가로 x, 세로 y)로 마우스를 이동
#pyautogui.moveTo(100, 200, duration=5) # 5초 동안 100, 200 위치로 이동, 마우스 움직이는 모습 볼수 있음5초동안 이동

#pyautogui.moveTo(100, 100, duration=0.25)
#pyautogui.moveTo(200, 200, duration=0.25)
#pyautogui.moveTo(300, 300, duration=0.25)

# "상대 좌표"로 마우스 이동 (현재 커서가 있는 위치로부터)
pyautogui.moveTo(100, 100, duration=0.25)
print(pyautogui.position()) # Point(x, y)
pyautogui.move(100, 100, duration=0.25) # 100, 100 기준으로 +100, +100 -> 200, 200
print(pyautogui.position()) # Point(x, y)
pyautogui.move(100, 100, duration=0.25) # 200, 200 기준으로 -> 300, 300
print(pyautogui.position()) # Point(x, y)

p = pyautogui.position()
print(p[0], p[1]) # x, y  위아래 좌표 똑같이 나온다
print(p.x, p.y) # x, y