# GUI z wykresami

import tkinter
import pandas as pd
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from MetaTrader import MT5Import
from Candlestick import graph_data_ohlc


import numpy as np

class My_point:
    def __init__(self,X,Y,Buy):
        self.X=X
        self.Y=Y
        self.Buy=Buy

root=tkinter.Tk()
root.wm_title("AWD")

fig=Figure(figsize=(5,4),dpi=100)

t=np.arange(0,500, 1)

#wykres kursu
plt1=fig.add_subplot(111)
plt1.plot(t, np.sin(t/50)) #później może Ticker zamiast plot
#wykres sygnalu, macd i histogram
fig1=Figure(figsize=(5,4),dpi=100)
plt=fig1.add_subplot(111)
sig=0.7*np.sin(2*np.pi*t/120) #tymczasowe funkcje
macd=0.6*np.cos(3*np.pi*t/100) #tymczasowe funkcje
values=[]
points=[]
for i in range(0,t.size,1):
    values.append(macd[i]-sig[i])
    if i>0:
        if (values[i]>=0 and values[i-1]<0):
            points.append(My_point(t[i],macd[i],True))
        elif (values[i-1]>=0 and values[i]<0):
            points.append(My_point(t[i],macd[i],False))

plt.plot(t,sig,'b.')
plt.plot(t,macd,'y')
plt.step(t,values)
plt.axhline()


#Punkty kup/sprzedaj
for i in range(0,len(points),1):
    if points[i].Buy == True:
        plt.plot(points[i].X, points[i].Y, 'go')
    if points[i].Buy == False:
        plt.plot(points[i].X, points[i].Y, 'ro')


#Reszta z tworzenia GUI
canvas = FigureCanvasTkAgg(fig, master = root) #A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

canvas = FigureCanvasTkAgg(fig1, master = root) #A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand =1)

def on_key(event):
    print("You pressed {}".format(event.key))
    key_pres_handler(event,canvas,toolbar)

canvas.mpl_connect("key_press_event",on_key)

def quit():
    root.quit()
    root.destroy()

    button =tkinter.Button(master=root, text="Quit",command=quit)
    button.pack(side=tkinter.BOTTOM)

tkinter.mainloop()


