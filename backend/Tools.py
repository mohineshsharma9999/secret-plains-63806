from pandas_datareader import data as pdr
import yfinance as yf
import pandas as pd 

yf.pdr_override() # <== that's all it takes :-)

def getAllCompany():
    tickers = pd.read_html('https://ournifty.com/stock-list-in-nse-fo-futures-and-options.html#:~:text=NSE%20F%26O%20Stock%20List%3A%20%20%20%20SL,%20%201000%20%2052%20more%20rows%20')[0]
    return tickers.to_dict()

def getCompanyData(company,start_date,end_date):
    data = pdr.get_data_yahoo(company, start=start_date, end=end_date)
    data.index=data.index.astype(str)
    return data.to_dict()

def getPeriodicCompanyData(company,period,interval):
    data = yf.download(tickers=company, period=period, interval=interval)
    data.index=data.index.astype(str)
    return data.to_dict()