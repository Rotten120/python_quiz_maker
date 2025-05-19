# package of GUI
from tkinter import *

# packages for frames of app
from main_screen import *
from sub_screen import *
from window import *

# packages for pre set elements
import ele_pre_sets as pre_set

def cls(tk):
    for widget in tk.winfo_children():
        widget.destroy()

