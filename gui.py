from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkhtmlview import HTMLLabel
import threading
import algo
# algo object
ob = algo.cryp()
#main window object
root = Tk()
bgimg= ImageTk.PhotoImage(Image.open("assets/bg.jpg"))
bgLabel = Label(root,image=bgimg)
bgLabel.place(x=0,y=0,relheight=1,anchor="nw")
root.minsize(500,500)
root.title("Cryptarithmetic Problem Solver")
#submit

def validate():
    string = strings.get()
    res = resultval.get()
    string=string.upper()
    res=res.upper()
    l = string.split(sep=",")
    if(len(l)>0 and res!=""):
      loadingLabel=Label(text="getting your result....",bg="#c7cee8")
      #starting this in a background thread coz else this will keep executing in the main thread and block it after few seconds.
      bgThread = threading.Thread(target=submit,args=(l,res,loadingLabel))
      bgThread.start() 
    else:
       messagebox.showerror("Error!","Please fill out both the fields")
def submit(l,res,load):
   load.place(x=220,y=300)
   print(ob.isSolvable(l,res))
   load.place_forget()
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
myImg = ImageTk.PhotoImage(Image.open("assets/thinking.png"))
Label(text="Cryptarithmetic Problem Solver!".upper(),bg="#c7cee8").pack()
imglabel = Label(image=myImg,padx=10,pady=20,bg="#c7cee8").place(x=220,y=30)
number = Label(root,text="Input Strings",bg="#c7cee8").place(x=100,y=150)
result = Label(root,text="Result String",bg="#c7cee8").place(x=100,y=200)
strings = StringVar()
resultval = StringVar()
numberentry = Entry(root,textvariable=strings).place(x=210,y=150)
resultentry = Entry(root,textvariable=resultval).place(x=210,y=200)
mybtn = Button(text="SUBMIT",command=validate).place(x=230,y=250)
root.mainloop()