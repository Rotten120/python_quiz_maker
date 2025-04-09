from tkinter import *
import quiz_maker as q_maker
import os

bg_color = "#1a1a1a"
title_font = ("Arial", 40, "bold")
subtitle_font = ("Arial", 15, "bold")
button_font = ("Arial", 15)

txt_color = "white"
dark_color = "#333333"

tk = Tk()

def clear_screen():
    for widget in tk.winfo_children():
        widget.destroy()

def check_file_dir(file_path):
    

def new_quiz_menu():
    clear_screen()
    
    subtitle = Label(
        tk,
        text = "Input file name",
        font = subtitle_font,
        background = bg_color,
        foreground = txt_color
    )

    inp_file = Entry(
        tk,
        font = ("Arial", 10),
        width = 30,
        background = dark_color,
        foreground = txt_color
    )


    confirm = Button(
        tk,
        text = "Confirm",
        font = button_font,
        background = dark_color,
        foreground = txt_color
        command = lambda: check_file_dir(inp_file.get())
    )
    
    subtitle.place(relx = 0.2, rely = 0.05, anchor = "center")
    inp_file.place(relx = 0.29, rely = 0.12, anchor = "center")
    confirm.place(relx = 0.88, rely = 0.94, anchor = "center")

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
        bg = dark_color,
        fg = txt_color,
        command = new_quiz_menu
    )

    edit_quiz = Button(
        tk,
        text = "Edit Existing Quiz",
        font = button_font,
        bg = dark_color,
        fg = txt_color,
        command = new_quiz_menu
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


    
