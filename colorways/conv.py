import colorsys
from .internals import colpal_function, colpal_params_function, hexpal_function
from .util import clamp01, turn2deg, turn2rad, mmult
from .matrices import srgb_rgb2xyz, srgb_xyz2rgb 
from .matrices import srgb_rgb2xyz_D50, srgb_xyz2rgb_D50 
from math import pi, sqrt, atan2, degrees, radians, cos, sin

"""
This module provides conversion functions for colors and palettes.

Exports:
    Color space conversion functions. These take a single argument
    which is expected to be either a 3-element list (i.e. a color)
    or a list of colors (i.e. a palette.) 
    
    Conversions to and from XYZ. These are used internally as interim 
    conversions between L*a*b* and RGB colorspaces. 
 
        xyz2lab lab2xyz rgb2xyz xyz2rgb

    Conversions between RGB, HSL, HSV, HWB, L*a*b*, and L*C*h(ab) colorspaces.
    
        hsl2hsv hsl2hwb hsl2rgb hsl2lab hsl2lch
        hsv2hsl hsv2hwb hsv2rgb hsv2lab hsv2lch
        hwb2hsl hwb2hsv hwb2rgb hwb2lab hwb2lch
        rgb2hsl rgb2hsv rgb2hwb rgb2lab rgb2lch
        lab2hsl lab2hsv lab2hwb lab2rgb lab2lch
        lch2hsl lch2hsv lch2hwb lch2rgb lch2lab

    Conversions between RGB hexcodes and HSL, HSV, HWB, L*a*b*, and L*C*h(ab)

        hex2hsl hex2hsv hex2hwb hex2rgb hex2lab hex2lch
        hsl2hex hsv2hex hwb2hex rgb2hex lab2hex lch2hex

    Representation conversions. 
        bytes2norm
        rgb82rgb
        norm2bytes
        rgb2rgb8
        hex2bytes
        bytes2hex
        hxx_in_degpct
        rgb_in_percent

    Miscellaneous conversions. 
        rgb2hue
        srgb2linsrgb(rgb):
        linsrgb2srgb(rgb):


"""

__all__ = [
    'xyz2lab', 'lab2xyz', 'rgb2xyz', 'xyz2rgb',

    'hsl2hsv', 'hsl2hwb', 'hsl2rgb', 'hsl2lab', 'hsl2lch',
    'hsv2hsl', 'hsv2hwb', 'hsv2rgb', 'hsv2lab', 'hsv2lch',
    'hwb2hsl', 'hwb2hsv', 'hwb2rgb', 'hwb2lab', 'hwb2lch',
    'rgb2hsl', 'rgb2hsv', 'rgb2hwb', 'rgb2lab', 'rgb2lch',
    'lab2hsl', 'lab2hsv', 'lab2hwb', 'lab2rgb', 'lab2lch',
    'lch2hsl', 'lch2hsv', 'lch2hwb', 'lch2rgb', 'lch2lab', 

    'hex2hsl', 'hex2hsv', 'hex2hwb', 'hex2rgb', 'hex2lab', 'hex2lch',
    'hsl2hex', 'hsv2hex', 'hwb2hex', 'rgb2hex', 'lab2hex', 'lch2hex',

    'bytes2norm',
    'rgb82rgb',
    'norm2bytes',
    'rgb2rgb8',
    'hex2bytes',
    'bytes2hex',
    'rgb_in_percent',
    'hxx_in_degpct',

    'rgb2hue',
    'srgb2linsrgb',
    'linsrgb2srgb',
    
    ]


########################################
#
# Conversions between RGB and XYZ and between L*a*b* and XYZ.  
# These are core functions needed for interim conversion between RGB and L*a*b*. 
# 
# TODO: Enable different luminants and observation angles. 

@colpal_function
def rgb2xyz(rgb):
    """Interprets the given vec3 as RGB and converts it to XYZ"""
    # This is a necessary initial step for RGB->L*a*b*
    # http://www.brucelindbloom.com/index.html?Eqn_RGB_to_XYZ.html
    # https://www.easyrgb.com/en/math.php
    tmp = list(rgb)
    for i in range(3):  
        if tmp[i] > 0.04045: 
            tmp[i] = ((tmp[i] + 0.055) / 1.055) ** 2.4
        else: 
            tmp[i] /= 12.92
        
        tmp[i] *= 100
    return mmult(tmp, srgb_rgb2xyz)


