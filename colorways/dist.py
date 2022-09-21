from math import pi, sqrt, sin, cos, exp, atan2

"""
This module provides functions for computing various distance measures 
between colors.

Exports:
    rgb_euclidean(rgb1, rgb2): Computes euclidean distance in RGB space.
    hsv_euclidean(hsv1, hsv2): Computes euclidean distance in HSV space.
    hsl_euclidean(hsl1, hsl2): Computes euclidean distance in HSL space. 
    hwb_euclidean(hsl1, hsl2): Computes euclidean distance in HWB space. 
    cie76(lab1, lab2): 
    cie94(lab1, lab2, kL=1, K1=0.045, K2=0.015):
    ciede2000(lab1, lab2, kL=1.0, kC=1.0, kH=1.0): 
    cie76_JND: The "Just Noticeable Difference" threshold for CIE76 distances.

"""

__all__ = [
    'rgb_euclidean', 
    'hsv_euclidean', 
    'hsl_euclidean',
    'cie76', 
    'cie76_JND', 
    'cie94', 
    'ciede2000',
    ]

tau = 2*pi # Defining because python2's math module doesn't provide it. 

# Distance functions
# TODO: This module needs some clean up. euclidean_rgb() isn't limited to 
#       RGB, so its name is poor. hsv_euclidean and hsl_euclidean are the 
#       same. (Look into HWB version; it's probably the same as well.) 
#       Not sure if a LAB version makes sense. 


def rgb_euclidean(rgb1, rgb2):
    """Returns the euclidean distance between the vec3 args."""
    return sqrt((rgb1[0]-rgb2[0])**2 + (rgb1[1]-rgb2[1])**2 + (rgb1[2]-rgb2[2])**2)


def hxx_euclidean(hxx1, hxx2):
    """Returns euclidean distance between two colors in an Hxx colorspace."""
    x1, y1, z1 = cos(hxx1[0]*tau)*hxx1[1], sin(hxx1[0]*tau)*hxx1[1], hxx1[2]
    x2, y2, z2 = cos(hxx2[0]*tau)*hxx2[1], sin(hxx2[0]*tau)*hxx2[1], hxx2[2]
    return sqrt( (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2 )

hsv_euclidean = hxx_euclidean
hsl_euclidean = hxx_euclidean
hwb_euclidean = hxx_euclidean



# Computes delta E using CIE 1976
def cie76(lab1, lab2): 
    """Computes the CIE 1976 version of Delta E between two L*a*b* colors."""
    # https://en.wikipedia.org/wiki/Color_difference#CIE76
    return sqrt((lab1[0]-lab2[0])**2 + (lab1[1]-lab2[1])**2 + (lab1[2]-lab2[2])**2)

cie76_just_noticeable_difference = 2.3
cie76_JND = 2.3



# Computes delta E using CIE 1994
def cie94(lab1, lab2, kL=1, K1=0.045, K2=0.015):
    """Computes the CIE 1994 version of Delta E between two L*a*b* colors."""
    # https://en.wikipedia.org/wiki/Color_difference#CIE94
    L1, a1, b1 = lab1 
    c1 = sqrt(a1**2 + b1**2)
    L2, a2, b2 = lab2 
    c2 = sqrt(a2**2 + b2**2)
    dL2 = (L1 - L2)**2
    dC2 = (c1 - c2)**2 
    dH2 = (a1 - a2)**2 + (b1 - b2)**2 - dC2
    
    return sqrt( 
            dL2/kL**2 + 
            dC2/(1 + K1*c1)**2 +
            dH2/(1 + K2*c1)**2)



# Computes delta E using CIE DE2000
def ciede2000(lab1, lab2, kL=1.0, kC=1.0, kH=1.0): 
    """Computes the CIE 2000 version of Delta E between two L*a*b* colors."""
    # Reference, including Gaurav Sharma's original matlab implementation:
    # http://www2.ece.rochester.edu/~gsharma/ciede2000/
    L1, a1, b1 = lab1
    c1 = sqrt( a1**2 + b1**2)

    L2, a2, b2 = lab2
    c2 = sqrt( a2**2 + b2**2)

    c_avg = (c1 + c2) / 2

    G = 0.5 * (1 - sqrt(c_avg**7 / (c_avg**7 + 25**7))) 

    ap1 = a1 * (1 + G)
    ap2 = a2 * (1 + G)

    cp1 = sqrt(ap1**2 + b1**2)
    cp2 = sqrt(ap2**2 + b2**2)   

    hp1 = 0 if abs(ap1) + abs(b1) == 0 else atan2(b1, ap1)
    hp1 = hp1 if hp1 >= 0 else hp1 + tau

    hp2 = 0 if abs(ap2) + abs(b2) == 0 else atan2(b2, ap2)
    hp2 = hp2 if hp2 >= 0 else hp2 + tau

    dL = L2 - L1
    dC = cp2 - cp1
   
    dhp = 0 if cp1*cp2 == 0 else hp2 - hp1 
    if dhp >  pi: dhp -= tau
    if dhp < -pi: dhp += tau

    dH = 2 * sqrt(cp1 * cp2) * sin(dhp / 2)

    Lp = (L1 + L2) / 2
    Cp = (cp1 + cp2) / 2

    hp =  hp1 + hp2

    if cp1 * cp2 != 0: 
        hp = (hp1 + hp2) / 2.0
        if abs(hp1 - hp2) > pi:
            hp -= pi 
        if hp < 0: 
            hp += tau

    Lpm = (Lp - 50)**2
    T = (1 - 0.17 * cos(hp - tau / 12) + 
        0.24 * cos(2 * hp) + 
        0.32 * cos(3 * hp + tau / 60) -
        0.20 * cos(4 * hp - 63 * tau / 360))
    
    Sl = 1 + (0.015 * Lpm) / sqrt(20 + Lpm)
    Sc = 1 + 0.045 * Cp
    Sh = 1 + 0.015 * Cp * T
    
    deltaTheta = 30 * tau/360 * exp(-1 * ((360/tau * hp - 275)/25)**2)
    Rc = 2 * sqrt( Cp**7 / (Cp**7+25**7))

    Rt = -1 * sin(2 * deltaTheta) * Rc

    return sqrt(
        (dL / (kL * Sl))**2 + 
        (dC / (kC * Sc))**2 + 
        (dH / (kH * Sh))**2 + 
        Rt * dC / (kC * Sc) * dH / (kH * Sh))


