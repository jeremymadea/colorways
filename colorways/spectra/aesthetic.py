"""
Provides a pleasing approximation of the visible spectrum. 
The violet side seems a bit compressed. The original came from:
https://stackoverflow.com/revisions/22681410/5)

"""

__all__ = []

def eval_quadratic(x, a, b, c):
    return a*x*x + b*x + c

def rgb_component(nm, bands): 
    for tpl in bands:
        if tpl[0] <= nm < tpl[1]:
            t = (nm - tpl[0]) / float(tpl[1] - tpl[0])
            return eval_quadratic(t, tpl[2], tpl[3], tpl[4])
    return 0.0

def wavelen2rgb(nm):
    rbands = [(400,410,-0.20, 0.33, 0.00), 
              (410,475,-0.13, 0.00, 0.14), 
              (545,595,-1.00, 1.98, 0.00), 
              (595,650,-0.40, 0.06, 0.98),
              (650,700, 0.20,-0.84, 0.65)] 
    gbands = [(415,475, 0.80, 0.00, 0.00), 
              (475,590,-0.80, 0.76, 0.80),
              (585,639, 0.00,-0.84, 0.84)]
    bbands = [(400,475,-1.50, 2.20, 0.00),
              (475,560, 0.30,-1.00, 0.70)]
    
    r = rgb_component(nm, rbands)
    g = rgb_component(nm, gbands)
    b = rgb_component(nm, bbands)
    return [r, g, b]


# Relevant Original code (from https://stackoverflow.com/revisions/22681410/5)
#         if ((l>=400.0)&&(l<410.0)) { t=(l-400.0)/(410.0-400.0); r=    +(0.33*t)-(0.20*t*t); }
#    else if ((l>=410.0)&&(l<475.0)) { t=(l-410.0)/(475.0-410.0); r=0.14         -(0.13*t*t); }
#    else if ((l>=545.0)&&(l<595.0)) { t=(l-545.0)/(595.0-545.0); r=    +(1.98*t)-(     t*t); }
#    else if ((l>=595.0)&&(l<650.0)) { t=(l-595.0)/(650.0-595.0); r=0.98+(0.06*t)-(0.40*t*t); }
#    else if ((l>=650.0)&&(l<700.0)) { t=(l-650.0)/(700.0-650.0); r=0.65-(0.84*t)+(0.20*t*t); }
#         if ((l>=415.0)&&(l<475.0)) { t=(l-415.0)/(475.0-415.0); g=             +(0.80*t*t); }
#    else if ((l>=475.0)&&(l<590.0)) { t=(l-475.0)/(590.0-475.0); g=0.8 +(0.76*t)-(0.80*t*t); }
#    else if ((l>=585.0)&&(l<639.0)) { t=(l-585.0)/(639.0-585.0); g=0.84-(0.84*t)           ; }
#         if ((l>=400.0)&&(l<475.0)) { t=(l-400.0)/(475.0-400.0); b=    +(2.20*t)-(1.50*t*t); }
#    else if ((l>=475.0)&&(l<560.0)) { t=(l-475.0)/(560.0-475.0); b=0.7 -(     t)+(0.30*t*t); }
