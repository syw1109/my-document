import pyautogui
# 스크린 샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png") # 스크린샷 해서 파일로 저장

# pyautogui.mouseInfo()
# 28,18 34,167,242 #22A7F2 #강사 화면 기준
# 22,17 80,127,180 #507FB4 #내 화면 기준

pixel = pyautogui.pixel(22, 17) #주어진 좌표의 한개의 픽셀가져옴
print(pixel) #해당 픽셀에 있는RGB값을 찍어주는것  22,17 → 80,127,180

print(pyautogui.pixelMatchesColor(22, 18, (34,167,242)))  # pyautogui.pixelMatchesColor 매칭을 시켜서 색깔이 맞으면 True, else false
#print(pyautogui.pixelMatchesColor(28, 18, pixel))
# print(pyautogui.pixelMatchesColor(28, 18, (34,167,243)))