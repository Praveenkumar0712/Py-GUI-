from tkinter import*
root=Tk()
l=Label(root,text="name")
l.grid(row=0,column=0)
a=Entry(root)
a.grid(row=0,column=0)
def button():
    c=a.get()
    print(c)
b=Button(root,text="save",command=button)
b.grid(row=2,column=1)   
root.mainloop()