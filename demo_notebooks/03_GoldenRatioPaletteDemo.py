import os
import sys
from random import random

from ipycanvas import Canvas, hold_canvas
import ipywidgets as widgets 

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from colorways import *


class GoldenRatioPaletteDemo:
    def __init__(self, w=720, h=200):
        self.width = w
        self.height = h
        self.canvas = Canvas(width=w, height=h)
        self.palette = None

        self.n = widgets.IntSlider(description="Colors", value=6, min=1, max=250, orientation='horizontal')
        self.n.observe(lambda _: self.draw(), 'value')


        self.sat = widgets.FloatSlider(description="Sat:", value=0.8, min=0.0, max=1.0, step=1/256, orientation='horizontal')
        self.sat.observe(lambda _: self.draw(), 'value')

        self.lum = widgets.FloatSlider(description="Lum:", value=0.7, min=0.0, max=1.0, step=1/256, orientation='horizontal')
        self.lum.observe(lambda _: self.draw(), 'value')

        self.randbut = widgets.Button(
            description='Randomize',
            disabled=False,
            button_style=''
        )

        self.randbut.on_click(lambda _: self.draw())

        self.palette = golden_ratio_hsl_palette(self.n.value, self.sat.value, self.lum.value)
        display(widgets.VBox([self.n, self.sat, self.lum]))
        display(self.randbut)


    def draw(self, new_pal=True):
        n = self.n.value
        sat = self.sat.value
        lum = self.lum.value
        width = self.width
        height = self.height

        if new_pal:
            self.palette = golden_ratio_hsl_palette(n, sat, lum)
        with hold_canvas(self.canvas):
            for i, vec3 in enumerate(self.palette):
                self.canvas.fill_style = hsl2hex(vec3)
                self.canvas.fill_rect(i*width//n, 0, (i+1)*width//n, height)

            self.canvas.stroke_rect(0, 0, width, height)
        return self.canvas


