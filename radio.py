'''from tkinter import *
from tkinter import messagebox

root=Tk()

var=IntVar()

r1=Radiobutton(root,variable=var,value=1,text="Male")
r1.pack()
r2=Radiobutton(root,variable=var,value=2,text="Female")
r2.pack()

def submit():
    a=var.get()
    if a==1:
        print("YOU SELECTED MALE")
    elif a==2:
        print("YOU SELECTED FEMALE")
    else:
        messagebox.showinfo("ERROR","PLEASE SELECT AN ANY ONE OPTION")

b=Button(root,text="Submit",command=submit)
b.pack()

root.mainloop()'''


#checkbutton
from tkinter import *
from tkinter import messagebox

root=Tk()

var=IntVar()

r1=Checkbutton(root,variable=var,text="C")
r1.pack()
var1=IntVar()
r2=Checkbutton(root,variable=var1,text="PYTHON")
r2.pack()

def submit():
    a=var.get(),var1.get()
    if a==(1,0):
        messagebox.showinfo("info","You selected C")
    elif a==(0,1):
        messagebox.showinfo("info","confirm your cource")
    elif a==(1,1):
        print("You selected both C and Python")
        messagebox.showinfo("cource","you selected both")
    else:
        messagebox.showwarning("Warning","No selected")

b=Button(root,text="Submit",command=submit,background="pink")
b.pack()

root.mainloop()