from tkinter import *
import quiz_maker as q_maker
import ele_pre_sets as pre_set
import os

tk = Tk()

def clear_screen():
    for widget in tk.winfo_children():
        widget.destroy()
    
def check_file_dir(file_path):
    if not file_path.endswith(".txt"):
        file_path += ".txt"
    if not os.path.exists(file_path):
        new_quiz()
    else:
        lbl_txt = "* Fule already exists"
        notice = pre_set.label2(tk, lbl_txt, "red")
        notice.place(relx = 0.03, rely = 0.15)

def add_question(quest, opt_a, opt_b, opt_c, opt_d, ans):
    pass

def new_quiz():
    clear_screen()

    label_texts = [
        "Question", "Option A", "Option B", "Option C",
        "Option D", "Correct Option"
    ]
    
    labels = [pre_set.label1(tk, txt) for txt in label_texts]
    texts = [pre_set.text1(tk, 50, 2) for i in range(len(label_texts) - 1)]
    ans_text = Entry(tk, width = 1, font = pre_set.subtitle_font)

    reset = pre_set.button1(tk, "Clear", lambda: new_quiz(file_path))
    done = pre_set.button1(tk, "Back", window_menu)
    confirm = pre_set.button1(
        tk, "Add", lambda: add_question(
            [text.get("1.0", "end-1c") for text in texts],
            ans_text.get("1.0", "end-1c")
        )    
    )

    for idx, label in enumerate(labels):
        label.place(x = 10, y = 10 + idx * 70)
    for idx, text in enumerate(texts):
        text.place(x = 10, y = 40 + idx * 70)
    ans_text.place(x = 160, y = 360)
    
    confirm.place()
    reset.place()
    done.place()

def get_file_path():
    clear_screen()
    
    sub_txt = "Input file name"
    subtitle = pre_set.label1(tk, sub_txt)

    inp_file = Entry(
        tk,
        font = ("Arial", 10),
        width = 30,
        bg = pre_set.dark_color,
        fg = pre_set.txt_color
    )

    conf_txt = "Confirm"
    confirm = pre_set.button1(
        tk, conf_txt, lambda: check_file_dir(inp_file.get())
    )    
    
    subtitle.place(relx = 0.2, rely = 0.05, anchor = "center")
    inp_file.place(relx = 0.29, rely = 0.12, anchor = "center")
    confirm.place(relx = 0.88, rely = 0.94, anchor = "center")

def window_menu():
    title = Label(
        tk, text = "QUIZ MAKER",
        font = ("Arial", 40, "bold"),
        bg = pre_set.bg_color, fg = pre_set.txt_color
    )

    new_txt = "Create New Quiz"
    new_quiz = pre_set.button2(tk, new_txt, get_file_path)

    edit_txt = "Edit Existing Quiz"
    edit_quiz = pre_set.button2(tk, edit_txt, get_file_path) 

    title.place(relx = 0.5, rely = 0.3, anchor = "center")
    new_quiz.place(relx = 0.5, rely = 0.6, anchor = "center")
    edit_quiz.place(relx = 0.5, rely = 0.75, anchor = "center")

if __name__ == "__main__":
    tk.title("Python Quiz Maker")
    tk.geometry("400x400")
    tk.configure(bg = pre_set.bg_color) 

    window_menu()

    tk.mainloop()


    