@colpal_function
def xyz2rgb(xyz):
    """Interprets the given vec3 as XYZ and converts it to RGB"""
    # This is a necessary final step for L*a*b*->RGB
    # http://www.brucelindbloom.com/index.html?Eqn_XYZ_to_RGB.html
    # https://www.easyrgb.com/en/math.php
    (x, y, z) = xyz
    x /= 100.0
    y /= 100.0
    z /= 100.0
    rgb = mmult([x,y,z], srgb_xyz2rgb)
    for i in range(3):
        if rgb[i] > 0.0031308:
            rgb[i] = 1.055 * (rgb[i]**(1.0/2.4)) - 0.055
        else:
            rgb[i] *= 12.92
        rgb[i] = min(max(0.0, rgb[i]), 1.0)
    return rgb



@colpal_function
def xyz2lab(xyz):
    """Interprets the given vec3 as XYZ and converts it to L*a*b*"""
    # https://www.easyrgb.com/en/math.php
    tmp = list(xyz)
    tmp[0] /= 95.047 
    tmp[1] /= 100.000
    tmp[2] /= 108.883
    for i in range(3):
        if tmp[i] > 0.008856:
            tmp[i] **= (1.0/3.0)
        else:
            tmp[i] = (7.787 * tmp[i]) + (16.0/116.0)
    return [
        (116 * tmp[1]) - 16, 
        500 * (tmp[0] - tmp[1]), 
        200 * (tmp[1] - tmp[2])] 
        
    
@colpal_function
def lab2xyz(lab):
    """Interprets the given vec3 as L*a*b* and converts it to XYZ"""
    # https://www.easyrgb.com/en/math.php
    y = (lab[0] + 16) / 116.0
    x = lab[1] / 500.0 + y
    z = y - lab[2] / 200.0
    xyz = [x, y, z]
    for i in range(3):
        cube = xyz[i] ** 3
        if cube > 0.008856: 
            xyz[i] = cube
        else: 
            xyz[i] = (xyz[i] - 16/116.0) / 7.787
    xyz[0] = xyz[0] * 95.047
    xyz[1] = xyz[1] * 100.000
    xyz[2] = xyz[2] * 108.883
    return xyz



# Conversions between hex strings and bytes [0,255]

@colpal_function
def bytes2hex(vec):
    """
    Converts a list of ints in the range [0,255] to hex strings in #RRGGBB  
    format. 
    """
    return '#' + ''.join('%02X' % i for i in vec)


@hexpal_function
def hex2bytes(hexstr):
    """
    Converts a hex string in #RRGGBB format to a list of ints in [0,255].
    """
    if hexstr[0] == '#':
        hexstr = hexstr[1:]
    return [int(hexstr[:2], 16), int(hexstr[2:4], 16), int(hexstr[4:6], 16)]



# Hex codes
def hex2rgb(hexstr):
    """Converts a hex string in #RRGGBB format to a RGB vec3 in [0,1]. """
    return bytes2norm( hex2bytes( hexstr ))



def hex2hsl(hexcode):
    """Converts hex strings in #RRGGBB format to HSL.  """
    return rgb2hsl( hex2rgb( hexcode ))



def hex2hsv(hexcode):
    """Converts hex strings in #RRGGBB format to HSV.  """
    return rgb2hsv( hex2rgb( hexcode ))



def hex2hwb(hexcode):
    """Converts hex strings in #RRGGBB format to HWB.  """
    return rgb2hwb( hex2rgb( hexcode ))



def hex2lab(hexcode):
    """Converts hex strings in #RRGGBB format to L*a*b*.  """
    return rgb2lab( hex2rgb( hexcode))

#def hex2lch(hexcode):



def hsl2hex(hsl):
    """
    Converts an HSL vec3 to a hex string in #RRGGBB format.
    """
    return bytes2hex(norm2bytes(hsl2rgb( hsl )))



def hsv2hex(hsv):
    """
    Converts an HSV vec3 to a hex string in #RRGGBB format.
    """
    return bytes2hex( norm2bytes( hsv2rgb( hsv )))



def hwb2hex(hwb):
    """
    Converts an HWB vec3 to a hex string in #RRGGBB format.
    """
    return bytes2hex( norm2bytes( hwb2rgb( hwb )))



def lab2hex(lab):
    """
    Converts an HSL vec3 to a hex string in #RRGGBB format.
    """
    return bytes2hex( norm2bytes( lab2rgb( lab )))


@colpal_function
def rgb2hex(rgb):
    """
    Converts an HSL vec3 to a hex string in #RRGGBB format.
    """
    return bytes2hex( norm2bytes( rgb ))



