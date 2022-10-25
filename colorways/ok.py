# See https://bottosson.github.io/

from .util import cbrt
from .conv import lab2lch, lch2lab
"""
Okla colorspace functions. 
"""

__all__ = [
    'xyz2oklab',
    'oklab2xyz',
    'lsrgb2oklab', 
    'oklab2lsrgb', 
    'oklab2oklch',
    'oklch2oklab',

]

oklab2oklch = lab2lch
oklch2oklab = lch2lab

def xyz2oklab(xyz):
    (x,y,z) = xyz
    l = 0.8189330101 * x + 0.3618667424 * y - 0.1288597137 * z
    m = 0.0329845436 * x + 0.9293118715 * y + 0.0361456387 * z
    s = 0.0482003018 * x + 0.2643662691 * y + 0.6338517070 * z
    ll = cbrt(l)
    mm = cbrt(m)
    ss = cbrt(s)
    return [ 
        0.2104542553 * ll + 0.7936177850 * mm - 0.0040720468 * ss,
        1.9779984951 * ll - 2.4285922050 * mm + 0.4505937099 * ss,
        0.0259040371 * ll + 0.7827717662 * mm - 0.8086757660 * ss
    ]
 
def oklab2xyz(lab):
    (L,a,b) = lab

    ll = 1.         * L + 0.39633779 * a + 0.21580376 * b
    mm = 1.00000001 * L - 0.10556134 * a - 0.06385417 * b
    ss = 1.00000005 * L - 0.08948418 * a - 1.29148554 * b
    l = ll ** 3
    m = mm ** 3
    s = ss ** 3
    
    return [
         1.22701385 * l - 0.55779998 * m + 0.28125615 * s
        -0.04058018 * l + 1.11225687 * m - 0.07167668 * s
        -0.07638128 * l - 0.42148198 * m + 1.58616322 * s
    ]


def lsrgb2oklab(rgb):
    (r, g, b) = rgb
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    ll = cbrt(l)
    mm = cbrt(m)
    ss = cbrt(s)
    return [
        0.2104542553 * ll + 0.7936177850 * mm - 0.0040720468 * ss,
        1.9779984951 * ll - 2.4285922050 * mm + 0.4505937099 * ss,
        0.0259040371 * ll + 0.7827717662 * mm - 0.8086757660 * ss,
    ]

def oklab2lsrgb(lab):
    (L,a,b) = lab
    ll = L + 0.3963377774 * a + 0.2158037573 * b
    mm = L - 0.1055613458 * a - 0.0638541728 * b
    ss = L - 0.0894841775 * a - 1.2914855480 * b
    l = ll ** 3
    m = mm ** 3
    s = ss ** 3
    return [
         4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
        -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
        -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s,
    ]

