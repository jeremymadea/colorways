from itertools import product
from random import random, choice, gammavariate, normalvariate
from math import pi, cos 
from .util import clamp01, reflect, lspace, hxx_lspace, randmix_vec3, randvec3_partial


"""
This module provides functions for generating palettes.

Exports:
    wave(t, freq=1.0, phase=0.0, offset=0.5, amp=0.5, fn=cos):
    wave_palette(n, fpoa, fn=cos):
    random_wave_palette(n):
    random_fpoa():
    golden_ratio_hsl_palette(n, hue, sat, lum):
    theory_hsl_palette(n, o1, o2, ra1, ra2, ra3), 
    harmony_hsl_palette(n, o1, o2, ra1, ra2, ra3,
    random_offset_palette(n, vec3, rng, map01fn=clamp01):
    value_offset_palette(n, vec3, rng, map01fn=clamp01):
    random_uniform_palette(n):
    random_walk(val, mindist, maxdist):
    random_walk_reflection(val, mindist, maxdist):
    random_walk_palette(n, vec3, minimum, maximum):
    random_walk_reflection_palette(n, vec3, minimum, maximum):
    randmix_palette(n, base, weight):
    randhue_palette(n, base):
    randred_palette = randhue_palette
    randsat_palette(n, base):
    randgreen_palette = randsat_palette
    randlum_palette(n, base):
    randblue_palette = randlum_palette
    randval_palette = randlum_palette
    randsatlum_palette(n, base):
    randgreenblue_palette = randsatlum_palette
    randsatval_palette = randsatlum_palette
    randhuesat_palette(n, base):
    randredgreen_palette = randhuesat_palette
    randhuelum_palette(n, base):
    randredblue_palette = randhuelum_palette
    randhueval_palette = randhuelum_palette
    gradient_palette(colors, steps): 
    hue_gradient_palette(colors, steps, bigarc=False): 
    perms_palette(pal)
    combo_palette(pal):
"""

__all__ = [
    'wave',
    'wave_fpoa_color',
    'wave_palette',
    'random_wave_palette',
    'random_fpoa',
    'golden_ratio_hsl_palette',
    'theory_hsl_palette',
    'harmony_hsl_palette',
    'random_offset_palette',
    'value_offset_palette',
    'random_uniform_palette',
    'random_walk',
    'random_walk_reflection',
    'random_walk_palette',
    'random_walk_reflection_palette',
    'randmix_palette',

    # Channel 1 
    'randhue_palette',
    'randred_palette',

    # Channel 2
    'randsat_palette',
    'randgreen_palette',
    'randwhite_palette',

    # Channel 3
    'randlum_palette',
    'randblue_palette',
    'randval_palette',
    'randblack_palette',

    # Channels 2 and 3
    'randsatlum_palette',
    'randgreenblue_palette',
    'randsatval_palette',
    'randwhiteblack_palette',

    # Channels 1 and 2
    'randhuesat_palette',
    'randredgreen_palette',
    'randhuelum_palette',
    'randhuewhite_palette',

    # Channels 1 and 3
    'randredblue_palette',
    'randhueval_palette',
    'randhueblack_palette',

    'gradient_palette',
    'hue_gradient_palette',

    # permutations palette
    'perms_palette',
    'combo_palette'
    
    ]


### Palette generation functions



def wave(t, freq=1.0, phase=0.0, offset=0.5, amp=0.5, fn=cos):
    """Undocumented"""
    return offset + amp * fn(2*pi * t*freq + phase)


# originally had (the equivalent of) : 
#   o + a * fn(pi*freq*t + pi*phase)
# Corrected to: 
#   o + a * fn(2*pi*freq*t + phase)




def wave_fpoa_color(t, fpoa, fn=cos, map01fn=clamp01):
    """Undocumented"""
    if map01fn is None:
        map01fn = lambda x: x
    return [
        map01fn(wave(t, *[arg[0] for arg in fpoa], fn=fn)),
        map01fn(wave(t, *[arg[1] for arg in fpoa], fn=fn)),
        map01fn(wave(t, *[arg[2] for arg in fpoa], fn=fn))]



def wave_palette(n, fpoa, fn=cos):
    """
    Generates a palette with sinusoid color channels.

    Args:
        n       number of colors in palette
        fpoa    Parameter list. See below.
        fn      Optional. sin or cos. Defaults to cos.  

    The fpoa parameter list is a structure like this:
        [[ frequency_red, frequency_green, frequency_blue ], 
         [ phase_red,     phase_green,     phase_blue     ], 
         [ offset_red,    offset_green,    offset_blue    ], 
         [ amplitude_red, amplitude_green, amplitude_blue ]]

    The equation is:

        offset + amplitude

    See Also:
        random_fpoa()

    """
    palette=[]
    for i in range(n):
        palette.append(wave_fpoa_color(i/n, fpoa, fn, clamp01))
    return palette



