# GUI z wykresami

import tkinter
import pandas as pd
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from MetaTrader import MT5Import
from Candlestick import graph_data_ohlc
import statistics as st
import datetime as dt
import matplotlib.pyplot as plt2
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import copy

import numpy as np


class My_point:
    def __init__(self,X,Y,Buy):
        self.X=X
        self.Y=Y
        self.Buy=Buy

def output(self, date1, date2, tick, currency, sugestion ):

    root=self

    
    t=np.arange(0,7000, 1)
    
    data = MT5Import(date1, date2, currency, tick)
    closep=[]
    highp=[]
    lowp=[]
    openp=[]
    time=[]
    for val in data:
        time.append(val[0])
        closep.append(val[1])
        highp.append(val[2])
        lowp.append(val[3])
        openp.append(val[4])
    trading_days = (date2.year - date1.year)*365 + (date2.month - date1.month)*30 + (date2.day - date1.day)
    annual_volatility = st.stdev(closep) * np.sqrt(trading_days) * 100
    
    candles=graph_data_ohlc(closep, highp, lowp, openp, time)

    
    cenka = pd.DataFrame(data = closep)
    ema26 = cenka.ewm(span =26).mean() 
    ema12 = cenka.ewm(span = 12).mean()
    macd = []
    for i in range (0,len(ema26)):
        macd.append(ema26.values[i] - ema12.values[i])
    sygnal = pd.DataFrame(data = macd)
    sig = sygnal.ewm(span= 9).mean()
    
    
    values=[]
    points=[]
    tactic = str()
    for i in range(0,len(macd),1):
        values.append(macd[i]-sig.values[i])
        if i>0:
            if (values[i]>=0 and values[i-1]<0):
                points.append(My_point(t[i],macd[i],True))
            elif (values[i-1]>=0 and values[i]<0):
                points.append(My_point(t[i],macd[i],False))
    
    data_to_return = []
    data_to_return.append(closep)
    data_to_return.append(points)

    last_pos = points[len(points)-1]
    if last_pos.Buy == True:
        tactic = "Position: Buy"
    else:
        tactic = "Position: Sell"

    anual_vol = "Annualised Volatility: "+ str(annual_volatility) +"%"
    sugestion.delete('1.0',tkinter.END)
    sugestion.insert(tkinter.INSERT, tactic + "\n" + anual_vol)
    fig1 = plt2.figure(figsize = [5.0, 3.0])
    xax = [1] * len(values)
    for i in range (0,len(values)):
        values[i] = values[i][0]

    ax1 = plt2.subplot2grid((1,1), (0,0))
    ax1.xaxis.set_major_locator(ticker.MaxNLocator(10))
    def mydate(x,pos):
        try:
            return time[int(x)]
        except IndexError:
            return ''
    ax1.xaxis.set_major_formatter(ticker.FuncFormatter(mydate))
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(5)
    ax1.grid(True)

    plt2.plot( sig,'b')
    plt2.plot( macd,'y')

    plt2.title('MACD')
    
    #Punkty kup/sprzedaj
    for i in range(0,len(points),1):
        if points[i].Buy == True:
            plt2.plot(points[i].X, points[i].Y, 'go')
        if points[i].Buy == False:
            plt2.plot(points[i].X, points[i].Y, 'ro')
    
    #Reszta z tworzenia GUI
    canvas = FigureCanvasTkAgg(candles, master = root) #A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    
    canvas = FigureCanvasTkAgg(fig1, master = root) #A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    return data_to_return
    


def ema(close, span_):
    emas = [0] * (len(close)+1)
    weights = [0] * len(close)
    for i in range(0,span_-1):
        weights[i] = span_ - i
    for i in range (1, len(close)):
        emas[i] = (close[len(close)-i] - emas[i-1]) * weights[i-1]* (2/(i+1)) + emas[i-1]
    emas.remove(0)
    return emas



def on_key(event):
    print("You pressed {}".format(event.key))
    key_pres_handler(event,canvas,toolbar)



def quit():
    root.quit()
    root.destroy()

    button =tkinter.Button(master=root, text="Quit",command=quit)
    button.pack(side=tkinter.BOTTOM)


