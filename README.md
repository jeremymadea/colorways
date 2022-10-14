Colorways
=========

A Python library for procedural generation of color palettes, color 
manipulation, and color analysis.

Description
===========

This library aims to provide a wide variety of tools for creating,
changing, and sorting sets of colors. It might be found useful by
desighers, game developers, data visualizers, generative artists, and
other color monkeys. 

Its goal is to make it easy and fun to generate pleasing and/or
interesting color combinations. This is not a comprehensive set of
tools for color scientists; it isn't blazingly fast; and it doesn't
aspire to support every color space under the sun (and certainly not
under every CIE standard illuminant.)

It does provide tools to convert between a handful of colorspaces,
including RGB, HSL, HSV, HWB, and L\*a\*b\*. It also provides functions
for comparing colors (including several CIE distance measures and
WCAG color contrast), interpolating between colors, blending colors,
randomizing colors, and sorting colors. Finally, it provides a broad
selection of parameterized color palette generators.

Installation
============

    pip install colorways

Conventions
===========

To the extent possible, this library treats a 'color" generically,
as a list of three floats between 0 and 1 inclusive. It is up to the
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
is most often meant simply as a list of vec3s.

Many of the functions in this library, particularly some conversion 
functions, will attempt to determine whether an argument is a vec3 or a 
palette and perform the conversion on either the single color or the whole
palette.

**Important note:** some color spaces (e.g. L\*a\*b\*) are represented by
three floats that are outside the [0,1] range. While intepreting an
RGB palette as HSL might give an interesting result, interpreting a
L\*a\*b palette as HSL will likely result in an error. At times, the 
term 'vec3' might be used where it can also refer to a L\*a\*b\* value
or another 3-element list of numbers. Similarly, the term 'palette'
will sometimes be loosely used to describe a list of colors in
non-vec3 formats.


Modules
-------
* bezier:        Functions for bezier curve palettes.
* blend:         Functions for blending colors.
* conv:          Conversions between color spaces and representations.
* css:           CSS named colors.
* dist:          Color distance measures. 
* gen:           Palette and gradient generation functions.
* masterpalette: Provides the MasterPalette class and utilities.
* pals.\*:        Various predefined color palettes.
* sort:          Functions for sorting palettes by various criteria. 
* spectra.\*:     Various approximations of the visual spectrum. 
* theory:        Functions for traditional color theory palettes.
* util:          Utility functions.
* wcag:          Web Content Accessibility Guidelines color contrast.


Status Note
===========

My original work on this was lost in a disk crash. In all, I lost many hours of work and the git repo. The intial commit of this repo was from a tarball I created to share with one other developer who I sometimes collaborate with. 

Documentation is incomplete. There are, however, a bunch of jupyter notebooks in the demo_notebooks directory. These cover most of the library's functionality.

