import os
import sys
from random import random

from ipycanvas import Canvas, hold_canvas
import ipywidgets as widgets 

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from colorways import *


class TheoryPaletteDemo:
    def __init__(self, w=720, h=200):
        self.width = w
        self.height = h
        self.canvas = Canvas(width=w, height=h)

        self.n = widgets.IntSlider(description="Colors", value=7, min=1, max=360, orientation='vertical')
        self.n.observe(lambda _: self.draw(), 'value')

        self.sat = widgets.FloatSlider(description="Sat:", value=0.2, min=0.0, max=1.0, step=1/256, orientation='vertical')
        self.sat.observe(lambda _: self.draw(), 'value')

        self.lum = widgets.FloatSlider(description="Lum:", value=0.56, min=0.0, max=1.0, step=1/256, orientation='vertical')
        self.lum.observe(lambda _: self.draw(), 'value')

        self.satr = widgets.FloatSlider(description="Sat Range:", value=0.52, min=0.0, max=1.0, step=1/256, orientation='vertical')
        self.satr.observe(lambda _: self.draw(), 'value')

        self.lumr = widgets.FloatSlider(description="Lum Range:", value=0.5, min=0.0, max=1.0, step=1/256, orientation='vertical')
        self.lumr.observe(lambda _: self.draw(), 'value')

        self.ref = widgets.FloatSlider(description="Hue:", value=275, min=0, max=360, step=1, orientation='vertical')
        self.ref.observe(lambda _: self.draw(), 'value')

        self.oa1 = widgets.FloatSlider(description="OA1:", value=160, min=0, max=360, step=1, orientation='vertical')
        self.oa1.observe(lambda _: self.draw(), 'value')

        self.oa2 = widgets.FloatSlider(description="OA2:", value=280, min=0, max=360, step=1, orientation='vertical')
        self.oa2.observe(lambda _: self.draw(), 'value')

        self.ra1 = widgets.FloatSlider(description="RA1:", value=172, min=0, max=360, step=1, orientation='vertical')
        self.ra1.observe(lambda _: self.draw(), 'value')

        self.ra2 = widgets.FloatSlider(description="RA2:", value=294, min=0, max=360, step=1, orientation='vertical')
        self.ra2.observe(lambda _: self.draw(), 'value')

        self.ra3 = widgets.FloatSlider(description="RA3:", value=190, min=0, max=360, step=1, orientation='vertical')
        self.ra3.observe(lambda _: self.draw(), 'value')

        self.randsat = widgets.Checkbox( value=True, description='Random Sat?', disabled=False)

        self.randlum = widgets.Checkbox( value=True, description='Random Lum?', disabled=False)

        self.hbox = widgets.HBox([self.n, self.sat, self.satr, self.lum, self.lumr, 
                      self.ref, self.oa1, self.oa2, self.ra1, self.ra2, self.ra3])

        display(self.randsat, self.randlum)
        display(self.hbox)


    def draw(self):
        self.palette = theory_hsl_palette(
            self.n.value,
            self.oa1.value,
            self.oa2.value,
            self.ra1.value,
            self.ra2.value,
            self.ra3.value,
            self.sat.value,
            self.satr.value, 
            self.lum.value,
            self.lumr.value,
            self.randsat.value,
            self.randlum.value,
            self.ref.value)

        with hold_canvas(self.canvas):
            for i, vec3 in enumerate(self.palette):
                self.canvas.fill_style = hsl2hex(vec3)
                self.canvas.fill_rect(i*self.width//self.n.value, 0, (i+1)*self.width//self.n.value, self.height)          
            self.canvas.stroke_rect(0, 0, self.width, self.height)
        return self.canvas





