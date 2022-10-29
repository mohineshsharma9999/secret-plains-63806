from pandas_datareader import data as pdr
import yfinance as yf
import pandas as pd 

yf.pdr_override() # <== that's all it takes :-)

def getAllCompany():
    tickers = pd.read_html('https://ournifty.com/stock-list-in-nse-fo-futures-and-options.html#:~:text=NSE%20F%26O%20Stock%20List%3A%20%20%20%20SL,%20%201000%20%2052%20more%20rows%20')[0]
    return tickers.to_dict()