import os
import sys
from random import random

from ipycanvas import Canvas, hold_canvas
import ipywidgets as widgets 

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from colorways import *


class RandomWalkPaletteDemo:
    def __init__(self, w=720, h=200):
        self.width = w
        self.height = h
        self.canvas = Canvas(width=w, height=h)
        self.palette = None

        self.n = widgets.IntSlider(description="Colors", value=6, min=1, max=250, orientation='horizontal')
        self.n.observe(lambda _: self.draw(), 'value')

        self.mode_options = [ ('HSL', 0), ('HSV', 1), ('RGB', 2)]
        self.mode= widgets.Dropdown( options=self.mode_options, value=0, description='Mode:',)
        self.mode.observe(lambda _: self.draw(), 'value')

        self.base = widgets.ColorPicker(
            concise=False,
            description='Base Color',
            value=rgb2hex(randvec3()),
            disabled=False
        )
        self.base.observe(lambda _: self.draw(), 'value')

        self.reflection = widgets.Checkbox(
            value=True,
            description='Reflect at edges?',
            disabled=False
        )
        self.reflection.observe(lambda _: self.draw(), 'value')

        self.rw_minmax = widgets.FloatRangeSlider(
            value=[0.0, 0.1],
            min=0.0,
            max=1.0,
            step=0.01,
            description='Step Range:',
            disabled=False,
            continuous_update=True,
            orientation='horizontal',
            readout=True,
            readout_format='.2f',
        )
        self.rw_minmax.observe(lambda _: self.draw(), 'value')

        self.randbut = widgets.Button(
            description='Randomize',
            disabled=False,
            button_style=''
        )
        self.randbut.on_click(lambda _: self.draw())

        display(widgets.HBox([self.mode, self.reflection]))
        display(widgets.HBox([self.n, self.rw_minmax, self.base]))
        display(self.randbut)

    def draw(self, new_pal=True):
        n = self.n.value
        mindist = self.rw_minmax.value[0]
        maxdist = self.rw_minmax.value[1]
        mode = self.mode.value
        width = self.width
        height = self.height
        
        base = hex2rgb(self.base.value)
        if mode == 0:
            base = rgb2hsl(base)
        elif mode == 1:
            base = rgb2hsv(base)
        elif mode == 3:
            base = rgb2hwb(base)
        
        if new_pal:
            if self.reflection.value: 
                self.palette = random_walk_reflection_palette(n, base, mindist, maxdist)
            else:
                self.palette = random_walk_palette(n, base, mindist, maxdist)
            
        with hold_canvas(self.canvas):
            for i, vec3 in enumerate(self.palette):
                if mode == 0:
                    self.canvas.fill_style = hsl2hex(vec3)
                elif mode == 1:
                    self.canvas.fill_style = hsv2hex(vec3)
                elif mode == 2:
                    self.canvas.fill_style = rgb2hex(vec3)
                elif mode == 3:
                    self.canvas.fill_style = hwb2hex(vec3)
                
                self.canvas.fill_rect(i*width//n, 0, (i+1)*width//n, height)

            self.canvas.stroke_rect(0, 0, width, height)
        return self.canvas


        

