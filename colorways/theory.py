from .internals import colpal_params_function, colpal_function

__all__ = [
    'complement',
    'hxx_triad',
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
def hxx_triad(base):
    return [ 
        [(base[0] - (1/3.0)) % 1.0, base[1], base[2]],
        list(base),
        [(base[0] - (2/3.0)) % 1.0, base[1], base[2]]
    ]
        

@colpal_function
def hxx_complementary_pair(base):
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
def tetradic_palette(base, angles):
    """
    Undocumented.
    """
    return [[(base[0]-a+.5)%1.0, base[1], base[2]] for a in angles 
           ] + [list(base)] + [ 
            [(base[0]+a)%1.0, base[1], base[2]] for a in angles]

