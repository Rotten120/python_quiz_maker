from base_file import *
import create_new_file_window as new_file

def window(tk):
    clear_screen(tk)
    title = Label(
        tk, text = "QUIZ MAKER",
        font = ("Arial", 40, "bold"),
        bg = pre_set.bg_color, fg = pre_set.txt_color
    )

    new_txt = "Create New Quiz"
    edit_txt = "Add to Existing Quiz"
    study_txt = "Answer Quiz"
    
    new_quiz_btn = pre_set.button2(tk, new_txt, lambda: new_file.window(tk))
    edit_quiz_btn = pre_set.button2(tk, edit_txt, lambda: new_file.window(tk)) 
    study_quiz_btn = pre_set.button2(tk, study_txt, lambda: new_file.window(tk))

    title.place(relx = 0.5, rely = 0.3, anchor = "center")
    new_quiz_btn.place(relx = 0.5, rely = 0.5, anchor = "center")
    edit_quiz_btn.place(relx = 0.5, rely = 0.65, anchor = "center")
    study_quiz_btn.place(relx = 0.5, rely = 0.8, anchor = "center")
    
