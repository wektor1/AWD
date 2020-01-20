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
        global T7
        T7 = Text(frame1, height=1)
        T7.pack(fill=X, padx=5, pady=5)
        T7.insert(END, "")

        frame2 = Frame(root)
        frame2.pack(fill=X)
        lbl2 = Label(frame2, text="Return of investment:", width=20)
        lbl2.pack(side=LEFT, padx=5, pady=5)
        global T8
        T8 = Text(frame2, height=1)
        T8.configure(state = ttk.DISABLED)
        T8.pack(fill=X, padx=5, pady=5)
        T8.insert(END, "")

        frame3 = Frame(root)
        frame3.pack(fill=X)
        closeButton1 = Button(frame3, command=self.calculate_return, text="Calculate")
        closeButton1.pack(side=LEFT, padx=5, pady=5)


    def calculate_return(self):
        global T7
        d1 =T7.get("1.0", 'end-1c')
        if (d1.isdigit() and d1 != ""):
            self.analise_data(float(d1))

    def analise_data(self, d1):
        global data, T8
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
        T8.configure(state = ttk.NORMAL)
        T8.delete('1.0',ttk.END)
        my_money += investment * data[0][length - 1]
        T8.insert(END, str(my_money))
        T8.configure(state = ttk.DISABLED)



