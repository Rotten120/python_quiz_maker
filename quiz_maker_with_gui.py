from tkinter import *
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
        new_quiz()
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
    is_ans_valid = quiz.append(temp_question)
    
    if is_ans_valid:
        lbl_txt = "* Question addded"
        notice = pre_set.label2(tk, lbl_txt, "green")
        notice.place(x = 110, y = 16)
    else:
        lbl_txt = "* Answer option is invalid"
        notice = pre_set.label2(tk, lbl_txt, "red")
        notice.place(x = 110, y = 16)

def new_quiz():
    clear_screen()
    txt_width = 40
    txt_height = 2

    label_texts = [
        "Question", "Option A", "Option B", "Option C",
        "Option D", "Correct Option"
    ]
    
    labels = [pre_set.label1(tk, txt) for txt in label_texts]
    texts = [pre_set.text1(tk, txt_width, txt_height) for i in range(len(label_texts) - 1)]
    ans_text = Entry(tk, width = 1, font = pre_set.subtitle_font)

    reset = pre_set.button2(tk, "  Clear   ", lambda: new_quiz())
    done = pre_set.button2(tk, "   Back   ", window_menu)
    confirm = pre_set.button2(
        tk, "   Add    ", lambda: add_question(
            [text.get("1.0", "end-1c") for text in texts],
            ans_text.get()
        )    
    )

    for idx, label in enumerate(labels):
        label.place(x = 10, y = 10 + idx * 70)
    for idx, text in enumerate(texts):
        text.place(x = 10, y = 40 + idx * 70)
    ans_text.place(x = 160, y = 360)
    
    confirm.place(x = 300, y = 100)
    reset.place(x = 300, y = 200)
    done.place(x = 300, y = 300)

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
    clear_screen()
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


    
