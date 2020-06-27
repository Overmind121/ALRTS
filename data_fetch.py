from pandas_datareader import data as web
from datetime import date, timedelta
from stockstats import StockDataFrame as Sdf


# while True:
#     dat = web.get_data_yahoo(input)
#
#     stockstats_df = Sdf.retype(dat)
#     macd = stockstats_df['macd']
#     macd_signal = stockstats_df['macds']
#     rsi = stockstats_df['rsi_14']
#
#     print("RSI " + str(rsi.iloc[-1]))
#     print("MACD " + str(macd.iloc[-1]))
#     print("MACD_SIGNAL " + str(macd_signal.iloc[-1]))

class FetchData:

    def __init__(self, stock):
        data = web.get_data_yahoo(stock)
        self.stock = stock
        self.num_days = 0
        self.start_date = 0
        self.end_date = 0
        self.stock_dat = Sdf.retype(data)

    def get_history(self, days):
        self.num_days = days
        self.start_date = (date.today() - timedelta(days=days)).isoformat()
        self.end_date = date.today().isoformat()

    def get_macd(self):
        return self.stock_dat['macd'].iloc[-1]

    def get_macd_signal(self):
        return self.stock_dat['macds'].iloc[-1]

    def get_rsi(self):
        return self.stock_dat['rsi_14'].iloc[-1]

if __name__ == "__main__":
    stck = input("What Stock are you interested in?")
    fetched_dat = FetchData(stck)
    print(fetched_dat.get_macd())
