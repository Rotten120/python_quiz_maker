from base_file import *
import add_questions_window as aq
import os

class New_File(Window):
    def display(self):
        sub_txt = "Input file name"
        subtitle = pre_set.label1(self, sub_txt)

        inp_file = pre_set.entry1(self, 30)
        
        conf_txt = "Confirm"
        confirm = pre_set.button1(
            self, conf_txt, lambda: self.check_file_dir(inp_file.get())
        )
        
        subtitle.place(relx = 0.2, rely = 0.05, anchor = "center")
        inp_file.place(relx = 0.29, rely = 0.12, anchor = "center")
        confirm.place(relx = 0.88, rely = 0.94, anchor = "center")

        print("CREATE")

    def check_file_dir(self, file_path):
        if file_path == "":
            lbl_txt = "* Invalid file name"
            notice = pre_set.label2(self, lbl_txt, "red")
            notice.place(relx = 0.03, rely = 0.15)
            return
        elif not file_path.endswith(".txt"):
            file_path += ".txt"

        if os.path.exists(file_path):
            lbl_txt = "* File already exists"
            notice = pre_set.label2(self, lbl_txt, "red")
            notice.place(relx = 0.03, rely = 0.15)
        else:
            self.parent.windows[aq.Add_Questions].set_file_path(file_path)
            self.parent.set_window(aq.Add_Questions)

