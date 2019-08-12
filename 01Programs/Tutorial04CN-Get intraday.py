import tushare
import pandas
import datetime
import os
import time


def stockPriceIntraday(ticker,folder):
    # Step 1. get intraday data online
    intraday = tushare.get_hist_data(ticker,ktype='5')

    # Step 2. if the history exists,append
    file = folder+'/'+ticker+'.csv'
    if os.path.exists(file):
        history = pandas.read_csv(file,index_col=0)
        intraday.append(history)


    # Step 3. Inverse based om index
    intraday.sort_index(inplace=True)
    intraday.index.name = 'timestamp'
    # Step 4. save
    intraday.to_csv(file)
    print('Intraday for ['+ticker+']got.')

# step 1. get tickers online
tickersRawData  = tushare.get_stock_basics()
tickers = tickersRawData.index.tolist()
# print(tickersRawData)

# step 2. save the ticker list to a local file
dateToday = datetime.datetime.today().strftime('%Y%m%d')
file = '../02Data/00.TickerListCN/TickerList_'+dateToday+'.csv'
tickersRawData.to_csv(file)
print('Tickers saved')

# step 3. get stock price (intraday) for all
for i,ticker in enumerate(tickers):
    try:
        print('Intraday',i,'/',len(tickers))
        stockPriceIntraday(ticker,folder='../02Data/01.IntradayCN')
    except:
        pass
    # if i>3:
    #     break
print('Intraday for all stocks got.')
