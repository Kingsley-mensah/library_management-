from tkinter import Entry


class CustomEntry(Entry):
    def __init__(self, *args, **kwargs):
        kwargs["borderwidth"] = 1
        kwargs["background"] = "white"
        kwargs["foreground"] = "black"
        kwargs["cursor"] = "ibeam"
        kwargs["insertbackground"] = "black"


        kwargs["font"] = ("Arial Regular",19)
        super().__init__(*args, **kwargs)
