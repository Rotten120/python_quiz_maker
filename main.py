from base_file import *
import menu_window as menu
import create_new_file_window as new_file
import add_questions_window as add_quest

if __name__ == "__main__":
    quiz_maker = Quiz_Maker(
        "Python Quiz Maker",
        "400x400"
    )
    
    windows = (
        #put all windows in here
        #first window must be the 'main menu'
    )

    for window in windows:
        quiz_maker.add_window(window, pre_set.bg_color)
    
    quiz_maker.set_window(windows[0])
    quiz_maker.mainloop()

    print("MAIN")
