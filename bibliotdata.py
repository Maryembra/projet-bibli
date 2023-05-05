import mysql.connector as mc

class connex:
    def __init__(self):
        self.host="localhost"
        self.database="bibliothèque"
        self.user="root"
        self.password=""
        self.port=3306
        self.conn=None
        self.Cursor=None
        self.table="livres"
#connecte=================================
    def connect(self):
        try:
         self.conn=mc.connect(host=self.host,database=self.database,user=self.user,password=self.password)
         print("connection is done")   
        except mc.Error as er:
            print(er)
        self.Cursor=self.conn.cursor()
#disconnecte===============================
    def disconnect(self):
        if self.cursor:
            self.cursor.close
        if self.conn:
            self.conn.close
#get all from a table=====================
    def getAll(self):
        req=f"select * from {self.table}"
        self.Cursor.execute(req)
        livres=self.Cursor.fetchall()
        return livres
#get specific livre by titre========================
    def getlivretitre(self,titre):
        req=f"select * from {self.table} where titre like %s"
        values=(titre+'%',)
        self.Cursor.execute(req,values)
        livres=self.Cursor.fetchall()
        return livres
#get specific livre by auteur========================
    def getlivreaut(self,auteur):
        req=f"select * from {self.table} where auteur like %s"
        values=(auteur+'%',)
        self.Cursor.execute(req,values)
        livres=self.Cursor.fetchall()
        return livres
#get specific livre by date========================
    def getlivredate(self,date):
        req=f"select * from {self.table} where annedepub like %s"
        values=(date+'%',)
        self.Cursor.execute(req,values)
        livres=self.Cursor.fetchall()
        return livres
#add======================================
    def add(self,titre,image,auteur,annedepub):
        req=f"insert into {self.table}(titre,image,auteur,annedepub)values(%s,%s,%s,%s)"
        values=(titre,image,auteur,annedepub)
        self.Cursor.execute(req,values)
        self.conn.commit()
#update===================================
    def update(self,titre,image,auteur,datep,id):
        req=f"update {self.table} set titre=%s,image=%s,auteur=%s,annedepub=%s where id=%s"
        values=(titre,image,auteur,datep,id)
        self.Cursor.execute(req,values)
        self.conn.commit()
#delete
    def delete(self,id):
        req=f"delete from {self.table} where id=%s"
        values=(id,)
        self.Cursor.execute(req,values)
        self.conn.commit()
        print("deletete succesfully")

database=connex()
database.connect()
#database.add("le dernier","img","ahmed","2002-08-22")
#print(database.getAll())
#database.delete("le dernier")