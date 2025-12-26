from tkinter import*
root=Tk()
a=["red","blue","green","pink"]
for i in a:
    f1=Frame(root,width="150",height="150",background=i)
    f1.pack()
root.mainloop()    
