from tkinter import Frame as frame

class Window(frame):
    def __init__(self, master, bg_color = "white"):
        super().__init__(master)
        self.parent = master
        self.configure(bg = bg_color)

    def display(self):
        txt = pre_set.label2(self, "SAMPLE WINDOW")
        txt.pack()
