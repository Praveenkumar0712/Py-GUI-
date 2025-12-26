from tkinter import *
spk=Tk()
f2=Frame(spk,width="510",height="70",background="pink")
f2.grid(row=1,column=2)
la=Label(f2,text="Praveen",background="red",foreground="white",font=("Arial",20,"bold"))
la.grid(row=4,column=3)
b=Button(spk,text="Submit",background="gold")

b.grid(row=2,column=2)
spk.mainloop()