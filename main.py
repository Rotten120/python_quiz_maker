from base_file import *
import menu_window as mn
import create_new_file_window as nf
import add_questions_window as aq

if __name__ == "__main__":
    quiz_maker = Quiz_Maker(
        "Python Quiz Maker",
        "400x400"
    )
    
    windows = [
        #list all windows to use in here
        #first window must be the 'main menu'
        mn.Menu,
        nf.New_File,
        aq.Add_Questions
    ]

    for window in windows:
        quiz_maker.add_window(window, pre_set.bg_color)
    
    quiz_maker.set_window(windows[0])    
    quiz_maker.mainloop()

    print("MAIN")
