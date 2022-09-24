from functools import wraps

"""Internally used functions."""

__all__ = [
    'blend_function',
    'colpal_function',
    'colpal_params_function',
    'hexpal_function',
]


# Handles functions with two arguments: either two colors, 
# a palette and a color, or two palettes. 
def blend_function(_function): 
    @wraps(_function)
    def blend_closure(base, blend):
        if type(base[0]) is list: 
            if type(blend[0]) is list: 
                return [ _function(a, b) for a, b in zip(base, blend) ]
            else:
                return [_function(a, blend) for a in base ]
        else:
            return _function(base, blend)
    return blend_closure


# Handles functions with one argument which may be a vec3 or palette. 
def colpal_function(_function):
    @wraps(_function)
    def cp_closure(base):
        if type(base[0]) is list:
            return [ _function(a) for a in base ] 
        else:
            return _function(base)                    
    return cp_closure


# Handles functions with a first argument that may be a vec3 or a palette. 
def colpal_params_function(_function):
    @wraps(_function)
    def cp_params_closure(base, *args, **kwargs):
        if type(base[0]) is list:
            return [ _function(a, *args, **kwargs) for a in base ] 
        else:
            return _function(base, *args, **kwargs)                    
    return cp_params_closure


def hexpal_function(_function):
    @wraps(_function)
    def hexpal_closure(hexpal):
        if type(hexpal) is str and 5<len(hexpal)<8:
            return _function(hexpal)
        elif type(hexpal) is list:
            return [ _function(hexcode) for hexcode in hexpal ]
        else:
            raise ValueError('Expected hexcode or list of hexcodes.')
    return hexpal_closure

