

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty

kv = '''
#:import Label kivy.uix.label.Label
<NewGameScreen>:
    name: 'newgame'
    sliders: sliders
    BoxLayout:
        orientation: 'vertical'

        Slider:
            id: sliders
            min: 1
            max: 16
            step: 1
            value: 1
            on_value: root.update_buttons()

        Button:
            text: 'Options'
            on_press: 
                root.manager.transition.direction = 'left'
                root.manager.current = 'options'

<OptionScreen>:
    layout: layout
    name: 'options'
    BoxLayout:
        Button:
            text: 'Go back'
            on_press: 
                root.manager.transition.direction = 'right'
                root.manager.current = 'newgame'
        BoxLayout:
            orientation: 'vertical'
            id:layout
            Button:
                text: "1"

'''
Builder.load_string(kv)

class NewGameScreen(Screen):
    sliders = ObjectProperty(None)
    def update_buttons(self, *args):
        layout = self.manager.get_screen('options').layout
        layout.clear_widgets()
        for i in range(int(self.sliders.value)):
            layout.add_widget(Button(text=str(i+1)))


class OptionScreen(Screen):
    layout = ObjectProperty(None)


class TestApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(NewGameScreen())
        sm.add_widget(OptionScreen())
        return sm

if __name__ == '__main__':
    TestApp().run()