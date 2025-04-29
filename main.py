from tkinter_gui import *
import menu_window as menu

tk = Tk()
width = 400
height = 400
        
if __name__ == "__main__":
    tk.title("Python Quiz Maker")
    tk.geometry(str(width) + "x" + str(height))
    
    tk.configure(bg = pre_set.bg_color)
    menu.window(tk)
    tk.mainloop()
