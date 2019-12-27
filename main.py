#!/usr/bin/python3
__version__ = "1.0"
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
import json
import requests

class MyGrid(Widget):
    data = ObjectProperty(None)

    url = 'https://jarvis-uwuyuv.firebaseio.com/.json'
    auth_key = 'RWnwRYHiAwVpBBkFicTdqXsUnnvnz8PyXcSJj7JP'

    def get(self):
        request = requests.get(self.url + '?auth=' + self.auth_key)
        #json_data = request.json()
        #data = json_data['temp']
        self.data.text = str("baf")

    def clear(self):
        self.data.text = "cleared"

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    MyApp().run()