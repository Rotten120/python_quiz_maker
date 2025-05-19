from tkinter import Toplevel as top_level

class SubScreen(top_level):
    def __init__(self, master, title = "tkinter", size = "500x500", pos = "", pages = {}):
        super().__init__(master)
        self.parent = master
        self.title(title)
        self.geometry(size + "+" + pos)
        self.windows = pages

    def add_window(self, page, bg_color = "white"):
        window = page(self, bg_color)
        self.windows[page] = window
        window.place(relwidth = 1, relheight = 1)

    def set_window(self, page):
        window = self.windows[page]
        window.display()
        window.tkraise()
