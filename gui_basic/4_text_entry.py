# text pack : 글자 입력 텍스트 위젯

from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 * 세로

txt = Text(root, width=30, height=5)  # 테스트 위젯이 생김  여러줄 가능 엔터키 가능
txt.pack() 
txt.insert(END, "글자를 입력하세요") # 글자 입력해줌. 

e = Entry(root, width=30) # 한줄만 입력 가능 엔터키 불가
e.pack()
e.insert(0, "한 줄만 입력해요") # 엔트리에도 글자 삽입

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END)) # 1 : 첫번째 라인, 첫번쨰 라인부터 가져와라.  0 : 0번째 column 위치, 0번쨰 칼럼부터 가져와라
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)  # 내용 삭제, 1라인부터, 0번쨰 컬럼부터
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()