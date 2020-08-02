import pandas as pd
import pandas_datareader.data as web
from stockstats import StockDataFrame as Sdf
from yahoo_fin import stock_info as si
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
        return self.stock_dat['rsi_14'].iloc[-1]

    def get_price(self):
        return si.get_live_price(self.stock)
if __name__ == "__main__":
    stck = input("What Stock are you interested in?")
    fetched_dat = FetchData(stck)
    print(fetched_dat.get_macd())
