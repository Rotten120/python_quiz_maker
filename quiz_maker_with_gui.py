from tkinter import *
from tkinter.ttk import *
import quiz_maker as q_maker

bg_color = "#1a1a1a"
txt_color = "white"
title_font = ("Arial", 30, "bold")

if __name__ == "__main__":
    tk = Tk()
    tk.title("Python Quiz Maker")
    tk.geometry("600x600")
    tk.configure(bg = bg_color)

    label = Label(tk, text="QUIZ MAKER",
                  font = title_font,
                  background = bg_color,
                  foreground = txt_color
    )
    label.place(relx = 0.5, rely = 0.2, anchor = "center")

    tk.bind("<FocusIn>", func)

    tk.mainloop()


    
