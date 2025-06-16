from base_file import *
import add_questions_window as aq
import os
        
class NewFile(Window):
    def display(self):
        cls(self)
        
        inp_file = pre_set.entry_text(self, 28)
        
        conf_txt = "Confirm"
        confirm = pre_set.btn_text(
            self, conf_txt, lambda: self.__check_file_dir(inp_file.get())
        )

        confirm.configure(width = 10)
        
        inp_file.place(x = 26, y = 30)
        confirm.place(x = 85, y = 60)

    def __check_file_dir(self, file_path):
        def get_master_window():
            # SELF -> CREATE_NEW_FILE_WINDOW
            # SELF.PARENT -> SUB_SCREEN MADE
            # SELF.PARENT.PARENT -> QUIZ_MAKER
            return self.parent.parent
        
        def draw_notice_lbl(text):
            notice = pre_set.lbl_text(self, text, "red")
            notice.configure(width = 20, anchor = "w")
            notice.place(x = 26, y = 8)
        
        if not file_path.endswith(".qmk"):
            file_path += ".qmk"

        if file_path == ".qmk" or file_path.count('.') != 1:
            draw_notice_lbl("* Invalid file name")
            return

        if os.path.exists(file_path):
            draw_notice_lbl("* File already exists")
        else:
            get_master_window().windows[aq.AddQuestions].set_file_path(file_path)
            get_master_window().set_window(aq.AddQuestions)
            self.parent.destroy()

