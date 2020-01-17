import MetaTrader5 as mt
from MetaTrader5 import *
from datetime import datetime

def MT5Import(date1, date2, currency, tick):
   MT5Initialize()
   MT5WaitForTerminal()
   frame = timeframe_maping(tick.get())
   eurusd_rates = MT5CopyRatesRange(currency.get(), frame, date1, date2)
   # shut down connection to MetaTrader 5

   MT5Shutdown()
   return eurusd_rates

def timeframe_maping(name):
    choices = {
        'MT5_TIMEFRAME_M1' : MT5_TIMEFRAME_M1, 
        'MT5_TIMEFRAME_M2' : MT5_TIMEFRAME_M2, 
        'MT5_TIMEFRAME_M3' : MT5_TIMEFRAME_M3, 
        'MT5_TIMEFRAME_M4' : MT5_TIMEFRAME_M4, 
        'MT5_TIMEFRAME_M5' : MT5_TIMEFRAME_M5, 
        'MT5_TIMEFRAME_M6' : MT5_TIMEFRAME_M6, 
        'MT5_TIMEFRAME_M10': MT5_TIMEFRAME_M10, 
        'MT5_TIMEFRAME_M12': MT5_TIMEFRAME_M12, 
        'MT5_TIMEFRAME_M15': MT5_TIMEFRAME_M15, 
        'MT5_TIMEFRAME_M20': MT5_TIMEFRAME_M20, 
        'MT5_TIMEFRAME_M30': MT5_TIMEFRAME_M30, 
        'MT5_TIMEFRAME_H1' : MT5_TIMEFRAME_H1,
        'MT5_TIMEFRAME_H2' : MT5_TIMEFRAME_H2, 
        'MT5_TIMEFRAME_H3' : MT5_TIMEFRAME_H3, 
        'MT5_TIMEFRAME_H4' : MT5_TIMEFRAME_H4, 
        'MT5_TIMEFRAME_H6' : MT5_TIMEFRAME_H6, 
        'MT5_TIMEFRAME_H8' : MT5_TIMEFRAME_H8, 
        'MT5_TIMEFRAME_H12': MT5_TIMEFRAME_H12, 
        'MT5_TIMEFRAME_D1' : MT5_TIMEFRAME_D1, 
        'MT5_TIMEFRAME_W1' : MT5_TIMEFRAME_W1, 
        'MT5_TIMEFRAME_MON1' : MT5_TIMEFRAME_MON1
        }
    return choices.get(name, 'SHIT')