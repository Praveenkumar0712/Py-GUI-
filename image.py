from tkinter import*
from tkinter import messagebox
from PIL import  Image,ImageTk

root=Tk()
root.title("image")
root.geometry("700x500")
bg_image=Image.open("aiimage.jpg.jpg")
bg_photo=ImageTk.PhotoImage(bg_image.resize((300,200)))


bg_label=Label(root,image=bg_photo)
bg_label.place(x=0,y=1,relwidth=1,relheight=1)

bg_image1=Image.open("images.jpg.png")
bg_photo1=ImageTk.PhotoImage(bg_image1.resize((500,300)))

bg_label1=Label(root,image=bg_photo1)
bg_label1.place(x=100,y=150,relwidth=1,relheight=1)



b=Button(bg_label,text="click")
b.pack(padx=500,pady=500)
root.mainloop()