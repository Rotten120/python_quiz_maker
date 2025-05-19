from tkinter import Tk

class MainScreen(Tk):
    def __init__(self, title = "tkinter", size = "500x500", pages = {}):
        super().__init__()
        self.title(title)
        self.geometry(size)
        self.windows = pages

    def add_window(self, page, bg_color = "white"):
        window = page(self, bg_color)
        self.windows[page] = window
        window.place(relwidth = 1, relheight = 1)

    def set_window(self, page):
        window = self.windows[page]
        window.display()
        window.tkraise()
