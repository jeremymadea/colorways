from ..conv import hsl_to_hsv

"""This module contains utilities for Processing's Python mode."""

###  Functions in this module require the Processing environment.

def hsv_from_color(c):
    """Get a list of the HSV/HSB components from a processing color.

    Args:
        A Processing color object.

    Returns:
        A 3-element list (vec3) of the color argument's hue, 
        saturation, and value (i.e. brightness) components.
    """
    return [hue(c), saturation(c), brightness(c)]



def rgb_from_color(c):
    """Get a list of the RGB components from a processing color.
    
    Args:
        c: a Processing color object.

    Returns: 
        A 3-element list (vec3) of the color argument's red, green, 
        and blue components. 
    """
    return [red(c), green(c), blue(c)]



def get_color(palette, i, mode=None):
    """Retrieves a palette color as a Processing color object.

    Args:
        palette: a list of vec3 colors in HSL. 
        i: an index into the palette
        mode: a Processing color mode (RGB or HSB.) Default is HSB.

    Returns:
        A Processing color object.
    """
    if mode is None:
        vec3 = hsl_to_hsv(palette[i])
        return as_color_in_mode(vec3, HSB)
    return as_color_in_mode(palette[i], mode)
  


def as_color_in_mode(vec3, mode):
    """Converts a vec3 to a Processing color object.

    Args:
        vec3: a list containing 3 floats in the range [0,1]
        mode: a Processing color mode (either RGB or HSB)

    Returns:
        A Processing color object.
    """
    push()
    colorMode(mode, 1.0)
    c = color(*vec3)
    pop()
    return c
   
   
   
def as_hsb_color(vec3):
    """Converts a vec3 to a Processing color object in HSB mode.
    
    Args:
        vec3: a list containing 3 floats in the range [0,1]

    Retruns:
        A Processing color object.
    """ 
    return as_color_in_mode(vec3, HSB)

    
    
def as_rgb_color(vec3):
    """Converts a vec3 to a Processing color object in RGB mode.
    
    Args:
        vec3: a list containing 3 floats in the range [0,1]

    Retruns:
        A Processing color object.
    """
    return as_color_in_mode(vec3, RGB)



