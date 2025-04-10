from tkinter import *

bg_color = "#1a1a1a"
title_font = ("Arial", 40, "bold")
subtitle_font = ("Arial", 15, "bold")
small_text_font = ("Arial", 10)
button_font = ("Arial", 15)
dark_color = "#333333"
txt_color = "white"

def button1(tk, txt, cmd):
    return Button(
        tk, text = txt, font = ("Arial", 15, "bold"),
        bg = dark_color, fg = "white",
        command = cmd
    )

def button2(tk, txt, cmd):
    return Button(
        tk, text = txt, font = ("Arial", 15),
        bg = dark_color, fg = "white",
        command = cmd
    )

def button3(tk, txt, cmd):
    return Button(
        tk, text = txt, font = ("Arial", 10),
        bg = dark_color, fg = "white",
        command = cmd
    )
        
def label1(tk, txt, txt_color = "white"):
    return Label(
        tk, text = txt, font = ("Arial", 15, "bold"),
        bg = bg_color, fg = txt_color
    )    
    
def label2(tk, txt, txt_color = "white"):
    return Label(
        tk, text = txt, font = ("Arial", 10),
        bg = bg_color, fg = txt_color
    )
    
def text1(tk, x_size = 1, y_size = 1):
    return Text(
        tk, font = ("Arial", 10),
        width = x_size, height = y_size
    )    

def radbut1(tk, var, val):
    return Radiobutton(
        tk, font = ("Arial", 10), variable = var,
        value = val, bg = bg_color
    )
