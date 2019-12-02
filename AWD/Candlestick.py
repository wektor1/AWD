from matplotlib import pyplot as plt
import matplotlib
from mpl_finance import candlestick_ohlc
import matplotlib.ticker as mticker

def graph_data_ohlc(rates):
    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1), (0,0))
    closep=[]
    highp=[]
    lowp=[]
    openp=[]
    for val in rates:
        closep.append(val[1])
        highp.append(val[2])
        lowp.append(val[3])
        openp.append(val[4])
    
    #closep=dataset[:,[3]]
    #highp=dataset[:,[1]]
    #lowp=dataset[:,[2]]
    #openp=dataset[:,[0]]
    date=range(len(closep))
    
    x = 0
    y = len(date)
    ohlc = []
    while x < y:
        append_me = date[x], openp[x], highp[x], lowp[x], closep[x]
        ohlc.append(append_me)
        x+=1
    candlestick_ohlc(ax1, ohlc, width=0.4, colorup='#77d879', colordown='#db3f3f')
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax1.grid(True)
    plt.xlabel('Candle')
    plt.ylabel('Price')
    plt.title('Candlestick sample representation')
    
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
    return plt
