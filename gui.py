from tkinter import *
from PIL import ImageTk,Image
from tkhtmlview import HTMLLabel
#main window object
root = Tk()
root.minsize(400,400)
root.title("Cryptarithmetic Problem Solver")
#menu bar
def abtCmd():
    about = Toplevel()
    label = HTMLLabel(about,html="\
                      <h1>About The problem</h1>\
                      <p>In the crypt-arithmetic problem, some letters are used to assign digits to it. Like ten different letters are holding digit values from 0 to 9 to perform arithmetic operations correctly. There are two words are given and another word is given an answer of addition for those two words.As an example, we can say that two words ‘BASE’ and ‘BALL’, and the result is ‘GAMES’. Now if we try to add BASE and BALL by their symbolic digits, we will get the answer GAMES.<b>There must be ten letters maximum, otherwise it cannot be solved.</b></p>\
                        <img src='assets/Example.jpg'>\
                      <br>\
                      <br>\
                     <a href='https://github.com/rahulkhattri0/Cryptarithmetic-Problem-solver'>Source Code of this Project.</a>"
                      )
    label.pack(padx=20,pady=20)

menu = Menu(root)
root.config(menu=menu)
file_menu = Menu(menu)
menu.add_cascade(label="Help",menu=file_menu)
file_menu.add_command(label="About",command=abtCmd)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.destroy)
# root.iconbitmap(bitmap="C:/Users/hp/Desktop/python stuff/cryparith/Cryptarithmetic-Problem-solver-main/creative.png")
# myImg = ImageTk.PhotoImage(Image.open("thinking.png"))
# imglabel = Label(image=myImg).grid(row=1,column=2)
Label(text="Cryptarithmetic Problem Solver!").grid(row=0,column=2)
number = Label(root,text="Input Strings\n(Pease enter minimum 2 strings,separated by commas)").grid(row=3,column=1)
result = Label(root,text="Result String").grid(row=4,column=1)
numberval = IntVar()
resultval = StringVar()
print(type(numberval))
numberentry = Entry(root,textvariable=numberval)
resultentry = Entry(root,textvariable=resultval)
numberentry.grid(row=3,column=2)
resultentry.grid(row=4,column=2)
root.mainloop()