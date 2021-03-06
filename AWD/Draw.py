from tkinter import *
import tkinter as ttk
from tkinter import StringVar
from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style
from tkcalendar import Calendar, DateEntry
from Invest_win import Invest_win
#from Param_win import Param_win
import AWD as awd
import datetime



signal_span=9
slow_span=26
fast_span =12
    
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


class Example(Frame):

    def __init__(self):
        super().__init__()
        global investing_data, signal_span, slow_span, fast_span
        signal_span=9
        slow_span=26
        fast_span =12
        investing_data = []
        self.initUI()
        
       

    def initUI(self):

        self.master.title("Asystent wspomagania decyzji maklerskich")
        self.pack(fill=BOTH, expand=True)
        

        '''frame dropdown z wyboerwm kursu'''
        frame1 = Frame(self)
        frame1.pack(fill=X)
        lbl1 = Label(frame1, text="Course type", width=15)
        lbl1.pack(side=LEFT, padx=5, pady=5)
        global entry1
        self.tkvar = StringVar()
        choices_course = {'EURUSD', 'USDCHF', 'GBPUSD', 'USDJPY'}
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

        lbl4 = Label(self.frame4, text="Results", width=15)
        lbl4.pack(side=LEFT, anchor=N, padx=5, pady=5)

        self.sugest = Text(self.frame4, height = 2, width = 25)
        self.sugest.pack(side=TOP, fill=X, anchor=N, padx=5, pady=5)

        self.df = Frame(self.frame4, height=40)
        self.df.pack(fill=BOTH, pady=5, padx=5, expand=True)
        #awd.output(df)

        '''frame z przyciskiem predykcji'''
        frame5 = Frame(self)
        frame5.pack(fill=X)
        closeButton5 = Button(frame5, command=self.accept, text="Analyze")
        closeButton5.pack(side=LEFT, padx=5, pady=5)

        closeButton8 = Button(frame5, command= lambda: self.invest(Invest_win), text="Calculate income")
        closeButton8.pack(side=LEFT, padx=5, pady=5)

        closeButton9 = Button(frame5, command= lambda: self.parameters(Param_win), text="MACD parameters")
        closeButton9.pack(side=LEFT, padx=5, pady=5)

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

    def correctness_check(self):
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
                return True
        else:
            '''tutaj co sie dzieje jak jest nie ma wprowadzonej daty'''
            wrong2 = Toplevel(root)
            ttk.Label(wrong2, text='Enter date').pack(padx=10, pady=10)
            closeButton7 = Button(wrong2, command=self.quit4, text="Ok")
            closeButton7.pack(padx=5, pady=5)
        return False

    def accept(self):
        global T, T2, entry1, wrong, wrong2, investing_data
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
                investing_data = awd.output(self.df, d1, d2, self.tkvar2, self.tkvar, self.sugest, signal_span, slow_span, fast_span)
        else:
            '''tutaj co sie dzieje jak jest nie ma wprowadzonej daty'''
            wrong2 = Toplevel(root)
            ttk.Label(wrong2, text='Enter date').pack(padx=10, pady=10)
            closeButton7 = Button(wrong2, command=self.quit4, text="Ok")
            closeButton7.pack(padx=5, pady=5)

    def invest(self, Win_class):
        global investing_data
        if( self.correctness_check):
            global window
            try:
                if window.state() == "normal": window.focus()
            except:
                
                window = ttk.Toplevel(root)
                Win_class(window, investing_data)
                window.mainloop()

    def parameters(self, Win_class):
        global window2
        try:
            
            if window2.state() == "normal": window2.focus()
        except:    
            
            window2 = ttk.Toplevel(root)
            Win_class(window2)
            window2.mainloop()


def main(root):
    app = Example()
    root.mainloop()

if __name__ == '__main__':
    root = ttk.Tk()
    root.title("Tk example")
    root.state('zoomed')
    s = Style(root)
    s.theme_use('clam')
    main(root)

