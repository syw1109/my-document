import pyautogui

#PS C:\cripto> pip install pyautogui 터미널 창에 pip 다운로드 시작
# 1) 에러가 떠서 앞에 python.exe -m pip install pyautogui 이렇게 붙여줌
# 2) 그래도 안돼서 관리자 모드로 VS코드를 여니깐, pip install pyautogui 치니깐 -> 업그레이드 하라는 문구가 떠서 업그레이드함
# c:\python38-32\python.exe -m pip install --upgrade pip   ---> 2)는 안해도 되는거 같음
# 3) 우하단에 3.8.6 64-bit 클릭해서 32비트 로 클릭하니 실행된다
size = pyautogui.size() #현재 화면의 스크린 사이즈
print(size)# 가로세로 크기 알수 있음
size[0] : width,  
size[1] : height  