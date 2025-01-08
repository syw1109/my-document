from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 * 세로

listbox = Listbox(root, selectmode="extended", height=0)  #extended 다중 선택, single 한개만 선택, height 숫자만큼 글자 보임, 0이면 모두 보임
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나") # 리스트 넘버 적어주기 귀찮으면 END로 넣으면 맨 마지막에 삽입된다
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    # 삭제
    # listbox.delete(0) # 클릭시 맨 앞(0) 항목을 삭제, END 맨 끝

    # 갯수 확인
    # print("리스트에는", listbox.size(), "개가 있어요") # 리스트에는 5 개가 있어요

    # 항목 확인 (시작 idx, 끝 idx)
    # print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2))  # 시작인덱스 0 번쨰줄  ~ 끝 인덱스 2 번째줄

    # 선택된 항목의 인덱스 확인 (위치로 반환 (ex) (1, 2, 3) ) 
    print("선택된 항목 : ", listbox.curselection())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()