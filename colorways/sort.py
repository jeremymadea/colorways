from .dist import rgb_euclidean, hsl_euclidean, hsv_euclidean, cie76, cie94, ciede2000

from .conv import ( 
    hsl2hsv, hsl2lab, hsl2rgb,
    hsv2hsl, hsv2lab, hsv2rgb,
    rgb2hsl, rgb2hsv, rgb2lab,
)


"""
    sort_palette_by_chan(pal, chan)

    sort_palette_by_chan0(pal): Returns a new palette sorted channel 0. 
    These are aliases for sort_palette_by_chan0:
        sort_palette_by_r
        sort_rgb_palette_by_r
        sort_palette_by_h
        sort_hsv_palette_by_hue
        sort_hsl_palette_by_hue

    sort_palette_by_chan1(pal): Returns a new palette sorted channel 1. 
    These are aliases for sort_palette_by_chan1:
        sort_palette_by_g
        sort_rgb_palette_by_g
        sort_palette_by_s
        sort_hsv_palette_by_sat
        sort_hsl_palette_by_sat

    sort_palette_by_chan2(pal): Returns a new palette sorted channel 2. 
    These are aliases for sort_palette_by_chan2:
        sort_palette_by_b
        sort_rgb_palette_by_b
        sort_palette_by_l
        sort_palette_by_v
        sort_hsv_palette_by_val
        sort_hsl_palette_by_lum

    sort_rgb_palette_by_hue(pal):
    sort_rgb_palette_by_sat(pal):
    sort_rgb_palette_by_val(pal):
    sort_rgb_palette_by_lum(pal):


    sort_hsv_palette_by_lum(pal):
    sort_hsv_palette_by_r(pal):
    sort_hsv_palette_by_g(pal):
    sort_hsv_palette_by_b(pal):    


    sort_hsl_palette_by_val(pal):
    sort_hsl_palette_by_r(pal):
    sort_hsl_palette_by_g(pal):
    sort_hsl_palette_by_b(pal):
    sort_rgb_palette_by_cie76_from(pal, rgb):
    sort_rgb_palette_by_cie94_from(pal, rgb):
    sort_rgb_palette_by_ciede2000_from(pal, rgb):
    sort_rgb_palette_by_rgb_euclidean_from(pal, rgb):
    sort_rgb_palette_by_hsv_euclidean_from(pal, rgb):
    sort_rgb_palette_by_hsl_euclidean_from(pal, rgb):
    sort_hsv_palette_by_cie76_from(pal, hsv):
    sort_hsv_palette_by_cie94_from(pal, hsv):
    sort_hsv_palette_by_ciede2000_from(pal, hsv):
    sort_hsv_palette_by_hsv_euclidean_from(pal, hsv):
    sort_hsl_palette_by_cie76_from(pal, hsl):
    sort_hsl_palette_by_cie94_from(pal, hsl):
    sort_hsl_palette_by_ciede2000_from(pal, hsl):
    sort_hsl_palette_by_hsl_euclidean_from(pal, hsl):
"""

__all__ = [
    'sort_palette_by_chan',
    'sort_palette_by_chan0',
    'sort_palette_by_r',
    'sort_palette_by_h',
    'sort_palette_by_chan1',
    'sort_palette_by_g',
    'sort_palette_by_s',
    'sort_palette_by_chan2',
    'sort_palette_by_b',
    'sort_palette_by_l',
    'sort_palette_by_v',
    'sort_rgb_palette_by_r',
    'sort_rgb_palette_by_g',
    'sort_rgb_palette_by_b',
    'sort_rgb_palette_by_hue',
    'sort_rgb_palette_by_sat',
    'sort_rgb_palette_by_val',
    'sort_rgb_palette_by_lum',
    'sort_hsv_palette_by_hue',
    'sort_hsv_palette_by_sat',
    'sort_hsv_palette_by_val',
    'sort_hsv_palette_by_lum',
    'sort_hsv_palette_by_r',
    'sort_hsv_palette_by_g',
    'sort_hsv_palette_by_b',
    'sort_hsl_palette_by_hue',
    'sort_hsl_palette_by_sat',
    'sort_hsl_palette_by_lum',
    'sort_hsl_palette_by_val',
    'sort_hsl_palette_by_r',
    'sort_hsl_palette_by_g',
    'sort_hsl_palette_by_b',
    'sort_rgb_palette_by_cie76_from',
    'sort_rgb_palette_by_cie94_from',
    'sort_rgb_palette_by_ciede2000_from',
    'sort_rgb_palette_by_rgb_euclidean_from',
    'sort_rgb_palette_by_hsv_euclidean_from',
    'sort_rgb_palette_by_hsl_euclidean_from',
    'sort_hsv_palette_by_cie76_from',
    'sort_hsv_palette_by_cie94_from',
    'sort_hsv_palette_by_ciede2000_from',
    'sort_hsv_palette_by_hsv_euclidean_from',
    'sort_hsl_palette_by_cie76_from',
    'sort_hsl_palette_by_cie94_from',
    'sort_hsl_palette_by_ciede2000_from',
    'sort_hsl_palette_by_hsl_euclidean_from',
    ]

