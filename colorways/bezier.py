from random import random, normalvariate
from .util import clamp01
__all__ = [
    'quadratic_palette',
    'random_quadratic_palette',
    'cubic_palette', 
    'random_cubic_palette', 
]

def _quadratic(x, a, b, c):
    return clamp01(a*(1-x)**2+4*b*x*(1-x)+c*x**2)

def random_quadratic_params():
    return ([random(), normalvariate(0.25, 0.5), random()],
            [random(), normalvariate(0.25, 0.5), random()],
            [random(), normalvariate(0.25, 0.5), random()])

def quadratic_palette(n, rabc, gabc, babc):
    return [[_quadratic(x/n, *rabc), 
             _quadratic(x/n, *gabc),
             _quadratic(x/n, *babc)] for x in range(n)]

def random_quadratic_palette(n):
    return quadratic_palette(n, *random_quadratic_params())


# a_{0}\left(1-t\right)^{3\ }+\ 3b_{0}t\left(1-t\right)^{2\ }+\ 3c_{0}t^{2}\left(1-t\right)\ +\ d_{0}t^{3}

def _cubic(t, a, b, c, d):
    # a(1-t)^3 + 3bt(1-t)^2 + 3ct^2(1-t) + dt^2
    return clamp01(a*(1-t)**3 + 3*b*t*(1-t)**2 + 3*c*t**2*(1-t) + d*t**2)

def random_cubic_params():
    return ([random(), normalvariate(0.25, 0.5), random(), random()],
            [random(), normalvariate(0.25, 0.5), random(), random()],
            [random(), normalvariate(0.25, 0.5), random(), random()])

def cubic_palette(n, rabcd, gabcd, babcd):
    return [[_cubic(x/n, *rabcd), 
             _cubic(x/n, *gabcd),
             _cubic(x/n, *babcd)] for x in range(n)]

def random_cubic_palette(n):
    return cubic_palette(n, *random_cubic_params())

#def bez_cubic_curve(t, y0, y1, ax, ay, bx, by):
#    return (_cubic(t, 0, ax, bx, 1), _cubic(t, y0, by, cy, y1))


