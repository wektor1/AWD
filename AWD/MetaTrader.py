import MetaTrader5 as mt
from MetaTrader5 import *
from datetime import datetime

def MT5Import():
   MT5Initialize()
   MT5WaitForTerminal()
   eurusd_rates = MT5CopyRatesRange("EURUSD", MT5_TIMEFRAME_M10, datetime(2019,11,29,13), datetime(2019,11,29,20))
   # shut down connection to MetaTrader 5

   MT5Shutdown()
   return eurusd_rates