
"""
This module provides functions defined in the Web Content Accessibility 
Guidelines 2.0. 

Exports:
wcag_rel_lum(rgb): Computes a color's relative luminance.
wcag_contrast_ratio(rgb1, rgb2): Computes contrast ratio between colors.

"""

__all__ = ['wcag_rel_lum', 'wcag_contrast_ratio']


def wcag_rel_lum(rgb):
    """
    Computes the relative luminance (as defined by WCAG 2.0) of the given 
    vec3 interpreted as RGB.
    """
    # Computed according to:
    # https://www.w3.org/TR/WCAG20/#relativeluminancedef
    # This uses a different threshold value for each color channel (0.03928) 
    # than is used for the sRGB to XYZ conversion done by rgb2xyz(). 
    # (Relative luminance is the Y in XYZ.)
    #
    # if Cr <= 0.03928 then R = Cr/12.92 else R = ((Cr+0.055)/1.055) ^ 2.4
    trgb = [ c/12.92 if c <= 0.03928 else ((c+0.055)/1.055)**2.4 for c in rgb ]
    #L = 0.2126 * R + 0.7152 * G + 0.0722 * B
    return (0.2126 * trgb[0]) + (0.7152 * trgb[1]) + (0.0722 * trgb[2])

   
 
def wcag_contrast_ratio(rgb1, rgb2):
    """
    Computes the contrast ratio (as defined by WCAG 2.0) of the two given 
    vec3s interpreted as RGB values.
    """
    # https://www.w3.org/TR/WCAG20/#contrast-ratiodef
    # (L1 + 0.05) / (L2 + 0.05), where
    # L1 is the relative luminance of the lighter of the colors, and
    # L2 is the relative luminance of the darker of the colors.
    L1 = wcag_rel_lum(rgb1)
    L2 = wcag_rel_lum(rgb2)
    L1, L2 = max(L1, L2), min(L1, L2)
    return (L1 + 0.05) / (L2 + 0.05)