### Palette sorting functions. 

def sort_palette_by_chan(pal, chan):
    """Undocumented"""
    return sorted(pal, key=lambda c: c[chan])


def sort_palette_by_chan0(pal):
    return sorted(pal, key=lambda c: c[0])


# Aliases for sorting channel 0
sort_palette_by_r = sort_palette_by_chan0
sort_palette_by_h = sort_palette_by_chan0


def sort_palette_by_chan1(pal):
    return sorted(pal, key=lambda c: c[1])


# Aliases for sorting channel 1
sort_palette_by_g = sort_palette_by_chan1
sort_palette_by_s = sort_palette_by_chan1


def sort_palette_by_chan2(pal):
    return sorted(pal, key=lambda c: c[2])


# Aliases for sorting channel 2
sort_palette_by_b = sort_palette_by_chan2
sort_palette_by_l = sort_palette_by_chan2
sort_palette_by_v = sort_palette_by_chan2

sort_rgb_palette_by_r = sort_palette_by_r
sort_rgb_palette_by_g = sort_palette_by_g
sort_rgb_palette_by_b = sort_palette_by_b


def sort_rgb_palette_by_hue(pal):
    """Undocumented"""
    return sorted(pal, key=lambda c: rgb2hsl(c)[0])


def sort_rgb_palette_by_sat(pal):
    """Undocumented"""
    return sorted(pal, key=lambda c: rgb2hsl(c)[1])


def sort_rgb_palette_by_val(pal):
    """Undocumented"""
    return sorted(pal, key=lambda c: rgb2hsv(c)[2])


def sort_rgb_palette_by_lum(pal):
    """Undocumented"""
    return sorted(pal, key=lambda c: rgb2hsl(c)[2])


sort_hsv_palette_by_hue = sort_palette_by_h
sort_hsv_palette_by_sat = sort_palette_by_s
sort_hsv_palette_by_val = sort_palette_by_v

    
def sort_hsv_palette_by_lum(pal):
    """Undocumented"""
    return sorted(pal, key=lambda c: hsv2hsl(c)[2]) 

    
def sort_hsv_palette_by_r(pal):
    """Undocumented"""
    return sorted(pal, key=lambda c: hsv2rgb(c)[0])

    
def sort_hsv_palette_by_g(pal):
    """Undocumented"""
    return sorted(pal, key=lambda c: hsv2rgb(c)[1])

    
def sort_hsv_palette_by_b(pal):    
    """Undocumented"""
    return sorted(pal, key=lambda c: hsv2rgb(c)[2])


sort_hsl_palette_by_hue = sort_palette_by_h
sort_hsl_palette_by_sat = sort_palette_by_s
sort_hsl_palette_by_lum = sort_palette_by_l


def sort_hsl_palette_by_val(pal):
    """Undocumented"""
    return sorted(pal, key=lambda c: hsl2hsv(c)[2])


def sort_hsl_palette_by_r(pal):
    """Undocumented"""
    return sorted(pal, key=lambda c: hsl2rgb(c)[0])


def sort_hsl_palette_by_g(pal):
    """Undocumented"""
    return sorted(pal, key=lambda c: hsl2rgb(c)[1])


def sort_hsl_palette_by_b(pal):
    """Undocumented"""
    return sorted(pal, key=lambda c: hsl2rgb(c)[2])


def _palette_distances(pal, vec3, distfunc=ciede2000):
    """Undocumented"""
    distances = []
    for i, v in enumerate(pal):
        distances.append((i, distfunc(vec3, v)))
    return distances


def sort_rgb_palette_by_cie76_from(pal, rgb):
    """Undocumented"""
    labpal = rgb2lab(pal)
    lab = rgb2lab(rgb)
    d_list = _palette_distances(labpal, lab, cie76)
    return [ list(pal[t[0]]) for t in sorted(d_list, key=lambda t: t[1]) ]


