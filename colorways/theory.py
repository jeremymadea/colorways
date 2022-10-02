from .internals import colpal_params_function, colpal_function
from .conv import rgb2hsl, hsl2rgb

"""This module provides functions for traditional color theory palettes."""

__all__ = [
    'complement',
    'hxx_complement',
    'hxx_triad',
    'hxx_analogous',
    'hxx_square',
    'hxx_complementary_pair',
    'split_palette',
    'tetradic_palette',
]

@colpal_function
def complement(base):
    """Returns the RGB complement of the color."""
    return [1.0-a for a in base]

@colpal_function
def hxx_complement(base):
    """Returns the Hxx complement of the color."""
    return [(base[0]+.5)%1, base[1], base[2]]

@colpal_function
def hxx_analogous(base):
    """Returns a 3-color analogous palette.""" 
    return [ 
        [(base[0] - (1/6.0))%1.0, base[1], base[2]],
        list(base),
        [(base[0] + (1/6.0))%1.0, base[1], base[2]]
    ]

@colpal_function
def hxx_triad(base):
    """Returns a triad palette."""
    return [ 
        [(base[0] - (1/3.0)) % 1.0, base[1], base[2]],
        list(base),
        [(base[0] - (2/3.0)) % 1.0, base[1], base[2]]
    ]
        

@colpal_function
def hxx_complementary_pair(base):
    """Returns a 2-color palette containing the base and its complement."""
    return [ list(base), [ (base[0] + 0.5) % 1.0, base[1], base[2] ]]



@colpal_function
def hxx_square(base):
    """
    Returns 4 color palette of the base color, and the base color with its 
    hue shifted 90, 180, and 270 degrees (or 0.25, 0.50, and 0.75 turns.) 
    """
    return [ list(base), 
             [ (base[0] + 0.25) % 1.0, base[1], base[2] ], 
             [ (base[0] + 0.50) % 1.0, base[1], base[2] ],
             [ (base[0] + 0.75) % 1.0, base[1], base[2] ]]



@colpal_params_function
def split_palette(base, angles):
    """
    Takes a base color or palette and a list of angles in [0, 1] turns.
    Base is assumed to be in an Hxx space. The last two channels are left 
    unchanged.
    """
    return [[(base[0]-a)%1.0, base[1], base[2]] for a in angles 
           ] + [list(base)] + [ 
            [(base[0]+a)%1.0, base[1], base[2]] for a in angles]


@colpal_params_function
def tetradic_palette(base, angle):
    """
    Takes a base color and an angle in [0, 1] turns. Base is assumed to be in
    Hxx space. A secondary base is specified by the angle from the base. The 
    returned palette consists of the base, its complement, the secondary base,
    and its complement. This scheme is otherwise known as a rectangular color 
    scheme.
    """
    return [
            list(base), 
            #rgb2hsl(complement(hsl2rgb(base))),  
            hxx_complement(base),  
            [(base[0]+angle)%1, base[1], base[2]], 
            [(base[0]+angle+.5)%1, base[1], base[2]] ]