def random_wave_palette(n):
    """Generates a wave palette from random frequency, phase, offset and 
       amplitude parameters.

       Args:
           n: The number of colors in the return palette. 

       Returns:
           A palette. 
    """
    return wave_palette(n, random_fpoa())



def random_fpoa():
    """Generates random Frequency, Phase, Offset, and Amplitude parameters."""
    #fpoa = [[1.0, 1.0, 1.0], # Frequency  f: 0 < f (favor near 1, > 0.5, < 4)
    #        [0.0, 0.0, 0.0], # Phase:     p: 0 <= p <= 1
    #        [0.5, 0.5, 0.5], # Offset:    o: -a < o < a+1
    #        [0.5, 0.5, 0.5]] # Amplitude: a: 0 < a (favor near .5)

    f = [0.5+gammavariate(1.5,.5) for _ in range(3)]
    p = [random() for _ in range(3)]
    a = [normalvariate(0.5,.09) for _ in range(3)]
    o = [-a[i] + normalvariate((2*a[i]+1)/2, (2*a[i]+1)/7) for i in range(3)]

    return [f, p, o, a]



def golden_ratio_hsl_palette(n, hue=random(), sat=.5, lum=.5):
    """Undocumented"""
    palette = []
    phi = 0.6180339887498948482
    #hue = random()
    for i in range(n):
        palette.append([ hue, sat, lum ])
        hue += phi
        hue %= 1.0
    return palette



def theory_hsl_palette(n, o1, o2, ra1, ra2, ra3, 
                        sat=0.5, satrange=0.5, lum=0.5, lumrange=0.5, 
                        randsat=False, randlum=False, refang=None):
    """Undocumented"""
    palette = []
    if refang is None:
        ref = random() * 360.0
    else:
        ref = refang
    for i in range(n):
        ang = i/n * (ra1 + ra2 + ra3) 
        if ang < ra1:
            ang -= (ra1/2.0)
        elif ang < ra1 + ra2:
            ang += o1 - ra2
        else:
            ang += o2 - ra3
        new_sat, new_lum = sat, lum
        if randsat:
            new_sat = reflect(sat + (random() - 0.5) * satrange)
        if randlum:
            new_lum = reflect(lum + (random() - 0.5) * lumrange)
        palette.append( [((ref + ang)/360.0) % 1.0, new_sat, new_lum] )
    return palette



def harmony_hsl_palette(n, o1, o2, ra1, ra2, ra3,
                        sat=0.5, satrange=0.5, lum=0.5, lumrange=0.5, refang=None):
    """Undocumented"""
    palette = []
    if refang is None:
        ref = random() * 360.0
    else:
        ref = refang
    for i in range(n):
        rand = random() * (ra1 + ra2 + ra3)
        if rand < ra1:
            rand -= (ra1/2.0)
        elif rand < ra1 + ra2:
            rand += o1 - ra2
        else:
            rand += o2 - ra3
        new_sat = sat + (random() - 0.5) * satrange
        new_lum = lum + (random() - 0.5) * lumrange
        palette.append( [((ref + rand)/360.0) % 1.0, new_sat, new_lum] )
    return palette



def random_offset_palette(n, vec3, rng, map01fn=clamp01):
    """Undocumented"""
    if map01fn is None:
        map01fn = lambda x: x
    palette = [vec3]
    for i in range(n-1):
        new = list(vec3)
        new[0] = map01fn(new[0] + random() * 2 * rng - rng)
        new[1] = map01fn(new[1] + random() * 2 * rng - rng)
        new[2] = map01fn(new[2] + random() * 2 * rng - rng)
        palette.append(new)
    return palette



def value_offset_palette(n, vec3, rng, map01fn=clamp01):
    """Undocumented"""
    if map01fn is None:
        map01fn = lambda x: x
    palette = [vec3]
    for i in range(n-1):
        val = sum(vec3)/3
        new = val + 2*random() * rng - rng
        ratio = new/val
        palette.append([map01fn(c * ratio) for c in vec3])
    return palette



def random_uniform_palette(n):
    """Undocumented"""
    return random_offset_palette(n, [0.5, 0.5, 0.5], 0.5)



def random_walk(val, mindist, maxdist):
    """Undocumented"""
    return val + choice([-1, 1]) * (mindist + random()  * (maxdist - mindist))



