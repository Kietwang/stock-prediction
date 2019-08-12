import tushare
import pandas
import datetime

#step 1. get tickers online
tickersRawData  = tushare.get_stock_basics()
tickers = tickersRawData.index.tolist()
# print(tickersRawData)

#step 2. save the ticker list to a local file
dateToday = datetime.datetime.today().strftime('%Y%m%d')
file = '../02Data/00.TickerListCN/TickerList_'+dateToday+'.csv'
tickersRawData.to_csv(file)
print('Tickers saved')
