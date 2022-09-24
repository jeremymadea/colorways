
import os
import sys
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)


from ipycanvas import Canvas, hold_canvas
import ipywidgets as widgets 
from random import random
from colorways import *

def show_palette(palette, w=720, h=200):
    width = w
    height = h
    c = Canvas(width=width, height=height)
    n = len(palette)
    with hold_canvas(c):
        for i, vec3 in enumerate(palette):
            c.fill_style = hsl2hex(vec3)
            c.fill_rect(i*width//n, 0, (i+1)*width//n, height)
        c.stroke_rect(0, 0, width, height)
    return c

def show_multi_palette(*palettes, w=720, h=200, cvs=None):
    width = w
    height = h
    c = cvs
    if c is None:
        c = Canvas(width=width, height=height)
    npals = len(palettes)
    with hold_canvas(c):
        for i in range(npals):
            n = len(palettes[i])
            for j, vec3 in enumerate(palettes[i]):
                c.fill_style = hsl2hex(vec3)
                c.fill_rect(j*width//n, i*height//npals, (j+1)*width//n, (i+1)*height//npals)
                c.stroke_line(0, (i+1)*height//npals, width, (i+1)*height//npals)
        c.stroke_rect(0, 0, width, height)
    return c


def show_hsl(hsl):
    return show_color(hsl2hex(hsl))

def show_hsv(hsv): 
    return show_color(hsv2hex(hsv))

def show_hwb(hwb):
    return show_color(hwb2hex(hwb))

def show_rgb(rgb): 
    return show_color(rgb2hex(rgb))
            

def show_color(hexclr):
    width = 100
    height = 100
    c = Canvas(width=width, height=height)
    c.fill_style = hexclr
    c.fill_rect(0,0,width,height)
    c.stroke_rect(0,0,width,height)
    return c
