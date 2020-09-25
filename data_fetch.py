from yahoo_fin import stock_info as si
import pandas as pd
import fix_yahoo_finance 
from pandas_datareader import data as web
from stockstats import StockDataFrame as Sdf

class FetchData:

    def __init__(self, stock):
        if stock == "none":
            data = 0
        else:
            data = web.get_data_yahoo(stock)
            self.stock = stock
            self.stock_dat = Sdf.retype(data)

    def get_macd(self):
        return self.stock_dat['macd'].iloc[-1]

    def get_macd_signal(self):
        return self.stock_dat['macds'].iloc[-1]

    def get_rsi(self):
        return self.stock_dat['rsi_12'].iloc[-1]

    def get_price(self):
        return si.get_live_price(self.stock)
if __name__ == "__main__":
    stck = input("What Stock are you interested in?")

    while True:
        fetched_dat = FetchData(stck)
        before = 0
        if(before != fetched_dat.get_macd()):
            before = fetched_dat.get_macd()
            print(before)
#81.84710003304872
