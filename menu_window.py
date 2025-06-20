from base_file import *
from tkinter import filedialog
import create_new_file_window as nf
import add_questions_window as aq
import study_window as st

class Menu(Window):
    def display(self):
        cls(self)
        
        title = Label(
            self, text = "QUIZ MAKER",
            font = ("Arial", 40, "bold"),
            bg = pre_set.bg_color, fg = pre_set.txt_color
        )

        new_txt = "Create New Quiz"
        edit_txt = "Add to Existing Quiz"
        study_txt = "Answer Quiz"
        
        new_quiz_btn = pre_set.btn_subtitle(self, new_txt, lambda: self.__create_new_path())
        edit_quiz_btn = pre_set.btn_subtitle(self, edit_txt, lambda: self.__edit_file_path()) 
        study_quiz_btn = pre_set.btn_subtitle(self, study_txt, lambda: self.__study_file_path())

        title.place(relx = 0.5, rely = 0.3, anchor = "center")
        new_quiz_btn.place(relx = 0.5, rely = 0.5, anchor = "center")
        edit_quiz_btn.place(relx = 0.5, rely = 0.65, anchor = "center")
        study_quiz_btn.place(relx = 0.5, rely = 0.8, anchor = "center")

    def __create_new_path(self):
        size = "250x100"
        x_pos = str(self.get_parent().winfo_x() + (400 - 250) // 2)
        y_pos = str(self.get_parent().winfo_y() + (400 - 100) // 2)
        pos = x_pos + "+" + y_pos
        screen = SubScreen(self.get_parent(), "New file name", size, pos)
        screen.add_window(nf.NewFile, pre_set.bg_color)
        screen.grab_set()
        screen.focus_set()
        screen.set_window(nf.NewFile)

    def __get_file_path(self, prompt = "Select a file"):
        file_path = filedialog.askopenfilename(
            title = prompt,
            filetypes = [("Quiz Questions", "*.qmk")]
        )

        return file_path

    def __edit_file_path(self):
        file = self.__get_file_path("Select a file to edit")
        if file:
            self.get_parent().windows[aq.AddQuestions].set_file_path(file)
            self.get_parent().set_window(aq.AddQuestions)

    def __study_file_path(self):
        file = self.__get_file_path("Select a file to study")
        if file:
            self.get_parent().windows[st.Study].set_file_path(file)
            self.get_parent().set_window(st.Study)
            
    
    
