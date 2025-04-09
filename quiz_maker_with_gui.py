from tkinter import *
import quiz_maker as q_maker

bg_color = "#1a1a1a"
txt_color = "white"
title_font = ("Arial", 40, "bold")
button_font = ("Arial", 15)
button_color = "#333333"

tk = Tk()

def q():
    print("LOL")

def window_menu():
    title = Label(
        tk,
        text = "QUIZ MAKER",
        font = title_font,
        background = bg_color,
        foreground = txt_color
    )

    new_quiz = Button(
        tk,
        text = "Create New Quiz",
        font = button_font,
        bg = button_color,
        fg = txt_color,
        command = q
    )

    edit_quiz = Button(
        tk,
        text = "Edit Existing Quiz",
        font = button_font,
        bg = button_color,
        fg = txt_color,
        command = q
    )

    title.place(relx = 0.5, rely = 0.3, anchor = "center")
    new_quiz.place(relx = 0.5, rely = 0.6, anchor = "center")
    edit_quiz.place(relx = 0.5, rely = 0.75, anchor = "center")

if __name__ == "__main__":
    tk.title("Python Quiz Maker")
    tk.geometry("400x400")
    tk.configure(bg = bg_color) 

    window_menu()

    tk.mainloop()


    
