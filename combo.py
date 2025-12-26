from tkinter import *
from tkinter import ttk

root=Tk()
root.geometry("300x300")
root.title("Tkinter Combobox Example")

l=Label(root,text="Choose an option")
l.pack(padx=10,pady=50)

options=["--default--","India","Singapore","USA","US","France"]
a=ttk.Combobox(root,values=options) 
a.pack(padx=0,pady=1)

a.set(options[0])

def show_selection():
    print("DEFAULT",a.get())
c=Button(root,text="Cancel",command=__file__,background="yellow")
c.pack(padx=6,pady=10)
b=Button(root,text="Submit",command=show_selection,background="green")
b.pack(padx=5,pady=11)

root.mainloop()
