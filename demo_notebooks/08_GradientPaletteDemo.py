import os
import sys
from random import random

from ipycanvas import Canvas, hold_canvas
import ipywidgets as widgets 

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from colorways import *


class GradientPaletteDemo:
    def __init__(self, w=720, h=200):
        self.width = w
        self.height = h
        self.canvas = Canvas(width=w, height=h)

        self.max_segments = 5

        self.n_segs = widgets.IntSlider(
            description="Segments",
            value=2,
            min=1,
            max=self.max_segments,
            orientation='horizontal')
        self.n_segs.observe(self.n_segs_changed, 'value')

        self.colors = [
            widgets.ColorPicker(
                concise=False,
                description=f'Color {i}',
                value=rgb2hex(randvec3()),
                disabled=False
            ) for i in range(self.max_segments + 1)]
        for p in self.colors:
            p.observe(lambda _: self.draw(), 'value')

        self.seg_n = [
            widgets.IntSlider(
                description=f"Length", 
                value=6, 
                min=1, 
                max=50, 
                orientation='horizontal'
            ) for i in range(self.max_segments)]
        for s in self.seg_n:
            s.observe(lambda _: self.draw(), 'value')

        self.segs = [
                widgets.HBox([self.colors[i], self.colors[i+1], self.seg_n[i]]) for i in range(self.max_segments)
        ]
        

        # GUI for color mode selection.
        self.mode_options = [
            ('HSL', 0),
            ('HSV', 1), 
            ('HWB', 2),
            ('RGB', 3),
            ('Lab', 4),
        ]
        self.mode = widgets.Dropdown(
            options=self.mode_options,
            value=0,
            description='Mode:',
        )
        self.mode.observe(self.mode_changed, 'value')

        self.arcdir = widgets.Dropdown(
            options = [('short', 0), ('long', 1)],
            value = 0,
            description = 'Hue Path:'
        )
        self.arcdir.observe(lambda _: self.draw(), 'value')

        self.n_segs.value = 1
        display(widgets.HBox([self.n_segs, self.mode, self.arcdir]))
        display(widgets.VBox(self.segs))

    def n_segs_changed(self, argdict):
        for i in range(self.max_segments):
            if i < argdict['new']:
                self.segs[i].layout.visibility = 'visible'
            else:
                self.segs[i].layout.visibility = 'hidden'
        self.draw()


    def mode_changed(self, argdict):
        if argdict['new'] == 0:
            self.arcdir.disabled = False
        elif argdict['new'] == 1:
            self.arcdir.disabled = False
        elif argdict['new'] == 2:
            self.arcdir.disabled = False
        elif argdict['new'] == 3:
            self.arcdir.disabled = True
        elif argdict['new'] == 4:
            self.arcdir.disabled = True
        self.draw()


    def draw(self, new_palette=True):
        n_segs = self.n_segs.value
        mode = self.mode.value
        colors = [ hex2rgb(p.value) for p in self.colors ]
        n_clrs = [ n.value for n in self.seg_n ]
        width = self.width
        height = self.height

        bigarc = False
        if self.arcdir.value == 1:
            bigarc = True 

        if mode == 0:
            colors = rgb2hsl(colors)
        elif mode == 1:
            colors = rgb2hsv(colors)
        elif mode == 2:
            colors = rgb2hwb(colors)
        elif mode == 3:
            pass
        elif mode == 4:
            colors = rgb2lab(colors)
      
 
        if new_palette:
            if mode in (0, 1, 2):
                self.palette = hue_gradient_palette(colors[0:n_segs+1], n_clrs[0:n_segs], bigarc)
            else: 
                self.palette = gradient_palette(colors[0:n_segs+1], n_clrs[0:n_segs])

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
                elif mode == 4:
                    self.canvas.fill_style = lab2hex(vec3) 
                self.canvas.fill_rect(i*width//n, 0, (i+1)*width//n, height)

            self.canvas.stroke_rect(0, 0, width, height)
        return self.canvas

