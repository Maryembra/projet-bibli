from tkinter import *
from  subprocess import call
from PIL import Image, ImageTk
from tkinter import ttk ,Tk
from tkinter import messagebox
import mysql.connector
def connexion():
    call(["python","signin.py"])

def Inscription():
    user=txtuser.get()
    password=txtmot.get()
    password_conf=txtmotcon.get()
   
    if(user==""or password=="" or password_conf==""):
        messagebox.showerror("","il faut saisir tous les informations")
    elif (password!=password_conf):
        messagebox.showerror("","mot de passe incorrect")
    else:
        try: 
            maBase=mysql.connector.connect(host="localhost",user="root",password="",database="bibliothèque")
            meConnect=maBase.cursor()
            sql="select *from utilisateur where username='{}'".format(txtuser.get())
            meConnect.execute(sql)
            rows=meConnect.fetchone()
            if rows!=None:
                messagebox.showerror("Erreur","Ce user existe déja")
            else:
                 sql="INSERT INTO utilisateur(username,password,password_confirma) VALUES (%s,%s,%s)"
                 val=(user,password,password_conf)
                 meConnect.execute(sql,val)    
                 maBase.commit()
                 call(["python","signin.py"])
                 

        except Exception as e:
            print(e)
            maBase.rollback()
            maBase.close()
root=Tk()
root.title("Sign up")
root.geometry("925x500+300+200")#largeur*longeur right+left
root.resizable(FALSE,False)
root.configure(background="#fff")
image1=Image.open("image/signup.webp")
test=ImageTk.PhotoImage(image1)
label1=Label(image=test,border=0,width=500)
label1.place(x=10,y=30)
frame=Frame(root,bg="white",width=325,height=400)
frame.place(x=550,y=50)
heading=Label(frame,text="Sign up",fg="#57a1f8",bg="white",font=("Arial",23))
heading.place(x=100,y=5)
txtuser=Entry(frame,bd=0,font=("Arial",13),width=25)
txtuser.place(x=5,y=80)
txtuser.insert(0,"Username")
Frame(frame,width=300,bg="black",height=2).place(x=5,y=110)
txtmot=Entry(frame,bd=0,font=("Arial",13),width=25)
txtmot.place(x=5,y=150)
txtmot.insert(0,"Password")
Frame(frame,width=300,bg="black",height=2).place(x=5,y=180)
txtmotcon=Entry(frame,bd=0,font=("Arial",13),width=25)
txtmotcon.place(x=5,y=220)
txtmotcon.insert(0,"Confirm Password")
Frame(frame,width=300,bg="black",height=2).place(x=5,y=249)
btnins=Button(frame,text="Sign up",bg="#57a1f8",fg="white",bd=0,width=45,height=2,command=Inscription)#command=connexion
btnins.place(x=5,y=290)
label3=Label(frame,text="I have an account",fg="black",bg="white",font=("Arial",9))
label3.place(x=40,y=340)
btn2=Button(frame,text="Sign in",cursor="hand2",border=0,fg="#57a1f8",bg="white",command=connexion)
btn2.place(x=140,y=340)
root.mainloop()