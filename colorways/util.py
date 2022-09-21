from random import random

"""
This module provides miscellaneous utility functions.

Exports:
    Functions for range limiting:
        reflect(x)
        clamp01(x)

    Validation functions:
        is_vec(arg, check_min=None, check_max=None, check_len=None, min_len=None, max_len=None, ok_types=(float,int))
        is_pal01(arg)
        is_pal(arg)
        is_byte_pal(arg)

    Linear interpolation utils: 
        lspace(u, v, n=2)
        circ_lspace(a, b, n=2, bigarc=False)
        hxx_lspace(u, v, n, bigarc=False)

    Palette modification utils:
        apply_to_chans(vec3, chans, fn, *args, **kwargs)
        modify_palette(pal, chans, fn, *args, **kwargs)

    Vec3 utils:
        randvec3()
        randvec3mono()
        randvec3_partial(vec3)
        mix_vec3(base, mixin, weight)
        randmix_vec3(base, weight)
"""

__all__ = [
    'reflect', 'clamp01',
    'is_vec', 'is_pal01', 'is_pal', 'is_byte_pal',
    'lspace', 'circ_lspace', 'hxx_lspace', 'fspace',
    'apply_to_chans', 'modify_palette',
    'randvec3', 'randvec3mono', 'randvec3_partial', 'mix_vec3', 'randmix_vec3',
    ]


### General utilities 

def reflect(x):
    """
    Maps x onto [0,1], treating x as a distance to "walk"
    back and forth across the interval starting at 0.
    """
    r = abs(x) % 2
    return r if r < 1 else 2-r


def clamp01(x):
    """
    Returns 0 if x is less than 0, 1 if x is greater than 1, and x otherwise.
    """
    return min(max(0.0, x), 1.0)


### Validation utilities.

def is_vec(arg, check_min=None, check_max=None, check_len=None,
           min_len=None, max_len=None, ok_types=(float,int)):
    if type(arg) is not list: return False
    if check_len is not None and check_len != len(arg): return False
    if min_len is not None and min_len > len(arg): return False
    if max_len is not None and max_len < len(arg): return False
    if not all( type(e) in ok_types for e in arg ): return False
    if check_min is not None and check_min > min(arg): return False
    if check_max is not None and check_max < max(arg): return False
    return True

def is_pal01(arg):
    if type(arg) is not list: return False
    return all(
        is_vec(e, min_len=3, check_min=0, check_max=1) for e in arg)

def is_pal(arg):
    if type(arg) is not list: return False
    return all( is_vec(e, min_len=3) for e in arg)

def is_byte_pal(arg, require_ints=False):
    if type(arg) is not list: return False
    if require_ints:
        return all( is_vec(
                e, min_len=3, check_min=0, check_max=255, ok_types=(int,)
            ) for e in arg)
    else:
        return all( is_vec(
                e, min_len=3, check_min=0, check_max=255
            ) for e in arg)

      


# Linear interpolation utils

def _lerp(a, b, t):
    """Undocumented"""
    return a + t*(b-a)



def lspace(u, v, n=2):
    """Undocumented"""
    if n < 2: n = 2
    ret = []
    if type(u) == type(v) == list:
        dims = min(len(u), len(v))
        for i in range(n): 
            ret.append([u[d] + i/(n-1)*(v[d]-u[d]) for d in range(dims)])
        return ret
    else:
        return lspace([u], [v], n)

def fspace(u, v, n=2, fn=None):
    """Undocumented"""
    if fn is None:
        fn = lambda x: x
    if n < 2: n = 2
    return [ fn(e) for e in lspace(u, v, n) ]


def circ_lspace(a, b, n, bigarc=False):
    """Undocumented"""
    d1 = abs(a-b)
    d2 = 1 - abs(a-b)
    if (0 < d2 < d1 and not bigarc) or (0 < d1 < d2 and bigarc):
        deltas = [e[0] for e in lspace([0], [d2], n)]
        if a < b: 
            return [(1 + (a-d))%1 for d in deltas]
        else: 
            return [(a+d)%1 for d in deltas]
    else: 
        return [e[0] for e in lspace([a], [b], n)]



def hxx_lspace(u, v, n, bigarc=False): 
    h_chan = circ_lspace(u[0], v[0], n, bigarc)
    xx_chans = lspace(u[1:], v[1:], n)
    return [ [h_chan[i]] + xx for i, xx in enumerate(xx_chans) ]
    
   


# Palette modification


def apply_to_chans(vec3, chans, fn, *args, **kwargs):
    """Undocumented"""
    new = []
    if type(chans) is int:
        chans = [chans]
    L = len(vec3) # because maybe it isn't a vec3.
    for i in range(L):
        if i in chans:
            new.append( fn(vec3[i], *args, **kwargs))
        else:
            new.append(vec3[i])
    return new


def modify_palette(pal, chans, fn, *args, **kwargs):
    """Undocumented"""
    new = []
    n = len(pal)
    for i, v in enumerate(pal): 
        new.append(apply_to_chans(v, chans, fn, i, n, *args, **kwargs))
    return new 


# Vec3 utils

def _rand_norm_byte():
    return 255*random()/255.0

def random_color():
    return [ _rand_norm_byte() for _ in range(3) ]

def random_gray():
    return [ _rand_norm_byte() ] * 3

def rand_color_partial(vec3):
    return [ rand_color() if c is None else c for c in vec3 ]

def randvec3():
    """Returns a list of three random floats in [0,1]."""
    return [ random() for _ in range(3) ]

def randvec3mono():
    """Returns a list containing a random float in [0,1] repeated 3 times."""
    return [ random() ] * 3   

def randvec3_partial(vec3):
    """
    Returns a copy of the given list with None elements replaced with random
    floats in the range [0,1].
    """
    return [ random() if c is None else c for c in vec3 ]

def mix_vec3(base, mixin, weight):
    """
    Takes a base vec3, a mixin vec3, and a weight and returns a vec3 whose 
    components are a weighted average of the given vec3s (weighted towards 
    the base.)
    """
    return [ weight*base[i] + (1-weight)*mixin[i] for i in range(len(base)) ]



def randmix_vec3(base, weight):
    """
    Takes a base vec3 and a weight and returns a vec3 whose components are the 
    weighted average of the base and a random vec3 (weighted towards the base.)
    """
    return mix_vec3(base, randvec3(), weight)



