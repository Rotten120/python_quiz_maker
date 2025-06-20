from tkinter import Frame

class Window(Frame):
    def __init__(self, master, bg_color = "white"):
        super().__init__(master)
        self.__parent = master
        self.configure(bg = bg_color)

    def get_parent(self):
        return self.__parent

    def display(self):
        txt = pre_set.label2(self, "SAMPLE WINDOW")
        txt.pack()
