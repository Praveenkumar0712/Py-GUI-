'''from tkinter import * 
root=Tk()
a=["blue","red","pink","yellow","green"]
for i in a:
    f1=Frame(root,width="500",height="500",background=i)
    f1.grid(row=1,column=2)
l1=Label(root,text="hello",background="yellow",foreground="black",font=("Algerian",25,"bold"))

l1.place(x=150,y=150)
root.mainloop()

from tkinter import *
root=Tk()
l=Label(root,text="name")
l.grid(row=0,column=0)
a=Entry(root)
a.grid(row=0,column=1)
def button():
    c=a.get()
    print(c)
b=Button(root,text="save",command=button)
b.grid(row=2,column=1)
root.mainloop()'''
