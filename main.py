from base_file import *
import menu_window as mn
import add_questions_window as aq
import study_window as st

if __name__ == "__main__":
    quiz_maker = MainScreen(
        "Python Quiz Maker",
        "400x400"
    )

    quiz_maker.iconbitmap("icon.ico")
    
    windows = [
        #list all windows to use in here
        #first window must be the 'main menu'
        mn.Menu,
        aq.AddQuestions,
        st.Study
    ]

    for window in windows:
        quiz_maker.add_window(window, pre_set.bg_color)
    
    quiz_maker.set_window(windows[0])    
    quiz_maker.mainloop()
