import os
import sys
from random import random

from ipycanvas import Canvas, hold_canvas
import ipywidgets as widgets 

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from colorways import *


class PermsPaletteDemo:
    def __init__(self, w=720, h=200):
        self.width = w
        self.height = h
        self.canvas = Canvas(width=w, height=h)

        self.max_bases = 4

        self.n_bases = widgets.IntSlider(
            description="Base Colors",
            value=1,
            min=1,
            max=self.max_bases,
            orientation='horizontal')
        self.n_bases.observe(self.n_bases_changed, 'value')

        self.colors = [
            widgets.ColorPicker(
                concise=False,
                description=f'Color {i}',
                value=rgb2hex(randvec3()),
                disabled=False
            ) for i in range(self.max_bases)]
        for p in self.colors:
            p.observe(lambda _: self.draw(), 'value')

        self.bases = [
                widgets.HBox([self.colors[i]]) for i in range(self.max_bases)
        ]
        

        # GUI for color mode selection.
        self.mode_options = [
            ('HSL', 0),
            ('HSV', 1), 
            ('HWB', 2),
            ('RGB', 3),
        ]
        self.mode = widgets.Dropdown(
            options=self.mode_options,
            value=0,
            description='Mode:',
        )
        self.mode.observe(self.mode_changed, 'value')

        self.n_bases.value = 2
        display(widgets.HBox([self.n_bases, self.mode]))
        display(widgets.VBox(self.bases))

    def n_bases_changed(self, argdict):
        for i in range(self.max_bases):
            if i < argdict['new']:
                self.bases[i].layout.visibility = 'visible'
            else:
                self.bases[i].layout.visibility = 'hidden'
        self.draw()


    def mode_changed(self, argdict):
        self.draw()


    def draw(self, new_palette=True):
        n_bases = self.n_bases.value
        mode = self.mode.value
        colors = [ hex2rgb(p.value) for p in self.colors ]
        width = self.width
        height = self.height

        if mode == 0:
            colors = rgb2hsl(colors)
        elif mode == 1:
            colors = rgb2hsv(colors)
        elif mode == 2:
            colors = rgb2hwb(colors)
        elif mode == 3:
            pass
      
 
        if new_palette:
            self.palette = perms_palette(colors[:n_bases])

        n = len(self.palette)
        with hold_canvas(self.canvas):
            for i, vec3 in enumerate(self.palette):
                if mode == 0:
                    self.canvas.fill_style = hsl2hex(vec3)
                elif mode == 1:
                    self.canvas.fill_style = hsv2hex(vec3)
                elif mode == 2:
                    self.canvas.fill_style = hwb2hex(vec3)
                elif mode == 3:
                    self.canvas.fill_style = rgb2hex(vec3)
                self.canvas.fill_rect(i*width//n, 0, (i+1)*width//n, height)

            self.canvas.stroke_rect(0, 0, width, height)
        return self.canvas

