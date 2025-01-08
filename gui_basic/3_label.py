# label 글자나 이미지를 보여준다  text

from tkinter import * 

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 창 크기

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="gui_basic/img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요") # config : text를 또 만나요로 바꾼다

    global photo2  # 이게 없으면 함수가 끝나면 이미지가 사라짐. 전역변수로 만들어줘야 안사라짐. 
    photo2 = PhotoImage(file="gui_basic/img2.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=change) 
btn.pack()

root.mainloop()