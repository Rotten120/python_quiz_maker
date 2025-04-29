from base_file import *
import add_questions_window as add_quest
import os

def check_file_dir(tk, file_path):
    if file_path == "":
        lbl_txt = "* Invalid file name"
        notice = pre_set.label2(tk, lbl_txt, "red")
        notice.place(relx = 0.03, rely = 0.15)
        return
    elif not file_path.endswith(".txt"):
        file_path += ".txt"

    if os.path.exists(file_path):
        lbl_txt = "* File already exists"
        notice = pre_set.label2(tk, lbl_txt, "red")
        notice.place(relx = 0.03, rely = 0.15)
    else:
        add_quest.window(tk, file_path)

def window(tk):
    clear_screen(tk)
    
    sub_txt = "Input file name"
    subtitle = pre_set.label1(tk, sub_txt)

    inp_file = pre_set.entry1(tk, 30)
    
    conf_txt = "Confirm"
    confirm = pre_set.button1(
        tk, conf_txt, lambda: check_file_dir(tk, inp_file.get())
    )    
    
    subtitle.place(relx = 0.2, rely = 0.05, anchor = "center")
    inp_file.place(relx = 0.29, rely = 0.12, anchor = "center")
    confirm.place(relx = 0.88, rely = 0.94, anchor = "center")
