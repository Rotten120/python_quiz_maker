from base_file import *
import menu_window as mn

class ShowScore(Window):
    def __init__(self, master, bg_color = "white"):
        self.score = 0
        self.total = 0
        super().__init__(master, bg_color)
        
    def display(self):
        def to_main():
            self.get_parent().get_parent().set_window(mn.Menu)
            self.get_parent().destroy()
            
        cls(self)

        notice_lbl = pre_set.lbl_title(self, "SCORE:")
        score_lbl = pre_set.lbl_title(self, str(self.score) + " / " + str(self.total))
        back_btn = pre_set.btn_text(self, "To Main", to_main)
        back_btn.configure(width = 20)

        notice_lbl.pack(pady = 28)
        score_lbl.pack()
        back_btn.place(relx = 0.5, y = 180, anchor = "center")

    def get_score(self, score, total):
        self.score = score
        self.total = total

