from tkinter import *

root=Tk()
root.title("Calculator")

l1=Label(root,text="NO1 :")
l1.place(x=50,y=10)
e1=Entry(root)
e1.place(x=90,y=10)
l2=Label(root,text="NO 2:")
l2.place(x=200,y=10)
e2=Entry(root)
e2.place(x=250,y=10)
l3=Label(root,text="TOTAL :")
l3.place(x=350,y=10)
e3=Entry(root)
e3.place(x=420,y=10)


def add():
    a=int(e1.get())+int(e2.get())
    e3.delete(0,END)
    e3.insert(0,a)

b=Button(root,text="ADD",command=add)
b.place(x=50,y=80)
def sub():
    a=int(e1.get())-int(e2.get())
    e3.delete(0,END)
    e3.insert(0,a)

b=Button(root,text="SUB",command=sub)
b.place(x=150,y=80)
def mul():
    a=int(e1.get())*int(e2.get())
    e3.delete(0,END)
    e3.insert(0,a)

b=Button(root,text="MUL",command=mul)
b.place(x=250,y=80)
def div():
    a=int(e1.get())/int(e2.get())
    e3.delete(0,END)
    e3.insert(0,a)

b=Button(root,text="DIV",command=div)
b.place(x=350,y=80)
def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
b=Button(root,text="CLEAR",command=clear)
b.place(x=200,y=150)


root.mainloop()