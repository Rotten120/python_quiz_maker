from base_file import *
import quiz_maker as q_maker

class Study(Window):
    def __init__(self, master, bg_color = "white"):
        self.quiz = q_maker.Quiz("")
        self.set_file_path("quiz_data.txt")
        super().__init__(master, bg_color)
    
    def display(self):
        def to_nxt_question():
            item = self.quiz.questions[idx]
            quest_txt = str(idx + 1) + ") " + item.question
            quest_lbl.configure(text = quest_txt)
            
            for opt in item.options:
                opts_lbl[opt].configure(text = item.options[opt])

        def update_ans(ans):
            user_ans_idx = user_ans[idx]
            if user_ans_idx != "-":
                opts_lbl[user_ans_idx].configure(bg = pre_set.bg_color)
            opts_lbl[ans].configure(bg = "black")
            user_ans[idx] = ans
            
        # --- initialize the elements --- #
        idx = 0
        user_ans = ["-" for i in range(len(self.quiz.questions))]
        
        quest_lbl = pre_set.label3(self, "")
        opts_lbl = {}
        opt = list(self.quiz.questions[0].options)
        
        for key in opt:
            opts_lbl[key] = pre_set.button4(self, "")
            opts_lbl[key].configure(width = 37)

        #this is out of the loop since when included in the loop
        #it seems all buttons do the same function which is 'update_ans('d')'
        opts_lbl['a'].configure(command = lambda: update_ans('a'))
        opts_lbl['b'].configure(command = lambda: update_ans('b'))
        opts_lbl['c'].configure(command = lambda: update_ans('c'))
        opts_lbl['d'].configure(command = lambda: update_ans('d'))
        
        to_nxt_question()
        # --- initialize the elements --- #

        

        quest_lbl.place(x = 50, y = 20)
        for idx, key in enumerate(opt):
            opts_lbl[key].place(x = 50, y = 120 + idx * 60)
        
        #print(self.quiz.print())

    def set_file_path(self, file_path):
        self.quiz.file_path = file_path
        self.quiz.read_from_file()
    
