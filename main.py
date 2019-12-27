#!/usr/bin/python3
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class mygrid(GridLayout):
    def __init__(self, **kwargs):
        super(mygrid,self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Name: "))
        self.name = TextInput(multiline = False)
        self.add_widget(self.name)

class myapp(App):
    def build(self):
        return mygrid()

if __name__ == "__main__":
    myapp().run()
