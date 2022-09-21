"""
This is a very crude approximation of the visible spectrum.
"""
__all__ = []

def wavelen2rgb(nm):
    r = g = b = 0.0
    if 380 <= nm  < 440:
        r = -(nm - 440) / 60.0
        b = 1.0
    elif 440 <= nm < 490:
        g = (nm - 440) / 50.0
        b = 1.0
    elif 490 <= nm < 510:
        g = 1.0
        b = -(nm - 510) / 20.0
    elif 510 <= nm < 580:
        r = (nm - 510) / 70.0
        g = 1.0
    elif 580 <= nm < 645:
        r = 1.0
        g = -(nm - 645) / 65.0
    elif 645 <= nm <= 780:
        r = 1.0
    return [r, g, b]
