from tkinter import *
root=Tk()
root.geometry("500x500")
root.title("LIST")
l1=Label(root,text="NAME")
l1.place(x=500,y=10)
e1=Entry(root)
e1.place(x=580,y=10)

l2=Label(root,text="AGE")
l2.place(x=500,y=70)
e2=Entry(root)
e2.place(x=580,y=70)
def submit():
    
    print("submit")
 
b=Button(root,text="Submit",command=submit)
b.place(x=580,y=120)

root.mainloop()