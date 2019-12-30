#!/usr/bin/python3
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty
from kivy.graphics import *
import numpy as np
from kivy.garden.graph import Graph, MeshLinePlot
from kivy.config import Config
Config.set('graphics', 'width', '990')
Config.set('graphics', 'height', '1100')



class MainLabels(Widget):

    hodnoty = [2,3,4,2,4,3,5,1]

    def plotGraph(self, amplit):
        numAmp = float(amplit)
        self.my_output.text="graph"
        for plot in self.my_graph.plots:
            self.my_graph.remove_plot(plot)
        plot = MeshLinePlot(mode='line_strip', color=[1, 0, 0, 1])
        plot.points = [(x, self.hodnoty[x]) for x in range(-0, 5)]
        self.my_graph.add_plot(plot)
        self.my_graph.x_ticks_major=1
        self.my_graph.y_ticks_major=1
        self.my_graph.xmin=-0
        self.my_graph.xmax=10
        self.my_graph.ymin=-5
        self.my_graph.ymax=5
        self.my_graph.xlabel='X axis'
        self.my_graph.ylabel='Y axis'
class TestApp(App):
    def build(self):
        return MainLabels()
if __name__ == '__main__':
    TestApp().run()