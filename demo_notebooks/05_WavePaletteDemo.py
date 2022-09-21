import os
import sys
from random import random

from ipycanvas import Canvas, hold_canvas
import ipywidgets as widgets 

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from colorways import *


class WavePaletteDemo:
    def __init__(self, w=720, h=200):
        self.width = w
        self.height = h
        self.canvas = Canvas(width=w, height=h)
        self.palette = None

        self.load_presets()

        self.randbut = widgets.Button(
            description='RaNDomiZe',
            disabled=False,
            button_style=''
        )
        self.randbut.on_click(lambda _: self.randomize())

        self.n = widgets.IntSlider(description="Colors",      value=50, min=1, max=250, orientation='vertical')
        self.f1 = widgets.FloatSlider(description="Freq1:",   value=0.33,  min=0.0, max=5.0, step=.01, orientation='vertical')
        self.f2 = widgets.FloatSlider(description="Freq2:",   value=0.5,   min=0.0, max=5.0, step=.01, orientation='vertical')
        self.f3 = widgets.FloatSlider(description="Freq3:",   value=0.625, min=0.0, max=5.0, step=.01, orientation='vertical')
        self.p1 = widgets.FloatSlider(description="Phase1:",  value=0.15*3.1416, min=-5, max=5, step=.01, orientation='vertical')
        self.p2 = widgets.FloatSlider(description="Phase2:",  value=0.15*3.1416, min=-5, max=5, step=.01, orientation='vertical')
        self.p3 = widgets.FloatSlider(description="Phase3:",  value=0.35*3.1416, min=-5, max=5, step=.01, orientation='vertical')
        self.o1 = widgets.FloatSlider(description="Offset1:", value=0.5,  min=-5, max=5, step=.01, orientation='vertical')
        self.o2 = widgets.FloatSlider(description="Offset2:", value=0.25, min=-5, max=5, step=.01, orientation='vertical')
        self.o3 = widgets.FloatSlider(description="Offset3:", value=0.3,  min=-5, max=5, step=.01, orientation='vertical')
        self.a1 = widgets.FloatSlider(description="Amp1:",    value=1, min=0, max=5, step=.01, orientation='vertical')
        self.a2 = widgets.FloatSlider(description="Amp2:",    value=1, min=0, max=5, step=.01, orientation='vertical')
        self.a3 = widgets.FloatSlider(description="Amp3:",    value=1, min=0, max=5, step=.01, orientation='vertical')

        self.sliders = [ self.n,
                         self.f1, self.f2, self.f3,
                         self.p1, self.p2, self.p3,
                         self.o1, self.o2, self.o3,
                         self.a1, self.a2, self.a3 ]

        self.preset_buttons = []
        for i, pset in enumerate(self.presets):
            self.preset_buttons.append( widgets.Button(
                description=f'Preset {i+1}',
            ))
            self.preset_buttons[-1].on_click(self.create_set_preset_callback(pset))

        self.all_sliders_observe()

        display(widgets.HBox(self.sliders))
        display(widgets.HBox([self.randbut] + self.preset_buttons))

    def randomize(self):
        fpoa = random_fpoa()
        self.set_preset(tuple([self.n.value] + fpoa))


    def all_sliders_observe(self):
        for s in self.sliders:
            s.observe(lambda _: self.draw(), 'value')
        
    def all_sliders_unobserve(self):
        for s in self.sliders:
            s.unobserve_all()
    
    def create_set_preset_callback(self, p):
        return lambda _: self.set_preset(p)

    def set_preset(self, preset):
        self.all_sliders_unobserve()
        self.n.value = preset[0]
        self.f1.value = preset[1][0]
        self.f2.value = preset[1][1]
        self.f3.value = preset[1][2]
        self.p1.value = preset[2][0]
        self.p2.value = preset[2][1]
        self.p3.value = preset[2][2]    
        self.o1.value = preset[3][0]
        self.o2.value = preset[3][1]
        self.o3.value = preset[3][2]
        self.a1.value = preset[4][0]
        self.a2.value = preset[4][1]
        self.a3.value = preset[4][2]
        self.all_sliders_observe()
        self.draw()
 
    def current_settings(self):
        return (self.n.value,
            [self.f1.value, self.f2.value, self.f3.value],
            [self.p1.value, self.p2.value, self.p3.value],
            [self.o1.value, self.o2.value, self.o3.value],
            [self.a1.value, self.a2.value, self.a3.value])
 
    def load_presets(self):

        self.presets = [(7,
              [1.345, 1.065, 0.745],
              [1.5707963267948966, 1.319468914507713, 1.0995574287564276],
              [1.3399999999999999, 0.25, 0.9],
              [1, 1, 1]),
             (100,
              [0.445, 0.635, 0.855],
              [1.6022122533307945, 1.382300767579509, 2.1362830044410597],
              [1.4100000000000001, 1.03, 1.04],
              [1, 1, 1]),
             (32,
              [0.995, 0.51, 0.54],
              [2.921681167838508, 1.413716694115407, 1.790707812546182],
              [-0.10000000000000009, 1.1, 1.27],
              [1, 1, 1]),
             (150,
              [0.98, 0.45, 1.02],
              [0.34557519189487723, 0.25132741228718347, 1.0995574287564276],
              [0.10999999999999999, 0.22999999999999998, 0.29000000000000004],
              [1, 1, 1]),
             (151,
              [0.62, 0.225, 0.05],
              [1.0053096491487339, 0.5654866776461628, 0.9738937226128359],
              [0.44999999999999996, 0.21999999999999997, 0.29],
              [1, 1, 1]),
             (150,
              [0.8754185416215507, 0.5100647113211614, 0.4971029005983944],
              [2.525869408293665, 0.16524836005364377, 1.0675815383561036],
              [1.1802587048869646, 1.1254781480308427, 1.2701816890002928],
              [1, 1, 1]),
             (82,
              [0.5132522731207945, 0.38391428715046, 0.8694473285978643],
              [2.9232985852944644, 0.5294157211719458, 0.26344340065363936],
              [0.9978925557910865, 1.3592034876373653, 1.1211810671295173],
              [1, 1, 1]),
             (101,
              [0.425, 0.6052829839192126, 0.46],
              [1.6336281798666925, 1.1938052083641213, 1.9163715186897738],
              [1.32, 0.99, 1.4],
              [1, 1, 1])]


        self.broken_presets = [
            (7, [2.69, 2.13, 1.49], [0.5, 0.42, 0.35], [0.7, -0.5, 0.4], [0.64, 0.75, 0.5]), 
            (100, [0.89, 1.27, 1.71], [0.51, 0.44, 0.68], [1.05, 0.58, 0.27], [0.36, 0.45, 0.77]), 
            (32, [1.99, 1.02, 1.08], [0.93, 0.45, 0.57], [-1.78, 0.43, 0.78], [1.68, 0.67, 0.49]),
            (150, [1.96, 0.9, 2.04], [0.11, 0.08, 0.35], [-0.3, -0.52, -0.26], [0.41, 0.75, 0.55]),
            (151, [1.24, 0.45, 0.1], [0.32, 0.18, 0.31], [-0.15, -0.54, -0.2], [0.6, 0.76, 0.49]),
            (150, [1.7508370832431015, 1.0201294226423228, 0.9942058011967888], 
                  [0.8040092038690752, 0.05260018668073341, 0.3398217579660475],
                  [0.5768668741782016, 0.6799773620865546, 0.7205886933736131],
                  [0.603391830708763, 0.44550078594428816, 0.5495929956266797]),
            (82, [1.026504546241589, 0.76782857430092, 1.7388946571957287],
                 [0.9305148399663172, 0.16851825795015152, 0.08385663887793071], 
                 [0.4562136883485164, 0.7783222857546727, 0.5525876116917988], 
                 [0.5416788674425701, 0.5808812018826927, 0.5685934554377184]),
            (101, [0.85, 1.2105659678384253, 0.92], [0.52, 0.38, 0.61], [0.21, 0.58, 0.92], [1.11, 0.41, 0.48]),
        ]
    
    def draw(self):
        n = self.n.value
        f1 = self.f1.value
        f2 = self.f2.value
        f3 = self.f3.value
        p1 = self.p1.value
        p2 = self.p2.value
        p3 = self.p3.value
        o1 = self.o1.value
        o2 = self.o2.value
        o3 = self.o3.value
        a1 = self.a1.value
        a2 = self.a2.value
        a3 = self.a3.value
        width = self.width
        height = self.height
        
        fpoa = [[f1, f2, f3], [p1, p2, p3], [o1, o2, o3], [a1, a2, a3]]
        
        self.palette = wave_palette(n, fpoa)
        
        with hold_canvas(self.canvas):
            for i, vec3 in enumerate(self.palette):
                self.canvas.fill_style = rgb2hex(vec3)
                self.canvas.fill_rect(i*width//n, 0, (i+1)*width//n, height)
            self.canvas.stroke_rect(0, 0, width, height)
        return self.canvas






