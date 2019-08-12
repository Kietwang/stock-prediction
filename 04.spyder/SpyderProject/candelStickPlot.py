# -*- coding: utf-8 -*-

import pandas
import matplotlib
import mpl_finance
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
matplotlib.pyplot.style.use('ggplot')

def stockPricePloat(ticker):
    # step 1. load Data
    history = pandas.read_csv('../../02Data/01.IntradayCN/'+ticker+'.csv',parse_dates=True,index_col=0)

    # step 2. Data Manipulation
    close = history['close']
    # print(close.head())CN
    close = close.reset_index()
    # print(close.head())
    close['timestamp'] = close['timestamp'].map(matplotlib.dates.date2num)

    ohlc = history[['open','high','low','close']].resample('1H').ohlc()
    ohlc = ohlc.reset_index()
    ohlc['timestamp'] = ohlc['timestamp'].map(matplotlib.dates.date2num)

    # step 3. Plot Figures.subplot 1:scatter plot.Subplot. Subplot 2: candle stick piot
    # step 3.1 subplot 1:scatter plot
    subplot1 = plt.subplot2grid((2,1),(0,0),rowspan=1,colspan=1)
    subplot1.xaxis_date()
    subplot1.plot(close['timestamp'],close['close'],'b.')
    plt.title(ticker)

    # step 3.2 subpolt 2.candle stick plot
    subplot2 = plt.subplot2grid((2,1),(1,0),rowspan=1,colspan=1,sharex=subplot1)
    mpl_finance.candlestick_ohlc(ax=subplot2,quotes=ohlc.values,width=0.01)

    plt.show()
stockPricePloat('000713')


