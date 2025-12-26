from tkinter import*
from tkinter import messagebox
from PIL import  Image,ImageTk

balance=50000
root=Tk()
root.title("image button")
root.geometry("500x500")
bg_image=Image.open("bank image.webp")

bg_photo=ImageTk.PhotoImage(bg_image.resize((500,300)))
bg_label=Label(root,image=bg_photo)
bg_label.place(x=0,y=1,relwidth=1,relheight=1)
def clicked_Button():
   new= Tk ()
   new.title("Login page")


   l=Label(new,text="USER NAME",font=("Times New Roman",16,"bold"))
   l.place(x=500,y=200)
   l2=Label(new,text=":",font=("Times New Roman",18,"bold"))
   l2.place(x=650,y=198)
   e=Entry(new)
   e.place(x=680,y=205)
   l1=Label(new,text="PASSWORD",font=("Times New Roman",16,"bold"))
   l1.place(x=500,y=280)
   l3=Label(new,text=":",font=("Times New Roman",18,"bold"))
   l3.place(x=650,y=278)
   e1=Entry(new)
   e1.place(x=680,y=285)
   def submit():
      z=e.get()
      y=e1.get()
      if z=="Aru@07" and y=="@Aru123":
         messagebox.showinfo("Loading","Please wait a moment!")
         messagebox.showinfo("Login","Login Successfully")
         new1=Tk()
         new1.title("Third page")
         def detail():
            new2=Tk()
            new2.title("DETAILS")
            new2.geometry("1000x600")
         
            l=Label(new2,text="ACCOUNT HOLDER NAME : PRAVEENKUMAR",font=("Times New Roman",16,"bold"))
            l.place(x=400,y=100)
            l1=Label(new2,text="ACCOUNT NO : 3520147891010",font=("Times New Roman",16,"bold"))
            l1.place(x=400,y=260)
            l2=Label(new2,text="ADDRESS : KARUVI, POOMBUKAR",font=("Times New Roman",16,"bold"))
            l2.place(x=400,y=180)
            l3=Label(new2,text="PHONE NO : 6381626258",font=("Times New Roman",16,"bold"))
            l3.place(x=400,y=340)
            l4=Label(new2,text="IFSC : IOB101225",font=("Times New Roman",16,"bold"))
            l4.place(x=400,y=420)
            l5=Label(new2,text="BANK ADDRESS : MAYILADUTHURAI",font=("Times New Roman",16,"bold"))
            l5.place(x=400,y=500)

            new2.mainloop()

         det=Button(new1,text="DETAILS",font=("Calibri",20,"bold"),command=detail)
         det.place(x=180,y=350)

         def baln():
            t="Your Account Balance :"+str(balance)
            messagebox.showinfo("Balance",t)

         blns=Button(new1,text="BALANCE",font=("Times New Roman",20,"bold"),command=baln)
         blns.place(x=450,y=350)

         def wdraw():
            if balance==0:
               messagebox.showerror("ERROR","Insufficient Balance! You can unable to withdraw the Amount.")
            else:
               new3=Tk()
               new3.title("Withdraw")

               y1=Label(new3,text="Account Balance is :",font=("Times New Roman",20,"bold"))
               y1.place(x=450,y=200)
               y2=Label(new3,text=balance,font=("Times New Roman",20,"bold"))
               y2.place(x=750,y=200)
               y=Label(new3,text="Enter your Amount",font=("Times New Roman",18,"bold"))
               y.place(x=450,y=305)
               x=Entry(new3)
               x.place(x=750,y=310)

               def okk():
                  y4=int(balance)-int(x.get())
                  messagebox.showinfo("Welcome",y4)

               y3=Button(new3,text="OK",font=("Times New Roman",18,"bold"),command=okk)
               y3.place(x=600,y=400)

               new3.mainloop()


         wdrw=Button(new1,text="WITHDRAW",font=("Times New Roman",20,"bold"),command=wdraw)
         wdrw.place(x=760,y=350)
         
         def dept(y4):
            new4=Tk()
            new4.title("Deposit")

            z1=Label(new4,text="Account Balance is :",font=("Times New Roman",20,"bold"))
            z1.place(x=450,y=200)
            z2=Label(new4,text=y4,font=("Times New Roman",20,"bold"))
            z2.place(x=750,y=200)
            z3=Label(new4,text="Enter your Amount",font=("Times New Roman",18,"bold"))
            z3.place(x=450,y=305)
            z4=Entry(new4)
            z4.place(x=750,y=310)

            def okk1():
               z5=int(y4)+int(z4.get())
               messagebox.showinfo("Welcome",z5)

            y3=Button(new4,text="OK",font=("Times New Roman",18,"bold"),command=okk1)
            y3.place(x=550,y=500)

            new4.mainloop()

         dep=Button(new1,text="DEPOSIT",font=("Times New Roman",20,"bold"),command=dept)
         dep.place(x=1100,y=350)
      
         new1.mainloop()
      else:
         messagebox.showerror("ERROR","LOGIN FAILED")
      
     

   b=Button(new,text="SUBMIT",font=("Calibri",16,"bold"),command=submit)
   b.place(x=610,y=360)

   new.mainloop()

b1=Button(bg_label,text="LOGIN",font=("Calibri",20,"bold"),bg="white",command=clicked_Button)
b1.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()