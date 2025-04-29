from base_file import *
import quiz_maker as q_maker

quiz = q_maker.Quiz("")

def append_question(tk, arr, ans):
    #arr is question, opta, optb, optc, optd respectively
    for inp in (arr + [ans]):
        if inp == "":
            lbl_txt = "* Empty input. Fill up all items"
            notice = pre_set.label2(tk, lbl_txt, "red")
            notice.place(x = 110, y = 16)
            return

    temp_question = q_maker.Question(arr[0], arr[1:], ans)
    quiz.append(temp_question)
    
    lbl_txt = "* Question addded"
    notice = pre_set.label2(tk, lbl_txt, "green")
    notice.place(x = 110, y = 16)

def window(tk, file_path):
    clear_screen(tk)
    quiz.file_path = file_path
    
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

    cor_opt = pre_set.label2(tk, cor_opt_txt)
    labels = [pre_set.label1(tk, txt) for txt in label_texts]
    texts = [pre_set.text1(tk, txt_width, txt_height) for i in label_texts]

    reset = pre_set.button3(tk, "Clear", lambda: window(tk, file_path))
    done = pre_set.button3(tk, "Back", lambda: window(tk, file_path))
    confirm = pre_set.button3(
        tk, "Add", lambda: append_question(
            tk, [text.get("1.0", "end-1c") for text in texts],
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
        rb = pre_set.radbut1(tk, correct_opt, opt)
        rb.place(x = 340, y = 115 + i * 70)

