from tkinter import *  #티킨터는 따로 설치할 것은 없다

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 * 세로
#root.geometry("640x480+300+100") # 가로 * 세로 + x좌표 + y좌표

root.resizable(True, False) # x(너비), y(높이) 값 변경 불가(false) (창 크기 변경 불가)

root.mainloop() #창이 닫히지 않도록 한다