import os
import sys
from random import random

from ipycanvas import Canvas, hold_canvas
import ipywidgets as widgets 

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from colorways import *


class OffsetPaletteDemo:
    def __init__(self, w=720, h=200):
        self.width = w
        self.height = h
        self.canvas = Canvas(width=w, height=h)

        self.n = widgets.IntSlider(description="Colors", value=6, min=1, max=250, orientation='horizontal')

        self.mode_options = [ ('HSL', 0), ('HSV', 1), ('RGB', 2)]
        self.mode= widgets.Dropdown( options=self.mode_options, value=0, description='Mode:',)

        self.paltype = widgets.Dropdown(
            options=[('Random Offset',0), ('Value Offset', 1)],
            description='Palette Type',
            value=0,
        )

        self.edge_strat = widgets.Dropdown(
            options=[('Clamp', clamp01), ('Reflect', reflect)],
            description='Edge Fn',
            value=clamp01,
        )

        self.base = widgets.ColorPicker(
            concise=False,
            description='Base Color',
            value=rgb2hex(randvec3()),
            disabled=False
        )

        self.rng = widgets.FloatSlider(
            value=0.5,
            min=0.0,
            max=1.0,
            step=0.01,
            description='Range:',
            disabled=False,
            continuous_update=True,
            orientation='horizontal',
            readout=True,
            readout_format='.2f',
        )

        self.randbut = widgets.Button(
            description='Randomize',
            disabled=False,
            button_style=''
        )

        self.randbut.on_click(lambda _: self.draw())
        self.n.observe(lambda _: self.draw(), 'value')
        self.rng.observe(lambda _: self.draw(), 'value')
        self.base.observe(lambda _: self.draw(), 'value')
        self.mode.observe(lambda _: self.draw(), 'value')
        self.edge_strat.observe(lambda _: self.draw(), 'value')
        self.paltype.observe(lambda _: self.draw(), 'value')

        self.palette = None
        display(widgets.HBox([self.mode, self.n, self.paltype]))
        display(widgets.HBox([self.base, self.rng, self.edge_strat]))
        display(self.randbut)

    def draw(self, new_pal=True):
        n = self.n.value
        rng = self.rng.value
        mode = self.mode.value
        edgefn = self.edge_strat.value
        paltype = self.paltype.value
        width = self.width
        height = self.height
 
        base = hex2rgb(self.base.value)

        if mode == 0:
            base = rgb2hsl(base)
        elif mode == 1:
            base = rgb2hsv(base)
        
        if new_pal:
            if paltype == 0:
                self.palette = random_offset_palette(n, base, rng, edgefn)
            else:
                self.palette = value_offset_palette(n, base, rng, edgefn)
            
        with hold_canvas(self.canvas):
            for i, vec3 in enumerate(self.palette):
                if mode == 0:
                    self.canvas.fill_style = hsl2hex(vec3)
                elif mode == 1:
                    self.canvas.fill_style = hsv2hex(vec3)
                elif mode == 2:
                    self.canvas.fill_style = rgb2hex(vec3)
                
                self.canvas.fill_rect(i*width//n, 0, (i+1)*width//n, height)

            self.canvas.stroke_rect(0, 0, width, height)
        return self.canvas