def random_walk_reflection(val, mindist, maxdist):
    """Undocumented"""
    return reflect(val + choice([-1, 1]) * (mindist + random()  * (maxdist - mindist)))    



def random_walk_palette(n, vec3, minimum, maximum):
    """Undocumented"""
    palette = [vec3]
    #new = vec3
    for i in range(n-1):
        new = list(vec3)
        new[0] = random_walk(new[0], minimum, maximum) % 1
        new[1] = random_walk(new[1], minimum, maximum) % 1
        new[2] = random_walk(new[2], minimum, maximum) % 1
        palette.append(new)
    return palette



def random_walk_reflection_palette(n, vec3, minimum, maximum):
    """Undocumented"""
    palette = [vec3]
    #new = list(vec3)
    for i in range(n-1):
        new = list(vec3)
        new[0] = random_walk_reflection(new[0], minimum, maximum)
        new[1] = random_walk_reflection(new[1], minimum, maximum)
        new[2] = random_walk_reflection(new[2], minimum, maximum)
        palette.append(new)
    return palette



def randmix_palette(n, base, weight):
    """Undocumented"""
    palette = [base]
    for i in range(n-1):
        palette.append(randmix_vec3(base, weight))
    return palette



def randhue_palette(n, base):
    """Undocumented"""
    palette = [base]
    for _ in range(n-1):
        palette.append(randvec3_partial( [None, base[1], base[2]]))
    return palette

randred_palette = randhue_palette



def randsat_palette(n, base):
    """Undocumented"""
    palette = [base]
    for _ in range(n-1):
        palette.append(randvec3_partial([base[0], None, base[2]]))
    return palette

randgreen_palette = randsat_palette
randwhite_palette = randsat_palette


def randlum_palette(n, base):
    """Undocumented"""
    palette = [base]
    for _ in range(n-1):
        palette.append(randvec3_partial([base[0], base[1], None]))
    return palette

randblue_palette = randlum_palette
randval_palette = randlum_palette
randblack_palette = randlum_palette


def randsatlum_palette(n, base):
    """Undocumented"""
    palette = [base]
    for _ in range(n-1):
        palette.append(randvec3_partial([base[0], None, None]))
    return palette

randgreenblue_palette = randsatlum_palette
randsatval_palette = randsatlum_palette
randwhiteblack_palette = randsatlum_palette


def randhuesat_palette(n, base):
    """Undocumented"""
    palette = [base]
    for _ in range(n-1):
        palette.append(randvec3_partial([None, None, base[2]]))
    return palette

randredgreen_palette = randhuesat_palette
randhuewhite_palette = randhuesat_palette

def randhuelum_palette(n, base):
    """Undocumented"""
    palette = [base]
    for _ in range(n-1):
        palette.append(randvec3_partial([None, base[1], None]))
    return palette

randredblue_palette = randhuelum_palette
randhueval_palette = randhuelum_palette
randhueblack_palette = randhuelum_palette

# Linear interpolated (gradient) palettes

def gradient_palette(colors, steps): 
    """Undocumented"""
    if len(colors) < 2: 
        raise ValueError('gradient_palette: colors must be a list of length 2 or more.')
    if type(steps) != list:
        steps = [steps] * (len(colors)-1)
    ret = lspace(colors[0], colors[1], steps[0])
    for i in range(1, len(colors)-1):
        # Avoid duplicating colors by slicing off the first, but keep length 
        # as expected by adding one to the steps.
        ret += lspace(colors[i], colors[i+1], steps[i]+1)[1:]
    return ret



def hue_gradient_palette(colors, steps, bigarc=False): 
    """Undocumented"""
    if len(colors) < 2: 
        raise ValueError('gradient_palette: colors must be a list of length 2 or more.')
    if type(steps) != list:
        steps = [steps] * (len(colors)-1)
    ret = hxx_lspace(colors[0], colors[1], steps[0], bigarc)
    for i in range(1, len(colors)-1):
        # Avoid duplicating colors by slicing off the first, but keep length 
        # as expected by adding one to the steps.
        ret += hxx_lspace(colors[i], colors[i+1], steps[i]+1, bigarc)[1:]
    return ret

def perms_with_replace(n,k):
    return product(range(n), repeat=k)

def perms_palette(pal):
    return [[ pal[p[0]][0], 
              pal[p[1]][1], 
              pal[p[2]][2] ] for p in perms_with_replace(len(pal),3)]

def combo_palette(pal):
    if len(pal) > 1:
        vals = [ *pal[0], *pal[1] ]
    else:
        vals = [ *pal[0] ]
    return [[ vals[p[0]], 
              vals[p[1]], 
              vals[p[2]]  ] for p in perms_with_replace(len(vals),3)] 




