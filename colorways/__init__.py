from .conv import * 
from .dist import *
from .gen import * 
from .sort import * 
from .util import *
from .wcag import * 

"""Colorways facilitates procedural color palette and gradient generation.

Description:

    This library aims to provide a wide variety of tools for creating,
    changing, and sorting sets of colors. It might be found useful by
    desighers, game developers, data visualizers, gneerative artists, and
    other color monkeys. 

    Its goal is to make it easy and fun to generate pleasing and/or
    interesting color combinations. This is not a comprehensive set of
    tools for color scientists; it isn't blazingly fast; and it doesn't
    aspire to support every color space under the sun (and certainly not
    under every CIE standard illuminant.)

    It does provide tools to convert between a handful of colorspaces,
    including RGB, HSL, HSV, HWB, and L*a*b*. It also provides functions
    for comparing colors (including several CIE distance mesures and
    WCAG color contrast), interpolating between colors, blending colors,
    randomizing colors, and sorting colors. Finally, it provides a
    selection of parameterized color palette generators.

Conventions:

    To the extent possible, this library treats a 'color" generically,
    as a list of three floats between 0 and 1 inclusive.** It is up to the
    programmer to remember (or decide) whether 

        color = [0.0, 1.0, 0.5] 
    
    is 'springgreen', 'red', 'maroon', (the CSS name for that color
    point in RGB, HSL, or HSV space respectively) or a middlish gray
    color (as that point would appear as an HWB color.) Throughout this library
    a generic color value like this is often referred to as a 'vec3'. 

    Support is provided for conversion to and from some popular external
    formats, such as lists of 3 bytes (i.e. integers in the range 0 to
    255 inclusive), hexadecimal strings, and CSS keywords.

    Similar to the convention of using generic vec3s for colors, a 'palette' 
    is most often meant simply as a list of vec3s.** Many of the 

    Many of the functions in this library, particularly some conversion 
    functions, will attempt to determine whether an argument is a vec3 or a 
    palette and perform the connversion on either the single color or the whole
    palette.

^^^^^^^^^^^^^^^^^

    ** Important note: some color spaces (e.g. L*a*b*) are represented by
    three floats that are outside the [0,1] range. While intepretting an
    RGB palette as HSL might give an interesting result, interpreting a
    L*a*b palette as HSL will likely result in an error. At times, the 
    term 'vec3' might be used where it can also refer to a L*a*b* value
    or another 3-element list of numbers. Similarly, the term 'palette'
    will sometimes be loosely used to describe a list of colors in
    non-vec3 formats.


    Modules:
        bezier  Functions for bezier curve palettes.
        blend   Functions for blending colors.
        conv    Conversions between color spaces and representations.
        css     CSS named colors.
        gen     Various palette and gradient generation functions.
        dist    Color distance measures. 
        p3      Utilities for Processing's Python mode
        palettes    Some predefined palettes.
        ryb     RYB color space conversions.
        spectra Various approximations of the visible spectrum.
        sort:   Routines for sorting palettes by various criteria. 
        theory  Functions for traditional color theory palettes. 
        vars    Some color variables. These differ from CSS keywords.
        util:   Utility functions.
        wcag:   Web Content Accessibility Guidelines color contrast.
        masterpalette: Provides the MasterPalette class and utilities.

"""


