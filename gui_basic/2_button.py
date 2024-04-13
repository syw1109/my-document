from tkinter import *

root = Tk()
root.title("Nado GUI")

btn1 = Button(root, text="버튼1") #root 에 넣고, text 버튼1 
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼22222")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4444ㅇㅇㅇ4") # 버튼 크기 고정
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5") # fg : 글자색, bg :배경
btn5.pack()

photo = PhotoImage(file="img22.png") #경로
btn6 = Button(root, image=photo) # 이미지 속성을 포토로
btn6.pack() 

def btncmd():  # btncmd 함수 설정
    print("버튼이 클릭되었어요")

btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()