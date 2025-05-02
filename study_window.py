from base_file import *
import menu_window as mn
import quiz_maker as q_maker

class Study(Window):
    def __init__(self, master, bg_color = "white"):
        self.idx = 0
        self.user_ans = []
        self.quiz = q_maker.Quiz("")
        super().__init__(master, bg_color)
    
    def display(self):
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
        quest_lbl = pre_set.label3(self, "")
        opt_btns = {}
        opts = ['a', 'b', 'c', 'd']
        
        for key in opts:
            opt_btns[key] = pre_set.button4(self, "")
            opt_btns[key].configure(width = 37)

        #this is out of the loop since when included in the loop
        #it seems all buttons do the same function which is 'update_ans('d')'
        opt_btns['a'].configure(command = lambda: update_ans(self.idx, 'a'))
        opt_btns['b'].configure(command = lambda: update_ans(self.idx, 'b'))
        opt_btns['c'].configure(command = lambda: update_ans(self.idx, 'c'))
        opt_btns['d'].configure(command = lambda: update_ans(self.idx, 'd'))

        item_ctr = pre_set.label1(self, "")
        next_btn = pre_set.button3(self, ">", increment_idx)
        back_btn = pre_set.button3(self, "<", decrement_idx)

        to_main_btn = pre_set.button3(self, "Back", lambda: self.parent.set_window(mn.Menu))
        submit_btn = pre_set.button3(self, "Submit", lambda: print("yeS"))
        
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
        self.quiz = q_maker.Quiz("")
        self.user_ans = []
        
        self.quiz.file_path = file_path
        self.quiz.read_from_file(True)
        self.user_ans = ["" for i in range(len(self.quiz.questions))]
        self.display()
    
