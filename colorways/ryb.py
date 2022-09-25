from .internals import colpal_function
from .conv import (
    rgb2hsl, rgb2hsv, rgb2hwb, rgb2lab, 
    hsl2rgb, hsv2rgb, hwb2rgb, lab2rgb )

__all__ = [
    'ryb2rgb',
    'ryb2hsl',
    'ryb2hsv',
    'ryb2hwb',
    'ryb2lab',
    'rgb2ryb',
    'hsl2ryb',
    'hsv2ryb',
    'hwb2ryb',
    'lab2ryb',
]

"""
This module provides RYB color space conversions. 
"""

################################################################################
# The functions rgb2ryb and ryb2rgb contain only minor modification to the 
# original versions by Arah J. Leonard found here:
# http://web.archive.org/web/20130415143903/http://www.insanit.net/tag/rgb-to-ryb/
#
# The original copyright notice and licensing: 
# Author: Arah J. Leonard
# Copyright 01AUG09
# Distributed under the LGPL - http://www.gnu.org/copyleft/lesser.html
# ALSO distributed under the The MIT License from the Open Source Initiative 
# (OSI) - http://www.opensource.org/licenses/mit-license.php
# You may use EITHER of these licenses to work with / distribute this source 
# code.
# Enjoy!


# Convert a red-green-blue system to a red-yellow-blue system.
@colpal_function
def rgb2ryb(rgb):
    r, g, b = rgb

    # Remove the whiteness from the color.
    w = min(r, g, b)
    r = r - w
    g = g - w
    b = b - w

    mg = max(r, g, b)

    # Get the yellow out of the red+green.
    y = min(r, g)
    r -= y
    g -= y

    # If this unfortunate conversion combines blue and green, 
    # then cut each in half to preserve the value's maximum range.
    if b and g:
        b /= 2.0
        g /= 2.0

    # Redistribute the remaining green.
    y += g
    b += g

    # Normalize to values.
    my = float(max(r, y, b))
    if my:
        n = mg / my
        r *= n
        y *= n
        b *= n

    # Add the white back in.
    r += w
    y += w
    b += w

    # And return back the ryb typed accordingly.
    #if t is int:
    #    print("rounding")
    #    return[round(r), round(g), round(b)]

    #return [t(r), t(y), t(b)]
    return [r, y, b]



# Convert a red-yellow-blue system to a red-green-blue system.
@colpal_function
def ryb2rgb(ryb):
    r, y, b = ryb

    # Remove the whiteness from the color.
    w = (min(r, y, b))
    r = r - w
    y = y - w
    b = b - w

    my = max(r, y, b)

    # Get the green out of the yellow and blue
    g = min(y, b)
    y -= g
    b -= g

    if b and g:
        b *= 2.0
        g *= 2.0

    # Redistribute the remaining yellow.
    r += y
    g += y

    # Normalize to values.
    mg = float(max(r, g, b))
    if mg:
        n = my / mg
        r *= n
        g *= n
        b *= n

    # Add the white back in.
    r += w
    g += w
    b += w

    return [r, g, b]


def ryb2hsl(ryb):
    return rgb2hsl(ryb2rgb(ryb))

def ryb2hsv(ryb):
    return rgb2hsv(ryb2rgb(ryb))

def ryb2hwb(ryb):
    return rgb2hwb(ryb2rgb(ryb))

def ryb2lab(ryb):
    return rgb2lab(ryb2rgb(ryb))


def hsl2ryb(hsl):
    return rgb2ryb(hsl2rgb(hsl))

def hsv2ryb(hsv):
    return rgb2ryb(hsv2rgb(hsv))

def hwb2ryb(hwb):
    return rgb2ryb(hwb2rgb(hwb))

def lab2ryb(lab):
    return rgb2ryb(lab2rgb(lab))