### Color mode conversion functions

@colpal_function
def hsv2hsl(hsv):
    """Interprets the given vec3 as HSV and converts it to HSL"""
    h = hsv[0]
    l = hsv[2] * (1-hsv[1]/2)
    s = 0 if l==0 or l==1 else (hsv[2]-l)/min(l, 1-l)
    return [h, s, l]
 
    
          
@colpal_function
def hsl2hsv(hsl):    
    """Interprets the given vec3 as HSL and converts it to HSV"""
    h = hsl[0]
    v = hsl[2] + hsl[1] * min(hsl[2], 1-hsl[2])
    s = 0 if v == 0 else 2 * (1 -hsl[2]/v)
    return [h, s, v]



@colpal_function
def rgb2hsv(rgb):
    """Interprets the given vec3 as RGB and converts it to HSV"""
    return list(colorsys.rgb_to_hsv(*rgb))



@colpal_function
def rgb2hsl(rgb):
    """Interprets the given vec3 as RGB and converts it to HSL"""
    h, l, s = colorsys.rgb_to_hls(*rgb)
    return [h, s, l]



@colpal_function
def hsv2rgb(hsv): 
    """Interprets the given vec3 as HSV and converts it to RGB"""
    return list(colorsys.hsv_to_rgb(*hsv))



@colpal_function
def hsl2rgb(hsl):
    """Interprets the given vec3 as HSL and converts it to RGB"""
    return list(colorsys.hls_to_rgb(hsl[0], hsl[2], hsl[1]))



def rgb2lab(rgb):
    """Interprets the given vec3 as RGB and converts it to L*a*b*."""
    return xyz2lab(rgb2xyz(rgb))



def lab2rgb(lab):
    """Interprets the given vec3 as L*a*b* and converts it to RGB"""
    return xyz2rgb(lab2xyz(lab))



def lab2hsv(lab):
    """Interprets the given vec3 as L*a*b* and converts it to HSV"""
    return rgb2hsv(lab2rgb(lab))



def lab2hsl(lab):
    """Interprets the given vec3 as L*a*b* and converts it to HSL"""
    return rgb2hsl(lab2rgb(lab))



def hsv2lab(hsv):
    """Interprets the given vec3 as HSV and converts it to L*a*b*"""
    return rgb2lab(hsv2rgb(hsv))



def hsl2lab(hsl):
    """Interprets the given vec3 as HSL and converts it to L*a*b*"""
    return rgb2lab(hsl2rgb(hsl))



@colpal_function
def hsv2hwb(hsv):
    """Interprets the given vec3 as HSV and converts to HWB"""
    return [ hsv[0], (1-hsv[1])*hsv[2], 1-hsv[2] ]



@colpal_function
def hwb2hsv(hwb):
    """Interprets the given vec3 as HWB and converts to HSV"""
    (h,w,b) = hwb
    scalar = w + b
    if scalar > 1:
        w /= scalar
        b /= scalar
    sat = 0.0 if b == 1 else 1-w/(1-b)
    return [ h, sat, 1-b ]



def rgb2hwb(rgb):
    """Interprets the given vec3 as RGB and converts to HWB"""
    return hsv2hwb(rgb2hsv(rgb))



def hwb2rgb(hwb):
    """Interprets the given vec3 as HWB and converts to RGB"""
    return hsv2rgb(hwb2hsv(hwb))



def hsl2hwb(hsl):
    """Interprets the given vec3 as HSL and converts to HWB"""
    return hsv2hwb(hsl2hsv(hsl))



def hwb2hsl(hwb):
    """Interprets the given vec3 as HWB and converts to HSL"""
    return hsv2hsl(hwb2hsv(hwb))



def lab2hwb(lab):
    """Interprets the given vec3 as L*a*b* and converts to HWB"""
    return hsv2hwb(lab2hsv(lab))



def hwb2lab(hwb):
    """Interprets the given vec3 as HWB and converts it to L*a*b* """
    return hsv2lab(hwb2hsv(hwb))


@colpal_function
def lab2lch(lab):
    """Interprets the given vec3 as L*a*b* and converts it to L*C*h(ab) """
    (l,a,b) = lab
    c = sqrt(a**2 + b**2) 
    h = atan2(b,a) / (2*pi)
    return [l,c,h]

@colpal_function
def lch2lab(lch):
    """Interprets the given vec3 as L*C*h(ab) and converts it to L*a*b* """
    (l,c,h) = lch
    a = c * cos(turn2rad(h))
    b = c * sin(turn2rad(h))
    return [l, a, b]

