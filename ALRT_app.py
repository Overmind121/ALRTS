import kivy
from kivymd.uix.screen import Screen
from kivymd.app import MDApp
from data_fetch import FetchData as fd
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder

from kivy.app import App
from kivy.uix.label import Label

from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from plyer import notification as note
class HomeScreen(Screen):
    pass


class CreateScreen(Screen):
    def transfer_name(self):
        self.manager.get_screen("info_screen").stock_name = (self.manager.get_screen("create_screen").ids.stock_request.text).upper()


class InfoScreen(Screen):
    stock_name = StringProperty("None")
    MACD_num = StringProperty("None")
    RSI_num = StringProperty("None")
    PRICE_num = StringProperty("None")


class AlertScreen(Screen):
    pass

class Manager(ScreenManager):
    pass


class AlertApp(MDApp):
    def build(self):
        self.stock_dat = 0
        self.stock_name = ""
        self.stock_MACD = 0
        self.stock_MACDS = 0
        self.stock_RSI = 0
        self.stock_PRICE = 0
        self.stock_gathered = False
        self.PRICE_alrt = -1
        self.RSI_alrt = -1
        self.MACD_alrt = -1
        self.MACDS_alrt = -1
        self.MACD_notified = False
        self.MACDS_notified = False
        self.RSI_notified = False
        self.PRICE_notified = False

        GUI = Builder.load_file("alrt.kv")
        return GUI

    def on_start(self):
        Clock.schedule_interval(self.gather_macd, 5)
        Clock.schedule_interval(self.gather_rsi, 5)
        Clock.schedule_interval(self.gather_price, 5)

    def change_screen(self, screen_name):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name

    def on_pause(self):
        Clock.schedule_interval(self.gather_macd, 5)
        Clock.schedule_interval(self.gather_rsi, 5)
        Clock.schedule_interval(self.gather_price, 5)


    def gather_stock(self):
        screen_manager = self.root.ids['screen_manager']
        self.stock_name = screen_manager.get_screen("info_screen").stock_name
        self.stock_dat = fd(self.stock_name)
        self.stock_gathered = True
        print(self.stock_name)

    def update_dat(self):
        self.stock_dat = fd(self.stock_name)

    def gather_macd(self, *args):
        screen_manager = self.root.ids['screen_manager']
        MACD_alert = screen_manager.get_screen("alert_screen").ids.MACD_alrt.text
        MACDS_alert = screen_manager.get_screen("alert_screen").ids.MACDS_alrt.text
        try:
            if (self.stock_gathered == True):
                self.update_dat()
                self.stock_MACD = round(self.stock_dat.get_macd(), 2)
                self.stock_MACDS = round(self.stock_dat.get_macd_signal(), 2)
                screen_manager.get_screen("info_screen").MACD_num = "MACD: " + str(self.stock_MACD)+ "\n MACDS: "+str(self.stock_MACDS)
                print(self.stock_MACD)
                print(self.stock_MACDS)
                print(MACD_alert + " alrt")
                try:
                    macd_find = float(MACD_alert)
                    if(macd_find == self.stock_MACD and self.MACD_notified == False):
                        note.notify("ALERT", "MACD WORKS")
                        self.MACD_notified = True

                    elif(macd_find != self.stock_MACD and self.MACD_notified == True):
                        self.MACD_notified = False
                except:
                    print("NO VALUE ENTERED FOR MACD")

                try:
                    macds_find = float(MACDS_alert)
                    if(macds_find == self.stock_MACDS and self.MACDS_notified == False):
                        note.notify("ALERT", "MACD SIGNAL WORKS")
                        self.MACDS_notified = True

                    elif(macds_find != self.stock_MACDS and self.MACDS_notified == True ):
                        self.MACDS_notified = False


                except:
                    print("NO VALUE ENTERED FOR MACD SIGNAL")
            else:
                pass

        except:
            print("ERROR")
            pass

    def gather_rsi(self, *args):
        screen_manager = self.root.ids['screen_manager']
        RSI_alert = screen_manager.get_screen("alert_screen").ids.RSI_alrt.text
        try:
            if (self.stock_gathered == True):
                self.update_dat()
                self.stock_RSI = round(self.stock_dat.get_rsi(),2)
                screen_manager.get_screen("info_screen").RSI_num = str(self.stock_RSI)
                print(self.stock_RSI)
                try:
                    rsi_find = float(RSI_alert)
                    if (rsi_find == self.stock_RSI and self.RSI_notified == False):
                        note.notify("ALERT", "RSI WORKS")
                        self.RSI_notified = True

                    elif (rsi_find != self.stock_RSI and self.RSI_notified == True):
                        self.RSI_notified = False
                except:
                    print("NO VALUE ENTERED FOR RSI")
            else:
                pass
 
        except:
            print("ERROR")
            pass

    def gather_price(self, *args):
        screen_manager = self.root.ids['screen_manager']
        PRICE_alert = screen_manager.get_screen("alert_screen").ids.PRICE_alrt.text
        try:
            if (self.stock_gathered == True):
                self.update_dat()
                self.stock_PRICE = round(self.stock_dat.get_price(),2)
                screen_manager.get_screen("info_screen").PRICE_num = str(self.stock_PRICE)
                print(self.stock_PRICE)
                try:
                    price_find = float(PRICE_alert)
                    if (price_find == self.stock_PRICE and self.PRICE_notified == False):
                        note.notify("ALERT", "PRICE WORKS")
                        self.PRICE_notified = True

                    elif (price_find != self.stock_price and self.PRICE_notified == True):
                        self.PRICE_notified = False
                except:
                    print("NO VALUE ENTERED FOR PRICE")
            else:
                pass

        except:
            print("ERROR")
            pass
if __name__ == "__main__":
    AlertApp().run()
