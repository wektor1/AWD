from tkinter import *
import tkinter as ttk
from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style
import copy



class Param_win:
    def __init__(self, root):
        
        self.root = root
        self.root.geometry("300x130+500+200")
        frame1 = Frame(self.root)
        frame1.pack(fill=X)
        lbl1 = Label(frame1, text="Signal span:", width=20)
        lbl1.pack(side=LEFT, padx=5, pady=5)
        global T9
        T9 = Text(frame1, height=1)
        T9.pack(fill=X, padx=5, pady=5)
        global signal_span, fast_span, slow_span
        T9.insert(END, str(signal_span))

        frame2 = Frame(self.root)
        frame2.pack(fill=X)
        lbl2 = Label(frame2, text="Fast EMA span:", width=20)
        lbl2.pack(side=LEFT, padx=5, pady=5)
        global T10
        T10 = Text(frame2, height=1)
        T10.pack(fill=X, padx=5, pady=5)
        
        T10.insert(END, str(fast_span))

        frame3 = Frame(self.root)
        frame3.pack(fill=X)
        lbl3 = Label(frame3, text="Slow EMA span:", width=20)
        lbl3.pack(side=LEFT, padx=5, pady=5)
        global T11
        T11 = Text(frame3, height=1)
        T11.pack(fill=X, padx=5, pady=5)
        
        T11.insert(END, str(slow_span))

        frame4 = Frame(self.root)
        frame4.pack(fill=X)
        closeButton1 = Button(frame4, command=self.set_span, text="Set values")
        closeButton1.pack(side=LEFT, padx=5, pady=5)

    def set_span(self):
        d1 = T9.get("1.0", 'end-1c')
        if (d1.isdigit() and d1 != ""):
            global signal_span
            signal_span = int(d1)
        d1 = T10.get("1.0", 'end-1c')
        if (d1.isdigit() and d1 != ""): 
            global fast_span
            fast_span= int(d1)
        d1 = T11.get("1.0", 'end-1c')
        if (d1.isdigit() and d1 != ""): 
            global slow_span
            slow_span = int(d1)
        self.root.destroy()