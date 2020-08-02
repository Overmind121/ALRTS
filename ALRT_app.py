import kivy
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from data_fetch import FetchData as fd
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, NumericProperty, StringProperty

stock_request = ""
stock = fd("AAPL")
focus = False

screen_helper = """
ScreenManager:
    Main:
    Info:
    
<Main>
    name:'main'
    stock_request_obj: stock_request_obj
    MDTextField:
        id: stock_request_obj
        hint_text: "Enter a valid stock"
        mode: "rectangle"
        helper_text: "Ex: AAPL, aapl, AMZN, amzn"
        helper_text_mode: "on_focus"
        pos_hint: {'center_x':0.5,'center_y':0.5}
        size_hint_x: None
        width: 300
        multiline:False
        on_text_validate: root.manager.current = 'info'
        on_text_validate: root.display_stock()
        
<Info>
    name:'info'
    FloatLayout:
        GridLayout:
            rows:1
            pos_hint: {"top": 1, "left":1}
            size_hint: 1, .1
            
            canvas:
                Color:
                    rgba: app.theme_cls.primary_color
                Rectangle:
                    pos: self.pos
                    size: self.size
                
            MDLabel:
                text: "MACD"
                font_size: 50
                font_style: "H6"
                halign: "center"
                
            MDLabel:
                text: root.labelText
                font_size: 50
                font_style: "H6"
                halign: "center"
            
            MDLabel:
                text: "RSI"
                font_size: 50
                font_style: "H6"
                halign: "center"
            
        Live:
           
"""

class Live(Label):
    def __init__(self, **kwargs):
        super(Live, self).__init__(**kwargs)
        self.text = "none"
        Clock.schedule_interval(self.update,1)

    def update(self, *args):
        self.text = str(stock.get_price())

class Main(Screen):
    global stock_request, stock
    stock_request_obj = ObjectProperty(None)

    def display_stock(self):
        stock = fd(str(self.stock_request_obj.text))
        stock_request = str(self.stock_request_obj.text).upper()
        #print("Your stock is " + str(self.stock_request_obj.text))
        self.manager.get_screen('info').labelText = stock_request
        focus = True
        return stock, stock_request

class Info(Screen):
    global stock, stock_request, focus
    labelText = StringProperty('Stock')
    MACD_label = StringProperty('none')
    RSI_label = StringProperty('none')
    Price_label = StringProperty('none')






sm = ScreenManager()
sm.add_widget(Main(name='main'))
sm.add_widget(Info(name='info'))

class ALRTApp(MDApp):
    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen



if __name__ == "__main__":
    ALRTApp().run()
