from math import sqrt, cos, pi
from .util import clamp01
from .conv import norm2bytes, bytes2norm
from .internals import blend_function

"""This module provides functions for blending colors."""

__all__ = [
    'blend_multiply',
    'blend_screen',
    'blend_overlay',
    'blend_softlight',
    'blend_softlight_ps',
    'blend_softlight_peg',
    'blend_softlight_ill',
    'blend_divide', 
    'blend_lighten',
    'blend_darken',
    'blend_difference',
    'blend_subtract',
    'blend_plus_darker',
    'blend_plus_lighter',
    'blend_linear_dodge',
    'blend_add',
    'blend_average',
    'blend_negate',
    'blend_exclude',
    'blend_hardlight',
    'blend_colorburn',
    'blend_softburn',
    'blend_colordodge',
    'blend_softdodge',
    'blend_reflect',
    'blend_freeze',
    'blend_xor_rgb8',
    'blend_xor',
    'blend_and_rgb8',
    'blend_and',
    'blend_or_rgb8',
    'blend_or',
    'blend_stamp',
    'blend_cosine'
]


# Most formulas from 
# https://en.wikipedia.org/wiki/Blend_modes

@blend_function
def blend_multiply(base, blend):
    """multiply"""
    return [min(1.0, a*b) for a, b in zip(base, blend)]



@blend_function
def blend_screen(base, blend):
    """screen"""
    return [1-(1-a)*(1-b) for a, b in zip(base, blend)]



@blend_function
def blend_overlay(base, blend):
    """overlay"""
    return [2*a*b if a < 0.5 else 1-2*(1-a)*(1-b) for a, b in zip(base, blend)]



@blend_function
def blend_divide(base, blend):
    """Undocumented."""
    return [
        a/b if 0<a<b else 0.0 if a == 0 else 1.0 for a, b in zip(base, blend)]



#@blend_function
#def blend_divide_alt(base, blend):
#    """Undocumented. TODO: based on byte representation"""
#    return [ min(1, a/ ((b+1/256)/256) ) for a, b in zip(base, blend) ]



# W3C Softlight
def _gw3c(a):
    """Undocumented."""
    return ((16*a-12)*a+4)*a if a <= 0.25 else sqrt(a)

def _sftlt_w3c(a, b):
    """Undocumented."""
    if b <= 0.5:
        return a-(1-2*b)*a*(1-a)
    else:   
        return a+(2*b-1)*(_gw3c(a)-a)

@blend_function
def blend_softlight(base, blend):
    """Undocumented."""
    return [_sftlt_w3c(a,b) for a, b in zip(base, blend)] 



# Photoshop Softlight
def _sftlt_ps(a, b):
    """Undocumented."""
    if b < 0.5:
        return 2*a*b+a*a*(1-2*b)
    else:
        return 2*a*(1-b)+sqrt(a)*(2*b-1)

@blend_function
def blend_softlight_ps(base, blend):
    """Undocumented."""
    return [_sftlt_ps(a,b) for a, b in zip(base, blend)] 



# Pegtop Softlight 
# http://www.pegtop.net/delphi/articles/blendmodes/softlight.htm
def _sftlt_peg(a, b):
    """Undocumented."""
    return (1-2*b)*a*a + 2*b*a

@blend_function
def blend_softlight_peg(base, blend):
    """Undocumented."""
    return [_sftlt_peg(a,b) for a, b in zip(base, blend)] 




def _sftlt_ill(a, b):
    """Undocumented."""
    return a**(2**(2*0.5-b))

@blend_function
def blend_softlight_ill(base, blend):
    """Undocumented."""
    return [_sftlt_ill(a,b) for a, b in zip(base, blend)] 




@blend_function
def blend_add(base, blend):
    """Undocumented."""
    return [min(1.0, a+b) for a, b in zip(base, blend)]

blend_linear_dodge = blend_function(blend_add)
blend_plus_lighter = blend_function(blend_add)




@blend_function
def blend_plus_darker(base, blend):
    """Undocumented."""
    return [max(0.0, a+b-1) for a, b in zip(base, blend)]



@blend_function
def blend_subtract(base, blend):
    """Returns base - blend for each channel, clamping negative values to 0."""
    return [max(0.0, a-b) for a, b in zip(base, blend)]



