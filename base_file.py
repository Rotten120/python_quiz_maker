from tkinter import *
import ele_pre_sets as pre_set

def cls(tk):
    for widget in tk.winfo_children():
        widget.destroy()

#window/s in obj refers to the same thing as page/s in parameters
#is the main screen
class Main_Screen(Tk):
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
        window.tkraise()

class Sub_Screen(Toplevel):
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
        window.tkraise()

#base class to be inherited by windows to be made
class Window(Frame):
    def __init__(self, master, bg_color = "white"):
        super().__init__(master)
        self.parent = master
        self.configure(bg = bg_color)
        self.display()

    def display(self):
        txt = pre_set.label2(self, "SAMPLE WINDOW")
        txt.pack()
