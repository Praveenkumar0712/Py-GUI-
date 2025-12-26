from tkinter import*
root=Tk()
l1=Label(root,text="NAME")
l2=Label(root,text="AGE")
l1.grid(row=0,column=1)
l2.grid(row=1,column=1)
a=Entry(root)
e=Entry(root)
d=Entry(root)
e.grid(row=1,column=2)
a.grid(row=0,column=2)
d.grid(row=2,column=3)
def calc():
   d=(a+e)
   print(d)
b=Button(root)
b.grid(row=2,column=2)
root.mainloop()      

  