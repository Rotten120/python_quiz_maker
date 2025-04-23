from tkinter import *
from tkinter import filedialog
import quiz_maker as q_maker
import ele_pre_sets as pre_set
import os

tk = Tk()
quiz = q_maker.Quiz("")

def clear_screen():
    for widget in tk.winfo_children():
        widget.destroy()

def check_file_dir(file_path):
    if not file_path.endswith(".txt"):
        file_path += ".txt"
    if file_path == ".txt":
        lbl_txt = "* Invalid file name"
        notice = pre_set.label2(tk, lbl_txt, "red")
        notice.place(relx = 0.03, rely = 0.15)
    elif not os.path.exists(file_path):
        quiz.file_path = file_path
        add_question()
    else:
        lbl_txt = "* File already exists"
        notice = pre_set.label2(tk, lbl_txt, "red")
        notice.place(relx = 0.03, rely = 0.15)

def add_question(arr, ans):
    #arr is question, opta, optb, optc, optd respectively
    
    for inp in (arr + [ans]):
        if inp == "":
            lbl_txt = "* Empty input. Fill up all items"
            notice = pre_set.label2(tk, lbl_txt, "red")
            notice.place(x = 110, y = 16)
            return

    temp_question = q_maker.Question(arr[0], arr[1:], ans)
    quiz.append(temp_question)
    
    lbl_txt = "* Question addded"
    notice = pre_set.label2(tk, lbl_txt, "green")
    notice.place(x = 110, y = 16)

def add_question():
    clear_screen()
    txt_width = 42
    txt_height = 2

    correct_opt = StringVar()
    correct_opt.set('a')
    cor_opt_txt = "Correct\nOption"
    opts = ['a', 'b', 'c', 'd']
    label_texts = [
        "Question", "Option A", "Option B", "Option C",
        "Option D"
    ]

    cor_opt = pre_set.label2(tk, cor_opt_txt)
    labels = [pre_set.label1(tk, txt) for txt in label_texts]
    texts = [pre_set.text1(tk, txt_width, txt_height) for i in label_texts]

    reset = pre_set.button3(tk, "Clear", lambda: new_quiz())
    done = pre_set.button3(tk, "Back", window_menu)
    confirm = pre_set.button3(
        tk, "Add", lambda: add_question(
            [text.get("1.0", "end-1c") for text in texts],
            correct_opt.get()
        )    
    )

    for idx, label in enumerate(labels):
        label.place(x = 5, y = 10 + idx * 70)
    for idx, text in enumerate(texts):
        text.place(x = 5, y = 40 + idx * 70)

    cor_opt.place(x = 326, y = 40)
    confirm.place(x = 265, y = 365, width = 130)
    reset.place(x = 135, y = 365, width = 130)
    done.place(x = 5, y = 365, width = 130)

    for i, opt in enumerate(opts):
        rb = pre_set.radbut1(tk, correct_opt, opt)
        rb.place(x = 340, y = 115 + i * 70)

def make_file_path():
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

def get_file_path():
    file_path = filedialog.askopenfilename(
        title = "Select a file",
        filetypes = [("Text Files", "*.txt")]
    )
    
    if file_path:
        quiz.file_path = file_path
        return True
    return False
    
def edit_quiz():
    if get_file_path():
        add_question()

def study_quiz():
    pass

def window_menu():
    clear_screen()
    title = Label(
        tk, text = "QUIZ MAKER",
        font = ("Arial", 40, "bold"),
        bg = pre_set.bg_color, fg = pre_set.txt_color
    )

    new_txt = "Create New Quiz"
    new_quiz_btn = pre_set.button2(tk, new_txt, make_file_path)

    edit_txt = "Add to Existing Quiz"
    edit_quiz_btn = pre_set.button2(tk, edit_txt, edit_quiz) 

    study_txt = "Answer Quiz"
    study_quiz_btn = pre_set.button2(tk, study_txt, study_quiz)

    title.place(relx = 0.5, rely = 0.3, anchor = "center")
    new_quiz_btn.place(relx = 0.5, rely = 0.5, anchor = "center")
    edit_quiz_btn.place(relx = 0.5, rely = 0.65, anchor = "center")
    study_quiz_btn.place(relx = 0.5, rely = 0.8, anchor = "center")

if __name__ == "__main__":
    tk.title("Python Quiz Maker")
    tk.geometry("400x400")
    tk.configure(bg = pre_set.bg_color) 

    window_menu()

    tk.mainloop()


    
