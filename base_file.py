from tkinter import *
import ele_pre_sets as pre_set

def clear_screen(tk):
    for widget in tk.winfo_children():
        widget.destroy()
        
