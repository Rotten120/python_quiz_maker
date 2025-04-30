from base_file import *
import create_new_file_window as nf

class Menu(Window):
    def display(self):
        title = Label(
            self, text = "QUIZ MAKER",
            font = ("Arial", 40, "bold"),
            bg = pre_set.bg_color, fg = pre_set.txt_color
        )

        new_txt = "Create New Quiz"
        edit_txt = "Add to Existing Quiz"
        study_txt = "Answer Quiz"
        
        new_quiz_btn = pre_set.button2(self, new_txt, lambda: self.parent.set_window(nf.New_File))
        edit_quiz_btn = pre_set.button2(self, edit_txt, lambda: self.parent.set_window(Menu)) 
        study_quiz_btn = pre_set.button2(self, study_txt, lambda: self.parent.set_window(Menu))

        title.place(relx = 0.5, rely = 0.3, anchor = "center")
        new_quiz_btn.place(relx = 0.5, rely = 0.5, anchor = "center")
        edit_quiz_btn.place(relx = 0.5, rely = 0.65, anchor = "center")
        study_quiz_btn.place(relx = 0.5, rely = 0.8, anchor = "center")

        print("MENU")
    
