from tkinter import *
import tkinter as ttk
from tkinter import StringVar
from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style
from tkcalendar import Calendar, DateEntry
import AWD as awd
import datetime




class Example(Frame):
    
    

    def __init__(self):
        super().__init__()

        self.initUI()
       

    def initUI(self):

        self.master.title("Asystent wspomagania decyzji maklerskich")
        self.pack(fill=BOTH, expand=True)

        '''frame dropdown z wyboerwm kursu'''
        frame1 = Frame(self)
        frame1.pack(fill=X)
        lbl1 = Label(frame1, text="Rodzaj kursu", width=15)
        lbl1.pack(side=LEFT, padx=5, pady=5)
        global entry1
        self.tkvar = StringVar()
        choices_course = {'EURUSD', 'USDCHF'}
        self.tkvar.set('EURUSD')  # set the default option
        entry1 = OptionMenu(frame1, self.tkvar, *choices_course)
        entry1.pack(fill=X, padx=5, expand=True)

        '''frame z wyborem ticku danych'''
        global T3
        frame_tick = Frame(self)
        frame_tick.pack(fill=X)
        lbl_kw = Label(frame_tick, text="Tick value", width=15)
        lbl_kw.pack(side=LEFT, padx=5, pady=5)
        global entry2
        self.tkvar2 = StringVar()
        choices_tick = {'MT5_TIMEFRAME_M1', 'MT5_TIMEFRAME_M2', 'MT5_TIMEFRAME_M3', 
                        'MT5_TIMEFRAME_M4', 'MT5_TIMEFRAME_M5', 'MT5_TIMEFRAME_M6', 
                        'MT5_TIMEFRAME_M10', 'MT5_TIMEFRAME_M12', 'MT5_TIMEFRAME_M15', 
                        'MT5_TIMEFRAME_M20', 'MT5_TIMEFRAME_M30', 'MT5_TIMEFRAME_H1',
                        'MT5_TIMEFRAME_H2', 'MT5_TIMEFRAME_H3', 'MT5_TIMEFRAME_H4', 
                        'MT5_TIMEFRAME_H6', 'MT5_TIMEFRAME_H8', 'MT5_TIMEFRAME_H12', 
                        'MT5_TIMEFRAME_D1', 'MT5_TIMEFRAME_W1', 'MT5_TIMEFRAME_MON1'}
        self.tkvar2.set('MT5_TIMEFRAME_M10')  # set the default option
        entry2 = OptionMenu(frame_tick, self.tkvar2, *choices_tick)
        entry2.pack(fill=X, padx=5, expand=True)

        '''frame z data poczatkowa'''
        frame2 = Frame(self)
        frame2.pack(fill=X)
        lbl2 = Label(frame2, text="Choose start date", width=15)
        lbl2.pack(side=LEFT, padx=5, pady=5)
        global T
        closeButton = Button(frame2,command=self.example1, text="Calendar")
        closeButton.pack(side=LEFT, padx=5, pady=5)

        T = Text(frame2, height=1)
        T.pack(fill=X, padx=5, pady=5)
        T.insert(END, "")

        '''frame z data koncowa'''
        frame3 = Frame(self)
        frame3.pack(fill=X)
        lbl3 = Label(frame3, text="Choose end date", width=15)
        lbl3.pack(side=LEFT, padx=5, pady=5)
        global T2
        closeButton2 = Button(frame3, command=self.example2, text="Calendar")
        closeButton2.pack(side=LEFT, padx=5, pady=5)

        T2 = Text(frame3, height=1)
        T2.pack(fill=X, padx=5, pady=5)
        T2.insert(END, "")

        '''frame z wynikami'''
        self.frame4 = Frame(self)
        self.frame4.pack(fill=BOTH, expand=True)

        lbl4 = Label(self.frame4, text="Wyniki", width=15)
        lbl4.pack(side=LEFT, anchor=N, padx=5, pady=5)

        self.sugest = Text(self.frame4, height = 2, width = 25)
        self.sugest.pack(side=TOP, fill=X, anchor=N, padx=5, pady=5)

        self.df = Frame(self.frame4, height=40)
        self.df.pack(fill=BOTH, pady=5, padx=5, expand=True)
        #awd.output(df)

        '''frame z przyciskiem predykcji'''
        frame5 = Frame(self)
        frame5.pack(fill=X)
        closeButton5 = Button(frame5, command=self.accept, text="Predict")
        closeButton5.pack(side=LEFT, padx=5, pady=5)


    def example1(self):
        global top
        top = Toplevel(root)
        ttk.Label(top, text='Choose date').pack(padx=10, pady=10)
        global cal1
        cal1 = DateEntry(top, width=12, background='darkblue',foreground='white', borderwidth=2)
        cal1.pack(padx=10, pady=10)
        closeButton3 = Button(top, command=self.quit1, text="Ok")
        closeButton3.pack(padx=5, pady=5)

    def example2(self):
        global top
        top = Toplevel(root)
        ttk.Label(top, text='Choose date').pack(padx=10, pady=10)
        global cal2
        cal2= DateEntry(top, width=12, background='darkblue',foreground='white', borderwidth=2)
        cal2.pack(padx=10, pady=10)
        closeButton4 = Button(top, command=self.quit2, text="Ok")
        closeButton4.pack( padx=5, pady=5)

    def quit1(self):
        global cal1, T, top
        date_1 = cal1.get()
        T.delete('1.0', END)
        T.insert(END, date_1)
        top.destroy()

    def quit2(self):
        global cal2, T2, top
        date_2 = cal2.get()
        T2.delete('1.0', END)
        T2.insert(END, date_2)
        top.destroy()

    def quit3(self):
        global wrong
        wrong.destroy()

    def quit4(self):
        global wrong2
        wrong2.destroy()

    def accept(self):
        global T, T2, entry1, wrong, wrong2
        d1=T.get("1.0",'end-1c')
        d2=T2.get("1.0",'end-1c')
        parsed1 = d1.split('/')
        parsed2 = d2.split('/')
        print(tuple(parsed1))
        print(tuple(parsed2))
        if(d1 != "" and d2 != ""):
            date1 = datetime.datetime(2000+int(parsed1[2]),int(parsed1[0]),int(parsed1[1]))
            date2 = datetime.datetime(2000 + int(parsed2[2]), int(parsed2[0]), int(parsed2[1]))
            if(date1 >= date2):
                '''tutaj co sie dzieje jak jest zla data'''
                wrong = Toplevel(root)
                ttk.Label(wrong, text='Invalid date').pack(padx=10, pady=10)
                closeButton6 = Button(wrong, command=self.quit3, text="Ok")
                closeButton6.pack(padx=5, pady=5)
            else:
                d1=date1
                d2=date2
                self.df.pack_forget()
                self.df.destroy()
                self.df = Frame(self.frame4, height=40)
                self.df.pack(fill=BOTH, pady=5, padx=5, expand=True)
                awd.output(self.df, d1, d2, self.tkvar2, self.tkvar, self.sugest)
        else:
            '''tutaj co sie dzieje jak jest nie ma wprowadzonej daty'''
            wrong2 = Toplevel(root)
            ttk.Label(wrong2, text='Enter date').pack(padx=10, pady=10)
            closeButton7 = Button(wrong2, command=self.quit4, text="Ok")
            closeButton7.pack(padx=5, pady=5)

        






def main(root):
    app = Example()
    root.mainloop()

if __name__ == '__main__':
    root = ttk.Tk()
    root.title("Tk example")
    s = Style(root)
    s.theme_use('clam')
    main(root)

