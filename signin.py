import tkinter
from tkinter import *
from  subprocess import call
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

def Seconnecter():
    surnom=txtUtilisateur.get()#utilisateur qui va pris cetee formation 
    mdp=txtmdp.get()
    if surnom=="" or mdp=="":
        messagebox.showerror("","il faut rentrer les données")#monter les erreurs
        txtmdp.delete("0","end") #si il y a des erreur on va effacer les champs
        txtUtilisateur.delete("0","end")
     
    else:
        maBase=mysql.connector.connect(host="localhost",user="root",password="",database="bibliothèque")
        meConnect=maBase.cursor()
        sql="select * from utilisateur where username='{}' and password='{}'".format(txtUtilisateur.get(),txtmdp.get())
        meConnect.execute(sql) 
        result = meConnect.fetchone()
        if result is not None:
             messagebox.showinfo("","Bienvenue")
             txtUtilisateur.delete("0","end")
             txtmdp.delete("0","end")
             root.destroy()#on a terminer
             call(["python","biblio.py"])
        else:
             txtUtilisateur.delete("0","end")
             txtmdp.delete("0","end")
             messagebox.showerror("","Nom d'utilisateur ou mot de passe invalide")
             maBase.close()
def SingUp():
    call(["python","signup.py"])
#ma fenetrE
root=Tk()
root.title("Login")
root.geometry("925x500+300+200")#largeur*longeur right+left
root.resizable(FALSE,False)
root.configure(background="#fff")
image1=Image.open("image/login.jpg")
test=ImageTk.PhotoImage(image1)
label1=Label(image=test)
label1.place(x=0,y=50)
frame=Frame(root,width=325,bg="white",height=410)
frame.place(x=550,y=50)
heading=Label(frame,text='Sign in',fg="#57a1f8",bg="white",font=("Arial",23))
heading.place(x=100,y=5)
#####username#####
txtUtilisateur=Entry(frame,bd=0,font=("Arial",13),width=25)
txtUtilisateur.place(x=30,y=80)
txtUtilisateur.insert(0,'Username')
Frame(frame,width=300,height=2,bg="black").place(x=25,y=100)
#####Password#####
txtmdp=Entry(frame,bd=0,font=("Arial",13),width=25)
txtmdp.place(x=30,y=140)
txtmdp.insert(0,'Password')
Frame(frame,width=300,bg="black",height=2).place(x=25,y=165)
####Boutton####
btn=Button(frame,text="Sing in",bd=0,height=2,width=42,bg='#57a1f8',fg="white",command=Seconnecter)
btn.place(x=30,y=200)
label=Label(frame,text="D'ont have an account?",fg="black",bg="white",font=("Arial",9))
label.place(x=70,y=250)
btn2=Button(frame,text="Sing in",width=6,bd=0,fg='#57a1f8',cursor="hand2",bg="white",command=SingUp)
btn2.place(x=200,y=250)
#execution
root.mainloop()