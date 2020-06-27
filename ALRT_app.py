from data_fetch import FetchData as fd
import kivy
stock = input("what stock?")
fetched_dat = fd(stock)
print(fetched_dat.get_macd())