from random import random, normalvariate
from .util import clamp01

"""This module provides functions for bezier curve palettes."""

__all__ = [
    'quadratic_palette',
    'random_quadratic_palette',
    'cubic_palette', 
    'random_cubic_palette', 
]


# Quadratic Bezier 

def _quadratic(x, a, b, c):
    return clamp01(a*(1-x)**2+4*b*x*(1-x)+c*x**2)

def random_quadratic_params():
    return ([random(), normalvariate(0.25, 0.5), random()],
            [random(), normalvariate(0.25, 0.5), random()],
            [random(), normalvariate(0.25, 0.5), random()])

def _quadratic_palette(n, rabc, gabc, babc):
    return [[_quadratic(x/n, *rabc), 
             _quadratic(x/n, *gabc),
             _quadratic(x/n, *babc)] for x in range(n)]

def random_quadratic_palette(n):
    """Returns a random quadratic bezier palette with n colors."""
    return _quadratic_palette(n, *random_quadratic_params())

def quadratic_palette(n, a, b, c):
    """Returns a quadratic bezier palette with n colors defined by points 
       a, b, and c."""
    return _quadratic_palette(n,
        [a[0],b[0],c[0]],
        [a[1],b[1],c[1]],
        [a[2],b[2],c[2]])


# Cubic Bezier

def _cubic(t, a, b, c, d):
    return clamp01(a*(1-t)**3 + 3*b*t*(1-t)**2 + 3*c*t**2*(1-t) + d*t**2)

def random_cubic_params():
    return ([random(), normalvariate(0.25, 0.5), random(), random()],
            [random(), normalvariate(0.25, 0.5), random(), random()],
            [random(), normalvariate(0.25, 0.5), random(), random()])

def _cubic_palette(n, rabcd, gabcd, babcd):
    return [[_cubic(x/n, *rabcd), 
             _cubic(x/n, *gabcd),
             _cubic(x/n, *babcd)] for x in range(n)]

def random_cubic_palette(n):
    """Returns a random cubic bezier palette with n colors."""
    return _cubic_palette(n, *random_cubic_params())

def cubic_palette(n, a, b, c, d):
    """Returns a cubic bezier palette with n colors defined by points 
       a, b, c, and d."""
    return _cubic_palette(n,
        [a[0],b[0],c[0],d[0]],
        [a[1],b[1],c[1],d[1]],
        [a[2],b[2],c[2],d[2]])