def sort_rgb_palette_by_cie94_from(pal, rgb):
    """Undocumented"""
    labpal = rgb2lab(pal)
    lab = rgb2lab(rgb)
    d_list = _palette_distances(labpal, lab, cie94)
    return [ list(pal[t[0]]) for t in sorted(d_list, key=lambda t: t[1]) ]


def sort_rgb_palette_by_ciede2000_from(pal, rgb):
    """Undocumented"""
    labpal = rgb2lab(pal)
    lab = rgb2lab(rgb)
    d_list = _palette_distances(labpal, lab, ciede2000)
    return [ list(pal[t[0]]) for t in sorted(d_list, key=lambda t: t[1]) ]


def sort_rgb_palette_by_rgb_euclidean_from(pal, rgb):
    """Undocumented"""
    d_list = _palette_distances(pal, rgb, rgb_euclidean) 
    return [ list(pal[t[0]]) for t in sorted(d_list, key=lambda t: t[1]) ]


def sort_rgb_palette_by_hsv_euclidean_from(pal, rgb):
    """Undocumented"""
    hsvpal = rgb2hsv(pal)
    hsv = rgb2hsv(rgb)
    d_list = _palette_distances(hsvpal, hsv, hsv_euclidean) 
    return [ list(pal[t[0]]) for t in sorted(d_list, key=lambda t: t[1]) ]


def sort_rgb_palette_by_hsl_euclidean_from(pal, rgb):
    """Undocumented"""
    hslpal = rgb2hsl(pal)
    hsl = rgb2hsl(rgb)
    d_list = _palette_distances(hslpal, hsl, hsl_euclidean) 
    return [ list(pal[t[0]]) for t in sorted(d_list, key=lambda t: t[1]) ]
    
   
def sort_hsv_palette_by_cie76_from(pal, hsv):
    """Undocumented"""
    labpal = hsv2lab(pal)
    lab = hsv2lab(hsv)
    d_list = _palette_distances(labpal, lab, cie76)
    return [ list(pal[t[0]]) for t in sorted(d_list, key=lambda t: t[1]) ]


def sort_hsv_palette_by_cie94_from(pal, hsv):
    """Undocumented"""
    labpal = hsv2lab(pal)
    lab = hsv2lab(hsv)
    d_list = _palette_distances(labpal, lab, cie94)
    return [ list(pal[t[0]]) for t in sorted(d_list, key=lambda t: t[1]) ]


def sort_hsv_palette_by_ciede2000_from(pal, hsv):
    """Undocumented"""
    labpal = hsv2lab(pal)
    lab = hsv2lab(hsv)
    d_list = _palette_distances(labpal, lab, ciede2000)
    return [ list(pal[t[0]]) for t in sorted(d_list, key=lambda t: t[1]) ]


def sort_hsv_palette_by_hsv_euclidean_from(pal, hsv):
    """Undocumented"""
    d_list = _palette_distances(pal, hsv, hsv_euclidean) 
    return [ list(pal[t[0]]) for t in sorted(d_list, key=lambda t: t[1]) ]


def sort_hsl_palette_by_cie76_from(pal, hsl):
    """Undocumented"""
    labpal = hsl2lab(pal)
    lab = hsl2lab(hsl)
    d_list = _palette_distances(labpal, lab, cie76)
    return [ list(pal[t[0]]) for t in sorted(d_list, key=lambda t: t[1]) ]


def sort_hsl_palette_by_cie94_from(pal, hsl):
    """Undocumented"""
    labpal = hsl2lab(pal)
    lab = hsl2lab(hsl)
    d_list = _palette_distances(labpal, lab, cie94)
    return [ list(pal[t[0]]) for t in sorted(d_list, key=lambda t: t[1]) ]


def sort_hsl_palette_by_ciede2000_from(pal, hsl):
    """Undocumented"""
    labpal = hsl2lab(pal)
    lab = hsl2lab(hsl)
    d_list = _palette_distances(labpal, lab, ciede2000)
    return [ list(pal[t[0]]) for t in sorted(d_list, key=lambda t: t[1]) ]


def sort_hsl_palette_by_hsl_euclidean_from(pal, hsl):
    """Undocumented"""
    d_list = _palette_distances(pal, hsl, hsl_euclidean) 
    return [ list(pal[t[0]]) for t in sorted(d_list, key=lambda t: t[1]) ]


