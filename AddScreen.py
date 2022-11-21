from tkinter import *
from tkinter import ttk

from CustonEntry import CustomEntry
from DB import DB






class AddScreen(Toplevel):
    db = DB()
    def __init__(self,master):
        super().__init__(master)
        self.geometry("600x800")
        self.configure(bg="#FFFFFF")
        self.state("zoom")
        self.title("Book Store Filing System")
        self.width = 1000

        self.frame = Frame(self)
        self.frame.configure(bg="white")
        # grid starts here
        Label(self.frame, text="Add A Book", foreground="black",bg="white", font=("Arial Bold",20)).grid(row=0,column=0,columnspan=2,pady=20)

        Label(self.frame, text="Serial Number (ISBN): ", foreground="black",bg="white", font=("Arial Regular",20)).grid(row=1,column=0,pady=20, sticky="we")
        self.sn = CustomEntry(self.frame,width=20, highlightthickness=0)
        self.sn.grid(row=1,column=1)
        self.sn.focus_set()

        Label(self.frame, text="Book Title: ", foreground="black",bg="white", font=("Arial Regular",20)).grid(row=2,column=0,pady=20, sticky="we")
        self.b_title = CustomEntry(self.frame,width=20, highlightthickness=0)
        self.b_title.grid(row=2,column=1)

        Label(self.frame, text="Book Author: ", foreground="black",bg="white", font=("Arial Regular",20)).grid(row=3,column=0,pady=20, sticky="we")
        self.b_author = CustomEntry(self.frame,width=20, highlightthickness=0)
        self.b_author.grid(row=3,column=1)

        Label(self.frame, text="Price (GHc): ", foreground="black",bg="white", font=("Arial Regular",20)).grid(row=4,column=0,pady=20, sticky="we")
        self.price = CustomEntry(self.frame,width=20, highlightthickness=0)
        self.price.grid(row=4,column=1)

        Label(self.frame, text="Shelf: ", foreground="black",bg="white", font=("Arial Regular",20)).grid(row=5,column=0,pady=20, sticky="we")
        self.shelf = CustomEntry(self.frame,width=20, highlightthickness=0)
        self.shelf.grid(row=5,column=1)

        Label(self.frame, text="Row: ", foreground="black",bg="white", font=("Arial Regular",20)).grid(row=6,column=0,pady=20, sticky="we")
        self.row = CustomEntry(self.frame,width=20, highlightthickness=0)
        self.row.grid(row=6,column=1)

        Label(self.frame, text="Column: ", foreground="black",bg="white", font=("Arial Regular",20)).grid(row=7,column=0,pady=20, sticky="we")
        self.col = CustomEntry(self.frame,width=20, highlightthickness=0)
        self.col.grid(row=7,column=1)

        self.add_btn = Button(self.frame, text="Add Book Record",command=self.add_data, width=20,height=2,anchor=CENTER,background="green",font=("Arial Bold",23),foreground="white",relief="flat",bd=0,borderwidth=0, highlightthickness=0)
        self.add_btn.grid(row=8,column=0, columnspan=2, pady=10)

        self.cancel_btn = Button(self.frame, text="Cancel",command=lambda: self.destroy(), width=20,height=2,anchor=CENTER,background="white",font=("Arial Bold",23),foreground="black",relief="flat",bd=0,borderwidth=0, highlightthickness=0)
        self.cancel_btn.grid(row=9,column=0, columnspan=2, pady=10)

        self.frame.pack()
        # self.transient(self.master)
        # self.grab_set()
        # self.wait_window(self)

    def add_data(self):
        # get value in entry boxes
        sn = self.sn.get()
        b = self.b_title.get()
        author = self.b_author.get()
        price = self.price.get()
        shelf = self.shelf.get()
        row = self.row.get()
        col = self.col.get()
        self.clear()
         #call the db insert method
        self.db.insertData(sn=sn, author=author, title=b, price=price, shelf=shelf, row=row,col=col )


    def clear(self):
        # clear data in entry
        self.sn.delete(0, 'end')
        self.b_title.delete(0, 'end')

        self.b_author.delete(0, 'end')

        self.price.delete(0, 'end')

        self.shelf.delete(0, 'end')

        self.row.delete(0, 'end')

        self.col.delete(0, 'end')

