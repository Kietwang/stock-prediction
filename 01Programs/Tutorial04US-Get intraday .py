import requests
import pandas
import io
import datetime
import os


def dataframeFromUrl(url):
    dataString = requests.get(url).content
    #使用pandas会为我们获取的数据添加索引，我们不行用他的，就可以直接用第一列就好了
    parsedResult = pandas.read_csv(io.StringIO(dataString.decode('utf-8')),index_col=0)
    return parsedResult
def stockPriceIntraday(ticker,folder):
    # step 1.get data online
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}' \
          '&interval=1min&apikey=GS9HGVRWCQ49I7SZ&outputsize=full&datatype=csv'.format(ticker=ticker)
    intraday = dataframeFromUrl(url)

    # step 2.Append if history exists
    file = folder+'/'+ticker+'.csv'
    if os.path.exists(file):
        history =pandas.read_csv(file,index_col=0)
        intraday.append(history)

    # step 3.Inverse based on index
    intraday.sort_index(inplace=True)

    # step 4.save
    intraday.to_csv(file)
    print('Intraday for ['+ticker+']got.')

# step 1.get ticker list online
url = 'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&render=download'
dataString = requests.get(url).content
# print(dataString)
tickersRawdata = pandas.read_csv(io.StringIO(dataString.decode('utf-8')))
tickers = tickersRawdata['Symbol'].tolist()
# print(tickers)

# step 2.save the ticker list to a local file
dateToday = datetime.datetime.today().strftime('%Y%m%d')
file = '../02Data/00.TickerListUS/TickerList_'+dateToday+'.csv'
tickersRawdata.to_csv(file,index=False)
print('tickers saved.')

# step 3.get stock price (intraday) 获取当日股价
for i,ticker in enumerate(tickers):
    try:
         print('Intraday',i,'/',len(tickers))
         stockPriceIntraday(ticker,folder='../02Data/01.IntradayUS')
         time.sleep(60)
    except:
        pass
    if i>10:
        break
print('Intraday for all stocks got.')

