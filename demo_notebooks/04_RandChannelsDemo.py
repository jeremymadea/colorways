import os
import sys
from random import random

from ipycanvas import Canvas, hold_canvas
import ipywidgets as widgets 

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from colorways import *


class RandChannelsDemo:
    def __init__(self, w=720, h=200):
        self.width = w
        self.height = h
        self.canvas = Canvas(width=w, height=h)

        self.n = widgets.IntSlider(description="Colors", value=6, min=1, max=250, orientation='horizontal')
        self.n.observe(lambda _: self.draw(), 'value')

        self.palette = random_uniform_palette(self.n.value)
        self.unsorted = self.palette

        # GUI for base color picker.
        self.base = widgets.ColorPicker(
            concise=False,
            description='Base Color',
            value='#888888',
            disabled=False
        )
        self.base.observe(lambda _: self.draw(), 'value')

        # GUI for color mode selection.
        self.mode_options = [
            ('HSL', 0),
            ('HSV', 1), 
            ('RGB', 2)]
        self.mode = widgets.Dropdown(
            options=self.mode_options,
            value=0,
            description='Mode:',
        )
        self.mode.observe(self.mode_changed, 'value')

        # GUI for selecting the algorithm. 
        # Options change based on the current color mode. (self.mode)
        # The values of the selectbox are functions.
        self.alg_options_hsl = [
            ('All', random_uniform_palette),
            ('Hue', randhue_palette),
            ('Sat', randsat_palette),
            ('Lum', randlum_palette),
            ('Hue/Lum', randhuelum_palette),
            ('Hue/Sat', randhuesat_palette),
            ('Sat/Lum', randsatlum_palette)]
        self.alg_options_hsv = [
            ('All', random_uniform_palette),
            ('Hue', randhue_palette),
            ('Sat', randsat_palette),
            ('Val', randval_palette),
            ('Hue/Val', randhueval_palette),
            ('Hue/Sat', randhuesat_palette),
            ('Sat/Val', randsatval_palette)]
        self.alg_options_rgb = [
            ('All', random_uniform_palette),
            ('Red', randhue_palette),
            ('Green', randsat_palette),
            ('Blue', randlum_palette),
            ('R/B', randhuelum_palette),
            ('R/G', randhuesat_palette),
            ('G/B', randsatlum_palette)]
        self.alg = widgets.Dropdown(
            options=self.alg_options_hsl,
            value=random_uniform_palette,
            description='Randomize:',
        )
        self.alg.observe(lambda _: self.draw(), 'value')

        # GUI for choosing sort options. 
        # Options change based on current color mode.
        self.sort_options_hsl = [
            ('As generated', 0),
            ('Advanced', 1),
            ('Hue', sort_hsl_palette_by_hue), 
            ('Sat', sort_hsl_palette_by_sat), 
            ('Lum', sort_hsl_palette_by_lum), 
            ('Val', sort_hsl_palette_by_val), 
            ('Red', sort_hsl_palette_by_r), 
            ('Green', sort_hsl_palette_by_g), 
            ('Blue', sort_hsl_palette_by_b)]
        self.sort_options_hsv = [
            ('As generated', 0),
            ('Advanced', 1),
            ('Hue', sort_hsv_palette_by_hue), 
            ('Sat', sort_hsv_palette_by_sat), 
            ('Lum', sort_hsv_palette_by_lum), 
            ('Val', sort_hsv_palette_by_val), 
            ('Red', sort_hsv_palette_by_r), 
            ('Green', sort_hsv_palette_by_g), 
            ('Blue', sort_hsv_palette_by_b)]
        self.sort_options_rgb = [
            ('As generated', 0),
            ('Advanced', 1),
            ('Hue', sort_rgb_palette_by_hue), 
            ('Sat', sort_rgb_palette_by_sat), 
            ('Lum', sort_rgb_palette_by_lum), 
            ('Val', sort_rgb_palette_by_val), 
            ('Red', sort_rgb_palette_by_r), 
            ('Green', sort_rgb_palette_by_g), 
            ('Blue', sort_rgb_palette_by_b)]
        self.sorting = widgets.Dropdown(
            options=self.sort_options_hsl,
            description='Sorting:',
        )
        self.sorting.observe(self.sort_changed, 'value')

        # GUI for choosing advanced (distance) sort options. 
        # Options change based on color mode.
        self.advsort_options_hsl = [
            ('Euclidean', sort_hsl_palette_by_hsl_euclidean_from),
            ('CIE76', sort_hsl_palette_by_cie76_from),
            ('CIE94', sort_hsl_palette_by_cie94_from),
            ('CIEDE2000', sort_hsl_palette_by_ciede2000_from)]
        self.advsort_options_hsv = [
            ('Euclidean', sort_hsv_palette_by_hsv_euclidean_from),
            ('CIE76', sort_hsv_palette_by_cie76_from),
            ('CIE94', sort_hsv_palette_by_cie94_from),
            ('CIEDE2000', sort_hsv_palette_by_ciede2000_from)]
        self.advsort_options_rgb = [
            ('Euclidean', sort_rgb_palette_by_rgb_euclidean_from),
            ('Euclidean HSV', sort_rgb_palette_by_hsv_euclidean_from),
            ('Euclidean HSL', sort_rgb_palette_by_hsl_euclidean_from),
            ('CIE76', sort_rgb_palette_by_cie76_from),
            ('CIE94', sort_rgb_palette_by_cie94_from),
            ('CIEDE2000', sort_rgb_palette_by_ciede2000_from)]
        self.advsort = widgets.Dropdown(
            options=self.advsort_options_hsl,
            description='Sorting:',
            disabled = True,
        )
        self.advsort.observe(lambda _: self.draw(False), 'value')

        # GUI for picking the reference color for advanced (distance) sorting.
        self.advsort_ref = widgets.ColorPicker(
            concise=False,
            description='Dist from:',
            value='#888888',
            disabled=True
        )
        self.advsort_ref.observe(lambda _: self.draw(False), 'value')

        # GUI for randomize button
        self.randbut = widgets.Button(
            description='Randomize',
            disabled=False,
            button_style=''
        )

        self.randbut.on_click(lambda _: self.draw())

        basic_controls = widgets.VBox([self.mode, self.n, self.base, self.alg, self.sorting])
        advsort_label = widgets.Label(value="Advanced Sorting Controls")
        advsort_label.layout.align_self='center'
        advsort_controls = widgets.VBox([advsort_label, self.advsort, self.advsort_ref])
        display(widgets.HBox([basic_controls, advsort_controls]))
        display(self.randbut)


    def mode_changed(self, argdict):
        if argdict['new'] == 0:
            self.alg.options = self.alg_options_hsl
            self.sorting.options = self.sort_options_hsl
            self.advsort.options = self.advsort_options_hsl
        elif argdict['new'] == 1:
            self.alg.options = self. alg_options_hsv
            self.sorting.options = self.sort_options_hsv
            self.advsort.options = self.advsort_options_hsv
        elif argdict['new'] == 2:
            self.alg.options = self.alg_options_rgb
            self.sorting.options = self.sort_options_rgb
            self.advsort.options = self.advsort_options_rgb
        self.draw()

    def sort_changed(self, argdict):
        if argdict['new'] != 1:     
            self.advsort.disabled = True
            self.advsort_ref.disabled = True
        else: 
            self.advsort.disabled = False
            self.advsort_ref.disabled = False 
        self.draw(False)


    def draw(self, new_palette=True):
        n = self.n.value
        mode = self.mode.value
        base = hex2rgb(self.base.value)
        refclr = hex2rgb(self.advsort_ref.value) 
        width = self.width
        height = self.height

        if mode == 0:
            base = rgb2hsl(base)
            refclr = rgb2hsl(refclr)
        elif mode == 1:
            base = rgb2hsv(base)
            refclr = rgb2hsv(refclr)
        
        palette_function = self.alg.value
       
        if new_palette:
            if palette_function == random_uniform_palette:
                self.palette = palette_function(n)
                self.unsorted = self.palette
            else:
                self.palette = palette_function(n, base)
                self.unsorted = self.palette

        if self.sorting.value == 0:
            self.palette = self.unsorted
        elif self.sorting.value == 1:
            self.palette = self.advsort.value(self.palette, refclr)
        else:
            self.palette = self.sorting.value(self.palette)

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

