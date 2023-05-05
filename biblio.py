import ttkbootstrap as tk
import tkinter.ttk as ttk
from bibliotdata import connex as Cs
import tkinter.messagebox as popup
from PIL import Image, ImageTk
Id=None
conn=Cs()
conn.connect()
#--------------------functions-------------------------
#-------------------addlivre--------------------
def addlivre():
    livre=inputti.get()
    auteur=inputaut.get()
    image=inputimg.get()
    datep=inputdate.get()
    if livre=="" or auteur=="":
        popup.showerror('Message','cannot insert liver without title or auteur')
    else:
        print(f"add livre {livre}")
        conn.add(livre,image,auteur,datep)
        show()
        popup.showinfo('Message','livre added successfully')
#showlivre--------------------------------------------
def show():
    inputti.delete(0,'end')
    global ID
    inputaut.delete(0,'end')
    inputimg.delete(0,'end')
    inputdate.delete(0,'end')
    my_tree.delete(*my_tree.get_children())
    ID=None
    livres=conn.getAll()
    for livre in livres:
        my_tree.insert(parent="", index=tk.END, text=livre[0],values=(livre[1],livre[2],livre[3],livre[4]))
#deletelivre---------------------------------------------------
def deletelivre():
     conn.delete(ID)
     show()
     popup.showinfo('Message','livre deleted successfully')
#selection of item for delete and update:
def selectItem(event):
    global ID
    seletedItem=my_tree.selection()[0]
    ID=my_tree.item(seletedItem)["text"]
    values=my_tree.item(seletedItem)["values"]
    inputti.delete(0,'end')
    inputaut.delete(0,'end')
    inputimg.delete(0,'end')
    inputdate.delete(0,'end')
    inputti.insert(0,values[0])
    inputaut.insert(0,values[2])
    inputimg.insert(0,values[1])
    inputdate.insert(0,values[3])
    print(f"select {id}")
#updatefunction:
def updatelivre():
    global ID
    if ID != None:
        conn.update(titre=inputti.get(),image=inputimg.get(),auteur=inputaut.get(),datep=inputdate.get(),id=ID)
        show()
    print(f"update livre {ID}")
    
def chercherlivre():
    my_tree.delete(*my_tree.get_children())
    if inputti.get()!="":
     livres=conn.getlivretitre(titre=inputti.get())
    elif inputaut.get()!="":
        livres=conn.getlivreaut(auteur=inputaut.get())
    elif inputdate.get()!="":
        livres=conn.getlivredate(date=inputdate.get())
    else:
        popup.showerror('Message','cannot search from epmy inputs')
    if not livres:
      popup.showerror('Message','livre not found')
    else:
            inputti.delete(0,'end')
            global ID
            inputaut.delete(0,'end')
            inputimg.delete(0,'end')
            inputdate.delete(0,'end')
            ID=None
            for livre in livres:
                my_tree.insert(parent='',index=tk.END, text=livre[0],values=(livre[1],livre[2],livre[3],livre[4]))





#interface-----------------------------------------------------------------------
window=tk.Window(themename="darkly")
window.geometry("1920x550")
window.title("library")
#image=Image.open("library.png")
#bck_end=ImageTk.PhotoImage(image)
#lbl=tk.Label(window,image=bck_end)
#lbl.place(x=0,y=0)
#=======================================================================#
s=tk.Style()
#----------------------table-----------------------------
s.configure('Treeview', rowheight=50)
my_tree=tk.Treeview(window,columns=("titre","image","auteur","datedepub"),height=50)
my_tree.heading("#0",text="ID")
my_tree.heading("titre",text="Titre")
my_tree.heading("image",text="Image")
my_tree.heading("auteur",text="Auteur")
my_tree.heading("datedepub",text="Date de pub")
my_tree.column("#0",width=50)
my_tree.column("titre",width=200)
my_tree.column("image",width=100)
my_tree.column("auteur",width=200)
my_tree.column("datedepub",width=100)
my_tree.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
#----------------greeting-----------------------
greeting = tk.Label(text="welcome to our library",bootstyle="primary")
greeting.pack(pady=20)
#----------------chercher-----------------------------
#---------------------titre--------------------------------
titelab=tk.Label(text="titre")
titelab.pack(padx=100,pady=10)
inputti=tk.Entry(window)
inputti.pack(side=tk.TOP)
#-----------------------auteur---------------------
auteurlab=tk.Label(text="Auteur")
auteurlab.pack(padx=20,pady=10)
inputaut=tk.Entry(window)
inputaut.pack(side=tk.TOP)
#-----------------image------------------
imagelab=tk.Label(text="image(optionnel)")
imagelab.pack(padx=10,pady=10)
inputimg=tk.Entry(window,)
inputimg.pack(side=tk.TOP)
#-----------------date-----------------------
datedepublab=tk.Label(text="date de publication(optionnel)")
datedepublab.pack(padx=10,pady=10)
inputdate=tk.Entry(window)
inputdate.pack(side=tk.TOP)
#---------------buttons--------------------------
cherch_button=tk.Button(window,text="chercher",command=chercherlivre,bootstyle="outline-toolbutton")
cherch_button.pack(side=tk.TOP, padx=5, pady=5)
add_button=tk.Button(window,text="add",command=addlivre,bootstyle="outline-toolbutton")
add_button.pack(side=tk.TOP,padx=20,pady=10)
my_tree.bind('<ButtonRelease-1>',selectItem)
show()
delete_button=tk.Button(window,text="Delete",command=deletelivre,bootstyle="outline-toolbutton")
delete_button.pack(side=tk.TOP, padx=5, pady=5)
update_button=tk.Button(window,text="update",command=updatelivre,bootstyle="outline-toolbutton")
update_button.pack(side=tk.TOP, padx=5, pady=5)
showall_button=tk.Button(window,text="show all",command=show,bootstyle="outline-toolbutton")
showall_button.pack(side=tk.TOP, padx=5, pady=5)













window.mainloop()