import requests
import pandas
import io
import datetime

# step 1.get ticker list online
url = 'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDA&render=download'
dataString = requests.get(url).content
print(dataString)
tickersRawdata = pandas.read_csv(io.StringIO(dataString.decode('utf-8')))
tickers = tickersRawdata['Symbol'].tolist()
print(tickers)

# step 2.save the ticker list to a local file
dateToday = datetime.datetime.today().strftime('%Y%m%d')
wfile = '../02Data/00.TickerListUS/TickerList_'+dateToday+'.csv'
tickersRawdata.to_csv(wfile,index=False)
print('tickers saved.')

