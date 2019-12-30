#!/usr/bin/python3
__version__ = "1.1"
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.graphics import *
import numpy as np
from kivy.garden.graph import Graph, MeshLinePlot
from multiprocessing import Process
import time
import json
import requests

class MyGrid(Widget):
    url = 'https://jarvis-uwuyuv.firebaseio.com/.json'
    auth_key = 'RWnwRYHiAwVpBBkFicTdqXsUnnvnz8PyXcSJj7JP'

    hodnoty = [21,22.5,23.22,24,23,20,18,25,24]

    def get(self, *args):
        request = requests.get(self.url + '?auth=' + self.auth_key)
        json_data = request.json()
        data = json_data['sensors']
        self.temp.text = str(data['temperature'])
        self.hum.text = str(data['humidity'])
        self.co2.text = str(data['CO2'])
        self.illu.text = str(data['illuminance'])
        self.draw_temp_graph()
        self.draw_hum_graph()
        self.draw_co2_graph()
        

    def clear(self):
        self.temp.text = "NAN"
        self.hum.text = "NAN"
        self.co2.text = "NAN"
        self.illu.text = "NAN"

    def draw_temp_graph(self):
        for plot in self.temp_graph.plots:
            self.temp_graph.remove_plot(plot)
        plot = MeshLinePlot(mode='line_strip', color=[1, 0, 0, 1])
        plot.points = [(x, self.hodnoty[x]) for x in range(-0, len(self.hodnoty))]
        self.temp_graph.add_plot(plot)
        self.temp_graph.x_ticks_major=1
        self.temp_graph.y_ticks_major=1
        self.temp_graph.xmin=-0
        self.temp_graph.xmax=10
        self.temp_graph.ymin=-30
        self.temp_graph.ymax=30
        self.temp_graph.xlabel='Time'
        self.temp_graph.ylabel='Temperature'

    def draw_hum_graph(self):
        for plot in self.hum_graph.plots:
            self.hum_graph.remove_plot(plot)
        plot = MeshLinePlot(mode='line_strip', color=[1, 0, 0, 1])
        plot.points = [(x, self.hodnoty[x]) for x in range(-0, len(self.hodnoty))]
        self.hum_graph.add_plot(plot)
        self.hum_graph.x_ticks_major=1
        self.hum_graph.y_ticks_major=1
        self.hum_graph.xmin=-0
        self.hum_graph.xmax=10
        self.hum_graph.ymin=-30
        self.hum_graph.ymax=30
        self.hum_graph.xlabel='Time'
        self.hum_graph.ylabel='Humidity'

    def draw_co2_graph(self):
        for plot in self.co2_graph.plots:
            self.co2_graph.remove_plot(plot)
        plot = MeshLinePlot(mode='line_strip', color=[1, 0, 0, 1])
        plot.points = [(x, self.hodnoty[x]) for x in range(-0, len(self.hodnoty))]
        self.co2_graph.add_plot(plot)
        self.co2_graph.x_ticks_major=1
        self.co2_graph.y_ticks_major=1
        self.co2_graph.xmin=-0
        self.co2_graph.xmax=10
        self.co2_graph.ymin=-30
        self.co2_graph.ymax=30
        self.co2_graph.xlabel='Time'
        self.co2_graph.ylabel='CO2'

class MyApp(App):
    def build(self):
        grid = MyGrid()
        Clock.schedule_interval(grid.get, 1)
        return grid

if __name__ == '__main__':
    MyApp().run()