def hsl2lch(hsl):
    """Interprets the given vec3 as HSL and converts it to L*C*h(ab) """
    return lab2lch(hsl2lab(hsl))

def hsv2lch(hsv):
    """Interprets the given vec3 as HSV and converts it to L*C*h(ab) """
    return lab2lch(hsv2lab(hsv))

def hwb2lch(hwb):
    """Interprets the given vec3 as HWB and converts it to L*C*h(ab) """
    return lab2lch(hwb2lab(hwb))

def rgb2lch(rgb):
    """Interprets the given vec3 as RGB and converts it to L*C*h(ab) """
    return lab2lch(rgb2lab(rgb))

def hex2lch(hexstr):
    """Converts the given RGB hexcode it to L*C*h(ab) """
    return lab2lch(hex2lab(hexstr))

def lch2rgb(lch):
    """Interprets the given vec3 as L*C*h(ab) and converts it to RGB """
    return lab2rgb(lch2lab(lch))

def lch2hsl(lch):
    """Interprets the given vec3 as L*C*h(ab) and converts it to HSL """
    return lab2hsl(lch2lab(lch))

def lch2hsv(lch):
    """Interprets the given vec3 as L*C*h(ab) and converts it to HSV """
    return lab2hsv(lch2lab(lch))

def lch2hwb(lch):
    """Interprets the given vec3 as L*C*h(ab) and converts it to HWB """
    return lab2hwb(lch2lab(lch))

def lch2hex(lch):
    """
    Interprets the given vec3 as L*C*h(ab) and converts it to an RGB hexcode. 
    """
    return lab2hex(lch2lab(lch))

########################################
#
# Representation conversions. 
#

@colpal_function
def bytes2norm(vec):
    """
    Converts list of unsigned bytes to floats in the range [0,1].
    """
    return [c/255.0 for c in vec]

rgb82rgb = bytes2norm # Alias

@colpal_function
def norm2bytes(vec):
    """
    Converts list of floats in the range [0,1] to ints in the range [0,255]. 
    """
    return [ round(x * 255) for x in vec ]

rgb2rgb8 = norm2bytes # Alias


@colpal_params_function
def hxx_in_degpct(hxx, decs=3):
    """
    Interprets given vec3 as an Hxx (HSL, HSV, HWB) and converts to a vec3 where
    the H component is in degrees and the other components are in percentages.
    The optional decs parameter (default:3) determines the number of decimal 
    places in the returned components.
    """
    (h, c1, c2) = hxx
    err = 10e-8 # TODO take a closer look at this.
    return [ round(360*h+err,decs), 
             round(100*c1+err,decs), round(100*c2+err,decs) ]

@colpal_params_function
def rgb_in_percent(rgb, decs=3):
    """
    Interprets given vec3 as an RGB value and converts to a vec3 where
    the components are in percentages. The optional decs parameter (default:3) 
    determines the number of decimal places in the returned components.
    """
    err = 10e-8 # TODO take a closer look at this.
    return [ round(100*c+err,decs) for c in rgb ]



########################################
#
# Miscellaneous conversions. 
#

@colpal_params_function
def rgb2hue(rgb, unit='turn'):
    """
    Interprets given vec3 as an RGB and returns its hue. Questionable accuracy.
    Optional unit argument specifies the unit the returned hue value is in. 
    It can be 'turn' (the default), 'deg' or 'rad'.
    """
    (r,g,b) = rgb
    mn = min(rgb)
    mx = max(rgb)
    delta = mx-mn
    if delta == 0: return 0.0
    multiplier = 1.0/(6*delta)

    if r == mx:
        hue = (g-b) * multiplier
    elif g == mx:
        hue = (1.0/3) + (b-r) * multiplier
    elif b == mx:
        hue = (2.0/3) + (r-g) * multiplier

    hue = hue % 1

    if unit == 'deg':
        return turn2deg(hue)
    elif unit == 'rad':
        return turn2rad(hue)
    return hue

@colpal_function
def srgb2linsrgb(rgb):
    """Converts sRGB to linear sRGB"""
    return [ 
        ((c + 0.055) / 1.055)**2.4 if c > 0.04045 else c / 12.92 
        for c in rgb ]

@colpal_function
def linsrgb2srgb(rgb):
    return [
        c * 12.92 if c < 0.0031308 else (1 + 0.055) * c**(1/2.4) - 0.055
        for c in rgb ]
