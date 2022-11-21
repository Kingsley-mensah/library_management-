from tkinter import Toplevel, Frame, Tk, Label, Button, CENTER

import mysql.connector


class DB:
    mydb = ""
    cursor = ""
    db_name = "Bookstore"
    bdb = "books"
    def __init__(self):
        self.is_import = None
        self.mydb = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="eugenedev",
            database=self.db_name
        )

        self.cursor = self.mydb.cursor()


    def fetchBooksData(self):
        query = "select * from {}".format(self.bdb)
        self.cursor.execute(query)
        rs = self.cursor.fetchall()
        return rs

    def insertData(self,sn,title,author,price,shelf,row,col):
        query = f"INSERT INTO `{self.bdb}`(`sn`, `title`, `price`, `shelf`, `shelf_row`, `shelf_col`,`author`) VALUES ('{sn}', '{title}', {float(price)}, '{shelf}', '{col}', '{row}','{author}');"
        try:
            self.cursor.execute(query)
            self.mydb.commit()
            NotifyWindow("Book added successfully")
        except:
            self.mydb.rollback()
            NotifyWindow("Error adding book")



class NotifyWindow(Tk):
    def __init__(self,message):
        super().__init__()

        self.frame = Frame(self)

        self.message = Label(self,text=message,fg="white")
        self.message.pack()
        self.ok_btn = Button(self,text="Okay",command=lambda: self.destroy())
        self.ok_btn.pack(anchor=CENTER,ipadx=2,)
        self.frame.pack(pady=20,padx=20)
        self.resizable(False,False)
        self.mainloop()
