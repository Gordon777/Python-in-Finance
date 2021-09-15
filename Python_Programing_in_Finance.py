#import lib
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web

#scrap for data
style.use('ggplot')
start = dt.datetime(2008,1,1)
end = dt.datetime(2021,9,1)
df = web.DataReader('SPY','yahoo',start,end)

#making moving average column
df['50ma'] = df['Adj Close'].rolling(window=50,min_periods=0).mean()
df.dropna(inplace=True)

df_ohlc = df['Adj Close'].resample('5D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

#ohlc
df_ohlc.reset_index(inplace=True)
#date conversion
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

#ploting analysis
ax1 = plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)
ax2 = plt.subplot2grid((6,1),(5,0),rowspan=5,colspan=1,sharex=ax1)
ax1.xaxis_date()
# ax1.plot(df.index, df['Adj Close'])
# ax1.plot(df.index, df['50ma'])
# ax2.bar(df.index, df['Volume'])


#candlestick_plot
candlestick_ohlc(ax1,df_ohlc.values,width=2,colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num),df_volume.values,0)
plt.show()