@blend_function
def blend_difference(base, blend):
    """Returns the absolute value of base - blend for each channel."""
    return [abs(a-b) for a, b in zip(base, blend)]



@blend_function
def blend_darken(base, blend):
    """Returns the minimum value for each channel."""
    return [min(a,b) for a, b in zip(base, blend)]



@blend_function
def blend_lighten(base, blend):
    """Returns the mximum value for each channel."""
    return [max(a, b) for a, b in zip(base, blend)]



@blend_function
def blend_average(base, blend):
    """Returns the average value for each channel."""
    return [(a+b)/2.0 for a, b in zip(base, blend)]


#### The following come mostly from 
# http://www.pegtop.net/delphi/articles/blendmodes
# (some modifications may be included.)
@blend_function
def blend_negate(base, blend):
    """
    f(a, b) = 1-abs(1-a-b)
    """
    return [1-abs(1-a-b) for a, b in zip(base, blend)]



@blend_function
def blend_exclude(base, blend):
    """
    f(a,b) = a + b - 2ab
    """
    return [a+b-2*a*b for a, b in zip(base, blend)]


@blend_function
def blend_hardlight(base, blend):
    """
    f(a,b) =  2ab                     (b < 0.5)
              1 - 2(1 - a)(1 - b)     (b >= 0.5)
    """
    return [2*a*b if b < 0.5 else 1-2*(1-a)*(1-b) for a, b in zip(base, blend)]


@blend_function
def blend_colorburn(base, blend):
    """
    f(a,b) = max(0, 1 - (1 - a) / b)
    """
    return [ max(0,1-(1-a)/b) for a, b in zip(base, blend) ]


@blend_function
def blend_softburn(base, blend):
    """
    f(a,b) = 0.5 b / (1 - a)    (a + b < 1)
             1 - 0.5(1 - a) / b (a + b >= 1)
    """
    return [ clamp01(0.5*b/(1-a) if (a+b<1) else 1-0.5*(1-a)/b)
                for a, b in zip(base, blend)]

@blend_function
def blend_colordodge(base, blend):
    """
    f(a,b) = min(1.0, a / (1 - b))
    """
    return [ min(1.0, a/(1-b)) for a, b in zip(base, blend) ]

@blend_function
def blend_softdodge(base, blend):
    """
    f(a,b) =  0.5a / (1 - b) (for a + b < 1)
             1 - 0.5(1 - b) / a (else)
    """
    return blend_softburn(blend, base)

@blend_function
def blend_reflect(base, blend):
    """
    f(a,b) = a**2 / (1 - b)
    """
    return [ min(1.0, a**2/(1-b)) for a, b in zip(base, blend) ]

@blend_function
def blend_freeze(base, blend):
    """
    f(a,b) = 1 - (1 - a)**2 / b
    """
    return [ max(0.0, 1-(1-a)**2/b) for a, b in zip(base, blend) ]

@blend_function
def blend_stamp(base, blend):
    """
    f(a,b) = a + 2b - 1
    """
    return [clamp01( a + 2*b - 1 ) for a, b in zip(base, blend) ]

@blend_function
def blend_cosine(base, blend):
    """
    Was called "interpolate" in Pegtop.
    f(a,b) = ½ - ¼cos(pi*a) - ¼cos(pi*b)
    """
    return [ clamp01( 0.5 - 0.25*cos(pi*a) - 0.25*cos(pi*b) ) 
             for a, b in zip(base, blend)
           ]

@blend_function
def blend_xor_rgb8(base, blend):
    """
    Only intended for use with colors in rgb8. 
    """
    return[ a ^ b for a, b in zip(base, blend) ]

@blend_function
def blend_xor(base, blend):
    return bytes2norm(blend_xor_rgb8(norm2bytes(base),norm2bytes(blend)))

@blend_function
def blend_and_rgb8(base, blend):
    """
    Only intended for use with colors in rgb8. 
    """
    return[ a & b for a, b in zip(base, blend) ]

@blend_function
def blend_and(base, blend):
    return bytes2norm(blend_and_rgb8(norm2bytes(base),norm2bytes(blend)))

@blend_function
def blend_or_rgb8(base, blend):
    """
    Only intended for use with colors in rgb8. 
    """
    return[ a | b for a, b in zip(base, blend) ]

@blend_function
def blend_or(base, blend):
    return bytes2norm(blend_or_rgb8(norm2bytes(base),norm2bytes(blend)))
