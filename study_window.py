from base_file import *
import menu_window as mn
import show_score_window as ss
import quiz_maker as q_maker

class Study(Window):
    def __init__(self, master, bg_color = "white"):
        self.idx = 0
        self.user_ans = []
        self.quiz = q_maker.Quiz("")
        super().__init__(master, bg_color)
    
    def display(self):
        cls(self)
        
        def go_to_question(number):
            if number < 0 or number >= len(self.user_ans):
                return
            
            item = self.quiz.questions[number]
            quest_lbl.configure(text = item.question)
            item_ctr.configure(text = str(number + 1) + "/" + str(len(self.user_ans)))
            
            for key in item.options:
                opt_txt = key + ") " + item.options[key]
                opt_btns[key].configure(text = opt_txt)
            if self.user_ans[number] != "":
                opt_btns[self.user_ans[number]].configure(bg = "black")

            update_ans(number, self.user_ans[number])

        def update_ans(number, ans):
            for key in opts:
                opt_btns[key].configure(bg = pre_set.bg_color)
            if ans != "":
                opt_btns[ans].configure(bg = "black")
            self.user_ans[number] = ans

        def increment_idx():
            if self.idx + 1 < len(self.user_ans):
                self.idx += 1
                go_to_question(self.idx)

        def decrement_idx():
            if self.idx > 0:
                self.idx -= 1
                go_to_question(self.idx)
        
        
        # --- initialize the elements --- #
        quest_lbl = pre_set.lbl_justified(self, "")
        opt_btns = {}
        opts = ['a', 'b', 'c', 'd']
        
        for key in opts:
            opt_btns[key] = pre_set.btn_justified(self, "")
            opt_btns[key].configure(width = 37)

        #this is out of the loop since when included in the loop
        #it seems all buttons do the same function which is 'update_ans('d')'
        opt_btns['a'].configure(command = lambda: update_ans(self.idx, 'a'))
        opt_btns['b'].configure(command = lambda: update_ans(self.idx, 'b'))
        opt_btns['c'].configure(command = lambda: update_ans(self.idx, 'c'))
        opt_btns['d'].configure(command = lambda: update_ans(self.idx, 'd'))

        item_ctr = pre_set.lbl_title(self, "")
        next_btn = pre_set.btn_text(self, ">", increment_idx)
        back_btn = pre_set.btn_text(self, "<", decrement_idx)

        to_main_btn = pre_set.btn_text(self, "Back", lambda: self.parent.set_window(mn.Menu))
        submit_btn = pre_set.btn_text(self, "Submit", lambda: self.show_answers())
        
        go_to_question(self.idx)
        # --- initialize the elements --- # 

        quest_lbl.place(x = 50, y = 30)
        item_ctr.place(relx = 0.45, y = 355)
        next_btn.place(x = 255, y = 355, width = 100)
        back_btn.place(x = 50, y = 355, width = 100)
        to_main_btn.place(x = 50, y = 5, width = 150)
        submit_btn.place(x = 200, y = 5, width = 155)
        
        for idx, key in enumerate(opts):
            opt_btns[key].place(x = 50, y = 120 + idx * 60)
        
        #print(self.quiz.print())

    def set_file_path(self, file_path):
        self.idx = 0
        self.quiz = q_maker.Quiz("")
        self.user_ans = []
        
        self.quiz.file_path = file_path
        self.quiz.read_from_file(True)
        self.user_ans = ["" for i in range(len(self.quiz.questions))]

    def check_answers(self):
        score = 0
        for idx in range(len(self.quiz.questions)):
            correct_ans = self.quiz.questions[idx].answer
            if correct_ans == self.user_ans[idx]:
                score += 1
        return score

    def show_answers(self):
        def to_main():
            self.parent.set_window(mn.Menu)
            screen.destroy()
            
        size = "200x200"
        x_pos = str(self.parent.winfo_x() + 100)
        y_pos = str(self.parent.winfo_y() + 100)
        pos = x_pos + "+" + y_pos
        screen = SubScreen(self.parent, "Checking answers...", size, pos)
        screen.add_window(ss.Show_Score, pre_set.bg_color)
        screen.windows[ss.Show_Score].get_score(self.check_answers(), len(self.quiz.questions))
        screen.protocol("WM_DELETE_WINDOW", to_main)
        
        screen.grab_set()
        screen.focus_set()
        screen.set_window(ss.Show_Score)
