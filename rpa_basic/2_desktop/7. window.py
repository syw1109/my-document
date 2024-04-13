import pyautogui   #맥북은 사용불가

# fw = pyautogui.getActiveWindow() # 현재 활성화된 창 (VSCode)  fw: foreground window : 활성화되어 있는 윈도우 창( ex. 계산기,)
# print(fw.title) # 창의 제목 정보
# print(fw.size) # 창의 크기 정보 (width, height)
# print(fw.left, fw.top, fw.right, fw.bottom) # 창의 좌표 정보
# pyautogui.click(fw.left + 25, fw.top + 20) # left에 25더하고, 탑에서 20더한 위치를 클릭

# for w in pyautogui.getAllWindows():
#     print(w) # 모든 윈도우 가져오기

# for w in pyautogui.getWindowsWithTitle("제목 없음"):  #for 반복문으로 사용
#     print(w)

w = pyautogui.getWindowsWithTitle("제목 없음")[0] # 리스트로 넘어온 것의 첫번쨰 값을 사용 [0]
print(w)
if w.isActive == False: # 현재 활성화가 되지 않았다면
    w.activate() # 활성화 (맨 앞으로 가져오기)

if w.isMaximized == False: # 현재 최대화가 되지 않았다면
    w.maximize() # 최대화

pyautogui.sleep(1)

if w.isMinimized == False : # 현재 최소화가 되지 않았다면
    w.minimize() # 최소화

w.restore() # 화면 원복

w.close() # 윈도우 닫기