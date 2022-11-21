from tkinter import *
from tkinter import ttk

from CustonEntry import CustomEntry

from AddScreen import AddScreen
from DB import DB


class DataScreen(Tk):
    db = DB()

    def __init__(self):
        super().__init__()
        self.geometry("1024x900")
        self.configure(bg="#FFFFFF")
        self.title("Book Store Filing System")
        self.width = 1000
        # search bar
        self.search_bar_frame = Frame(self)
        self.search_bar_frame.configure(width=self.width, height=80, bg="white")
        Label(self.search_bar_frame, text="Search for a book", bg="white", fg="blue", font=("Arial Bold", 27)).grid(
            row=0, column=0, sticky='w', pady=5)

        self.searchBox = Entry(self.search_bar_frame, width=55, highlightthickness=0, fg="black", bg="white",
                               cursor="ibeam", insertbackground="black", borderwidth=2, font=("Helvetica", 20))
        self.searchBox.grid(row=1, column=0, ipady=10)
        search_btn = Button(self.search_bar_frame, text="Search", width=10, height=2, relief="flat",command=self.on_search_click)
        search_btn.grid(row=1, column=1, padx=5)
        Label(self.search_bar_frame, text="Search by: *name *ISBN *Author", bg="white", fg="red", font=("Helvetica", 12)).grid(
            row=2, column=0, sticky='w',)
        self.search_bar_frame.pack(padx=20, pady=30)

        # data table
        self.table_frame = Frame(self)
        self.table_frame.configure(width=self.width, height=300, )
        col_names = ("1", "2", "3", "4", "5", "6")
        s = ttk.Style()
        s.theme_use('clam')

        self.table = ttk.Treeview(self.table_frame, columns=col_names, height=20, )

        self.table.column("#0", anchor=E, width=100, stretch=False)
        self.table.column("1", anchor=CENTER, width=200)
        self.table.column("2", anchor=CENTER, width=150, minwidth=100, stretch=False)
        self.table.column("3", anchor=CENTER, width=150, minwidth=100, stretch=False)
        self.table.column("4", anchor=CENTER, width=100, stretch=False)
        self.table.column("5", anchor=CENTER, width=100, stretch=False)
        self.table.column("6", anchor=CENTER, width=100, stretch=False)
        self.table.pack(fill=BOTH, expand=True, )

        self.table.heading("#0", text="ISBN")
        self.table.heading("1", text="Book Title")
        self.table.heading("2", text="Author")
        self.table.heading("3", text="Price")
        self.table.heading("4", text="Shelf")
        self.table.heading("5", text="Columns")
        self.table.heading("6", text="Row")
        self.data = self.db.fetchBooksData()
        for d in self.data:
            self.table.insert(parent="",
                              index=END,
                              text=d[0],
                              values=(d[1], d[6], d[2], d[3], d[5], d[4]))
        self.table_frame.pack()

        # operational buttons FRAME
        self.buttons_frame = Frame(self)
        self.buttons_frame.configure(width=self.width, height=200, pady=30, bg="white")

        #         buttons
        self.add_btn = Button(self.buttons_frame, text="Add Book", width=20, height=5, anchor=CENTER,
                              background="green", foreground="white", relief="flat", bd=0, borderwidth=0,
                              highlightthickness=0, command=self.on_add_btn_clicked)
        self.add_btn.grid(row=0, column=0, rowspan=2, sticky="we", padx=30)

        self.refresh_btn = Button(self.buttons_frame, text="Refresh Book Data", width=20, height=5, anchor=CENTER,
                                  background="blue", foreground="white", relief="flat", bd=0, borderwidth=0,
                                  highlightthickness=0, command=self.refresh_table)
        self.refresh_btn.grid(row=0, column=1, padx=30)

        self.close_btn = Button(self.buttons_frame, text="Close App", width=20, height=5, anchor=CENTER,
                                background="red", foreground="white", relief="flat", bd=0, borderwidth=0,
                                highlightthickness=0, command=lambda: self.destroy())
        self.close_btn.grid(row=0, column=2, padx=30)
        self.buttons_frame.pack(expand=True)

    def on_add_btn_clicked(self):
        add_window = AddScreen(self)

    def refresh_table(self):
        refdb = DB()
        for item in self.table.get_children():
            self.table.delete(item)
        data = refdb.fetchBooksData()
        # print(">___________________________________________________________<")
        for d in data:
            # print(d)
            self.table.insert(parent="",
                              index=END,
                              text=str(d[0]),
                              values=(d[1], d[6], d[2], d[3], d[5], d[4]))
        # print("<___________________________________________________________>")

    def on_search_click(self):
        q = self.searchBox.get()
        for item in self.table.get_children():
            self.table.delete(item)
        for d in self.data:
            if q.lower() in str(d[0].lower()) or q.lower() in str(d[1].lower()) or q.lower() in str(d[6].lower()):
                self.table.insert(parent="",
                                  index=END,
                                  text=str(d[0]),
                                  values=(d[1], d[6], d[2], d[3], d[5], d[4]))





if __name__ == "__main__":
    controlWindow = DataScreen()
    # controlWindow.resizable(False, False)
    controlWindow.mainloop()
