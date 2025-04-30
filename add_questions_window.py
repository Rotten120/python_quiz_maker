from base_file import *
import menu_window as mn
import quiz_maker as q_maker

class Add_Questions(Window):
    def __init__(self, master, bg_color = "white"):
        super().__init__(master, bg_color)
        self.quiz = q_maker.Quiz("")

    def display(self):
        txt_width = 42
        txt_height = 2

        correct_opt = StringVar()
        correct_opt.set('a')
        cor_opt_txt = "Correct\nOption"
        opts = ['a', 'b', 'c', 'd']
        label_texts = [
            "Question", "Option A", "Option B", "Option C",
            "Option D"
        ]

        cor_opt = pre_set.label2(self, cor_opt_txt)
        labels = [pre_set.label1(self, txt) for txt in label_texts]
        texts = [pre_set.text1(self, txt_width, txt_height) for i in label_texts]

        reset = pre_set.button3(self, "Clear", lambda: self.parent.set_window(mn.Menu))
        done = pre_set.button3(self, "Back", lambda: self.parent.set_window(mn.Menu))
        confirm = pre_set.button3(
            self, "Add", lambda: self.append_question(
                [text.get("1.0", "end-1c") for text in texts],
                correct_opt.get()
            )    
        )

        for idx, label in enumerate(labels):
            label.place(x = 5, y = 10 + idx * 70)
        for idx, text in enumerate(texts):
            text.place(x = 5, y = 40 + idx * 70)

        cor_opt.place(x = 326, y = 40)
        confirm.place(x = 265, y = 365, width = 130)
        reset.place(x = 135, y = 365, width = 130)
        done.place(x = 5, y = 365, width = 130)

        for i, opt in enumerate(opts):
            rb = pre_set.radbut1(self, correct_opt, opt)
            rb.place(x = 340, y = 115 + i * 70)

        print("ADD QUESTION")

    def append_question(self, arr, ans):
        #arr is question, opta, optb, optc, optd respectively
        for inp in (arr + [ans]):
            if inp == "":
                lbl_txt = "* Empty input. Fill up all items"
                notice = pre_set.label2(self, lbl_txt, "red")
                notice.place(x = 110, y = 16)
                return

        temp_question = q_maker.Question(arr[0], arr[1:], ans)
        self.quiz.append(temp_question)
        
        lbl_txt = "* Question addded"
        notice = pre_set.label2(self, lbl_txt, "green")
        notice.place(x = 110, y = 16)

    def set_file_path(self, file_path):
        self.quiz.file_path = file_path

