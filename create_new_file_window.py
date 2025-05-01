from base_file import *
import add_questions_window as aq
import os
        
class New_File(Window):
    def display(self):
        inp_file = pre_set.entry1(self, 28)
        
        conf_txt = "Confirm"
        confirm = pre_set.button3(
            self, conf_txt, lambda: self.check_file_dir(inp_file.get())
        )

        confirm.configure(width = 10)
        
        inp_file.place(x = 26, y = 30)
        confirm.place(x = 85, y = 60)

        print("CREATE")

    def check_file_dir(self, file_path):
        def get_master_window():
            #SELF -> CREATE_NEW_FILE_WINDOW
            #SELF.PARENT -> SUB_SCREEN MADE
            #SELF.PARENT.PARENT -> MAIN_WINDOW
            #SELF.PARENT.PARENT.PARENT -> QUIZ_MAKER
            return self.parent.parent.parent
        
        def draw_notice_lbl(text):
            notice = pre_set.label2(self, text, "red")
            notice.configure(width = 20, anchor = "w")
            notice.place(x = 26, y = 8)
        
        if file_path == "":
            draw_notice_lbl("* Invalid file name")
            return
        elif not file_path.endswith(".txt"):
            file_path += ".txt"

        if os.path.exists(file_path):
            draw_notice_lbl("* File already exists")
        else:
            get_master_window().windows[aq.Add_Questions].set_file_path(file_path)
            get_master_window().parent.set_window(aq.Add_Questions)
            self.parent.destroy()

