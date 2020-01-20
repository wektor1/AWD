from tkinter import *
import tkinter as ttk
from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style

class Invest_win:
    def __init__(self, root, investing_data):
        global data
        data = investing_data
        self.root = root
        self.root.geometry("300x100+500+200")
        frame1 = Frame(root)
        frame1.pack(fill=X)
        lbl1 = Label(frame1, text="Type investment amount:", width=20)
        lbl1.pack(side=LEFT, padx=5, pady=5)
        global T
        T = Text(frame1, height=1)
        T.pack(fill=X, padx=5, pady=5)
        T.insert(END, "")

        frame2 = Frame(root)
        frame2.pack(fill=X)
        lbl2 = Label(frame2, text="Return of investment:", width=20)
        lbl2.pack(side=LEFT, padx=5, pady=5)
        global T2
        T2 = Text(frame2, height=1)
        T2.configure(state = ttk.DISABLED)
        T2.pack(fill=X, padx=5, pady=5)
        T2.insert(END, "")

        frame3 = Frame(root)
        frame3.pack(fill=X)
        closeButton1 = Button(frame3, command=self.calculate_return, text="Calculate")
        closeButton1.pack(side=LEFT, padx=5, pady=5)


    def calculate_return(self):
        global T1
        d1 =T.get("1.0", 'end-1c')
        if (d1.isdigit() and d1 != ""):
            self.analise_data(float(d1))

    def analise_data(self, d1):
        global data, T2
        my_money = d1
        investment = 0.0
        length = len(data[0])
        for x in data[1]:
            if (x.Buy and (x.X + 1) < length):
                investment = my_money / data[0][x.X + 1]
                my_money = 0.0
            elif(investment != 0.0 and (x.X + 1) < length ):
                my_money = investment * data[0][x.X + 1]
                investment = 0.0
        T2.configure(state = ttk.NORMAL)
        T2.delete('1.0',ttk.END)
        my_money += investment * data[0][length - 1]
        T2.insert(END, str(my_money))
        T2.configure(state = ttk.DISABLED)



