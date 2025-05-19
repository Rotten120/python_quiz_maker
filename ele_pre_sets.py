from tkinter import *

bg_color = "#1a1a1a"
title_font = ("Arial", 40, "bold")
subtitle_font = ("Arial", 15, "bold")
small_text_font = ("Arial", 10)
button_font = ("Arial", 15)
dark_color = "#333333"
txt_color = "white"

# -------- BUTTONS -------- #

def btn_title(tk, txt, cmd):
    return Button(
        tk, text = txt, font = ("Arial", 15, "bold"),
        bg = dark_color, fg = "white",
        command = cmd
    )

def btn_subtitle(tk, txt, cmd):
    return Button(
        tk, text = txt, font = ("Arial", 15),
        bg = dark_color, fg = "white",
        command = cmd
    )

def btn_text(tk, txt, cmd):
    return Button(
        tk, text = txt, font = ("Arial", 10),
        bg = dark_color, fg = "white",
        command = cmd
    )

def btn_justified(tk, txt, txt_color = "white", txt_wrap = 295, txt_align = "left"):
    return Button(
        tk, text = txt, font = ("Arial", 10),
        bg = bg_color, fg = txt_color,
        wraplength = txt_wrap, justify = txt_align, anchor = "w"
    )

# -------- LABELS -------- #

def lbl_title(tk, txt, txt_color = "white"):
    return Label(
        tk, text = txt, font = ("Arial", 15, "bold"),
        bg = bg_color, fg = txt_color
    )    
    
def lbl_text(tk, txt, txt_color = "white"):
    return Label(
        tk, text = txt, font = ("Arial", 10),
        bg = bg_color, fg = txt_color
    )

def lbl_justified(tk, txt, txt_color = "white", txt_wrap = 300, txt_align = "left"):
    return Label(
        tk, text = txt, font = ("Arial", 10),
        bg = bg_color, fg = txt_color,
        wraplength = txt_wrap, justify = txt_align
    )

# -------- ENTRIES -------- #

def entry_text(tk, y_size = 1):
    return Entry(
        tk, font = ("Arial", 10), width = y_size,
        bg = dark_color, fg = txt_color
    )

def entry_title(tk, y_size = 1):
    return Entry(
        tk, font = ("Arial", 15), width = y_size,
        bg = dark_color, fg = txt_color
    )

# -------- TEXTS -------- #

def text(tk, x_size = 1, y_size = 1):
    return Text(
        tk, font = ("Arial", 10),
        width = x_size, height = y_size
    )    

# -------- RADIO BUTTONS -------- #

def radbut(tk, var, val):
    return Radiobutton(
        tk, font = ("Arial", 10), variable = var,
        value = val, bg = bg_color
    )
