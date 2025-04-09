from tkinter import *
import quiz_maker as q_maker
import os

bg_color = "#1a1a1a"
title_font = ("Arial", 40, "bold")
subtitle_font = ("Arial", 15, "bold")
small_text_font = ("Arial", 10)
button_font = ("Arial", 15)

txt_color = "white"
dark_color = "#333333"

tk = Tk()

def clear_screen():
    for widget in tk.winfo_children():
        widget.destroy()
    
def check_file_dir(file_path):
    if not file_path.endswith(".txt"):
        file_path += ".txt"

    print(file_path)

    if not os.path.exists(file_path):
        new_quiz()
    else:
        notice = Label(
            tk,
            text = "* File already exists",
            font = small_text_font,
            background = bg_color,
            foreground = "red"
        )

        notice.place(relx = 0.03, rely = 0.15)

def add_question(quest, opt_a, opt_b, opt_c, opt_d, ans):
    pass

def new_quiz():
    clear_screen()

    label1 = Label(
        tk,
        text = "Question",
        font = subtitle_font,
        background = bg_color,
        foreground = txt_color
    )

    label2 = Label(
        tk,
        text = "Option A",
        font = subtitle_font,
        background = bg_color,
        foreground = txt_color
    )

    label3 = Label(
        tk,
        text = "Option B",
        font = subtitle_font,
        background = bg_color,
        foreground = txt_color
    )

    label4 = Label(
        tk,
        text = "Option C",
        font = subtitle_font,
        background = bg_color,
        foreground = txt_color
    )

    label5 = Label(
        tk,
        text = "Option D",
        font = subtitle_font,
        background = bg_color,
        foreground = txt_color
    )

    label6 = Label(
        tk,
        text = "Correct Option",
        font = subtitle_font,
        background = bg_color,
        foreground = txt_color
    )

    quest_text = Text(
        tk,
        height = 2,
        width = 40,
        font = small_text_font
    )

    opt_a_text = Text(
        tk,
        height = 2,
        width = 40,
        font = small_text_font
    )

    opt_b_text = Text(
        tk,
        height = 2,
        width = 40,
        font = small_text_font
    )

    opt_c_text = Text(
        tk,
        height = 2,
        width = 40,
        font = small_text_font
    )

    opt_d_text = Text(
        tk,
        height = 2,
        width = 40,
        font = small_text_font
    )

    ans_text = Entry(
        tk,
        width = 1,
        font = subtitle_font
    )

    confirm = Button(
        tk,
        text = "Add",
        font = subtitle_font,
        background = dark_color,
        foreground = txt_color,
        command = lambda: add_question(
                quest_text.get("1.0", "end-1c"),
                opt_a_text.get("1.0", "end-1c"),
                opt_b_text.get("1.0", "end-1c"),
                opt_c_text.get("1.0", "end-1c"),
                opt_d_text.get("1.0", "end-1c"),
                ans_text.get("1.0", "end-1c")
            )
    )

    reset = Button(
        tk,
        text = "Clear",
        font = subtitle_font,
        background = dark_color,
        foreground = txt_color
        command = lambda: new_quiz()
    )

    label1.place(x = 10, y = 10)
    label2.place(x = 10, y = 80)
    label3.place(x = 10, y = 150)
    label4.place(x = 10, y = 220)
    label5.place(x = 10, y = 290)
    label6.place(x = 10, y = 360)
    
    quest_text.place(x = 10, y = 40)
    opt_a_text.place(x = 10, y = 110)
    opt_b_text.place(x = 10, y = 180)
    opt_c_text.place(x = 10, y = 250)
    opt_d_text.place(x = 10, y = 320)
    ans_text.place(x = 160, y = 360)

def get_file_path():
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
        foreground = txt_color,
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
        command = get_file_path
    )

    edit_quiz = Button(
        tk,
        text = "Edit Existing Quiz",
        font = button_font,
        bg = dark_color,
        fg = txt_color,
        command = get_file_path
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


    
