#from math import tau, cos, sin, hypot, atan2
from statistics import mean, pstdev, pvariance
#from .conv import * 
from .dist import cie76
from .conv import (
    rgb2hsl,
    rgb2hsv,
    hsv2hwb,
    rgb2lab,
    hsv2hsl,
    hsv2rgb,
    hsl2hsv,
    hsl2rgb,
    hwb2hsv,
    hex2lab,
    norm2bytes,
    bytes2norm,
)
from .util import (
    pal_extract_chans, rect, polar, circ_mean, luma,
)

"""Provides the MasterPalette class and utility functions.

"""
__all__ = [
    'new_order_by_dist_closure'
    'MasterPalette'
]


def list_indexed_by(L, indices):
    return [L[i] for i in indices]

def new_order_by_dist_closure(hexstr, fn=cie76): 
    lab = hex2lab(hexstr)
    def orderfunc(p, i): 
        return fn(p.lab[i], lab)
    return orderfunc



def bin_sizes(nitems, nbins):
    bsz = nitems / nbins
    return [round((i+1)*bsz)-round(i*bsz) for i in range(nbins)]

def bin_slices(nitems, nbins):
    bsz = nitems/nbins
    return [(round(i*bsz), round((i+1)*bsz)) for i in range(nbins)]




class MasterPalette: 
    """
    A MasterPalette holds palette data and metadata and provides 
    methods to facilitate palette analysis tasks, the creation and 
    storage of different palette orderings, and the generation of 
    palette variants. 
    """
    
    def __init__(self, palette, mode='hsl', usebytes=False):
        self._palette = list(palette) # Keep a copy of the original.
        self._mode = mode
        self._usebytes = usebytes

        self.pal = self._palette
        self.curr = self.pal

        if usebytes: 
            self.pal = bytes2norm(palette)
    
        if mode == 'rgb':
            self.rgb = self.pal
            self.hsl = rgb2hsl(self.rgb)
            self.hsv = rgb2hsv(self.rgb)
            self.hwb = hsv2hwb(self.hsv) # preferred
            self.lab = rgb2lab(self.rgb)
        elif mode == 'hsv':
            self.hsv = sel.pal
            self.hsl = hsv2hsl(self.hsv)
            self.hwb = hsv2hwb(self.hsv)
            self.rgb = hsv2rgb(self.hsv)
            self.lab = rgb2lab(self.rgb)
        elif mode == 'hsl':
            self.hsl = self.pal
            self.hsv = hsl2hsv(self.hsl)
            self.hwb = hsv2hwb(self.hsv) # preferred
            self.rgb = hsl2rgb(self.hsl)
            self.lab = rgb2lab(self.rgb)
        elif mode == 'hwb':
            self.hwb = self.pal
            self.hsv = hwb2hsv(self.hwb)
            self.hsl = hsv2hsl(self.hsv) 
            self.rgb = hsl2rgb(self.hsl) # preferred 
            self.lab = rgb2lab(self.rgb)

        self.rgb8 = norm2bytes(self.rgb)
    
        self.hsl_h, self.hsl_s, self.hsl_l = pal_extract_chans(self.hsl)
        self.hsv_h, self.hsv_s, self.hsv_v = pal_extract_chans(self.hsv)
        self.rgb_r, self.rgb_g, self.rgb_b = pal_extract_chans(self.rgb)
        self.lab_l, self.lab_a, self.lab_b = pal_extract_chans(self.lab)
        self.hwb_h, self.hwb_w, self.hwb_b = pal_extract_chans(self.hwb)

        self.luma = [ luma(clr) for clr in self.rgb ]
        self.n = len(self.hsl)

        self.mean_hue_dist, self.mean_hue = circ_mean(self.hsl_h)
        if self.mean_hue < 0.0: 
            self.mean_hue += 1.0
        
        self.hsl_mean_s = mean(self.hsl_s)
        self.hsl_std_s = pstdev(self.hsl_s)
        self.hsl_min_s = min(self.hsl_s)
        self.hsl_max_s = max(self.hsl_s)
        self.hsl_mean_l = mean(self.hsl_l)
        self.hsl_std_l = pstdev(self.hsl_l)
        self.hsl_min_l = min(self.hsl_l)
        self.hsl_max_l = max(self.hsl_l)

        self.hsv_mean_s = mean(self.hsv_s)
        self.hsv_std_s = pstdev(self.hsv_s)
        self.hsv_min_s = min(self.hsv_s)
        self.hsv_max_s = max(self.hsv_s)
        self.hsv_mean_v = mean(self.hsv_v)
        self.hsv_std_v = pstdev(self.hsv_v)
        self.hsv_min_v = min(self.hsv_v)
        self.hsv_max_v = max(self.hsv_v)

        self.rgb_mean_r = mean(self.rgb_r)
        self.rgb_std_r = pstdev(self.rgb_r)
        self.rgb_min_r = min(self.rgb_r)
        self.rgb_max_r = max(self.rgb_r)
        self.rgb_mean_g = mean(self.rgb_g)
        self.rgb_std_g = pstdev(self.rgb_g)
        self.rgb_min_g = min(self.rgb_g)
        self.rgb_max_g = max(self.rgb_g)
        self.rgb_mean_b = mean(self.rgb_b)
        self.rgb_std_b = pstdev(self.rgb_b)
        self.rgb_min_b = min(self.rgb_b)
        self.rgb_max_b = max(self.rgb_b)

        self.hwb_mean_w = mean(self.hwb_w)
        self.hwb_std_w = pstdev(self.hwb_w)
        self.hwb_min_w = min(self.hwb_w)
        self.hwb_max_w = max(self.hwb_w)
        self.hwb_mean_b = mean(self.hwb_b)
        self.hwb_std_b = pstdev(self.hwb_b)
        self.hwb_min_b = min(self.hwb_b)
        self.hwb_max_b = max(self.hwb_b)

        self.luma_mean = mean(self.luma)
        self.luma_std = pstdev(self.luma)
        self.luma_min = min(self.luma)
        self.luma_max = max(self.luma)
  
        indexes = range(self.n)
        self.indexes = indexes

        self.orderings = {
            None: indexes,
            'by-hue': sorted(indexes, key=lambda i: self.hsl_h[i]), 
            'by-lsat': sorted(indexes, key=lambda i: self.hsl_s[i]), 
            'by-lum': sorted(indexes, key=lambda i: self.hsl_l[i]), 
            'by-vsat': sorted(indexes, key=lambda i: self.hsv_s[i]), 
            'by-val': sorted(indexes, key=lambda i: self.hsv_v[i]), 
            'by-r': sorted(indexes, key=lambda i: self.rgb_r[i]), 
            'by-g': sorted(indexes, key=lambda i: self.rgb_g[i]), 
            'by-b': sorted(indexes, key=lambda i: self.rgb_b[i]), 
            'by-luma': sorted(indexes, key=lambda i: self.luma[i]), 
            'by-L': sorted(indexes, key=lambda i: self.lab_l[i]), 
            'by-white': sorted(indexes, key=lambda i: self.hwb_w[i]), 
            'by-black': sorted(indexes, key=lambda i: self.hwb_b[i]), 
        }

    def get_rgb(self, order=None):
        return list_indexed_by(self.rgb, self.orderings[order])

    def get_hsl(self, order=None):
        return list_indexed_by(self.hsl, self.orderings[order])

    def get_hsv(self, order=None):
        return list_indexed_by(self.hsl, self.orderings[order])

    def get_lab(self, order=None):
        return list_indexed_by(self.hsl, self.orderings[order])

    def get_hwb(self, order=None):
        return list_indexed_by(self.hwb, self.orderings[order])

    def get_rgb8(self, order=None):
        return list_indexed_by(self.rgb8, self.orderings[order])

    def register_ordering(self, name, ordering):
        self.orderings[name] = ordering

    def create_ordering(self, name, order_by_fn):
        idxkey = []
        # Use provided function to compute key for index.
        for i in range(self.n):
            idxkey.append((i, order_by_fn(self, i)))
        ordering = [t[0] for t in sorted(idxkey, key=lambda t: t[1])]
        self.register_ordering(name, ordering)

    def create_bin_ordering(self, name, bins, base_order, bin_order):
        """
        Creates a new bin ordering and saves it. 

        First, the palette is ordered according to the base_order, then it 
        is partitioned into bins. Finally, the contents of each bin are sorted 
        according to the bin_order.

        Args:
            name (str): the name to save the ordering as.
            bins (int): the number of bins.
            base_order (str): the name of the ordering to start with.
            bin_order (str): the name of the ordering to use for bin contents.
        """
        order = list(self.orderings[base_order]) # Start with base order.
        bslices = bin_slices(self.n, bins)
        # create a lookup table for the ordering given by key2. 
        lookup = [None] * self.n
        for i, ix in enumerate(self.orderings[bin_order]): 
            lookup[ix] = i

        # Iterate through the slices and sort each slice by the ordering
        # specified with key2. 
        for s in bslices:
            order[s[0]:s[1]] = sorted(order[s[0]:s[1]], key=lambda i: lookup[i])

        self.register_ordering(name, order) 

    def gen(self, fn):
        """
        Generate a variant.

        This method returns a list.  The provided callback is called once for 
        each color in the MasterPalette. The callback must have a signature 
        such as:

            callback(master, i)

        It must accept two arguments; the first will be a reference to the 
        MasterPalette and the second is an index that increases by one on each 
        call, ranging from 0 on the first call to one less than the length of 
        the MasterPalette on the final call. 
        
        When the callback returns None, nothing is added to the return list.
        When it returns a set or a tuple, each element in the set or tuple is 
        added to the return list. Otherwise, whatever the callback returns is 
        added to the return list. 

        Most often, the values to be added to the return list will be three
        element lists (vec3's) so gen will return a palette. But this is not
        strictly required. No checking is done on the elements added to the
        return list.
        """

        new = []
        for i in range(self.n):
            retval = fn(self, i)
            if retval is not None:
                if type(retval) in (set, tuple):
                    for vec3 in retval: 
                        new.append(vec3)
                else:
                    new.append(retval)
        return new        
        
    def __len__(self):
        return self.n

    def __getitem__(self, i):
        if isinstance(i, slice):
            return self.__class__(self.curr[i])
        else:
            return self.curr[i]

    def reset(self):
        self.curr = self.pal

    def config(self, space=None, order=None):
        if space is None: 
           space = self._mode
        if space == 'rgb':
            self.curr = self.get_rgb(order) 
        elif space == 'hsl':
            self.curr = self.get_hsl(order) 
        elif space == 'hsv':
            self.curr = self.get_hsv(order) 
        elif space == 'lab':
            self.curr = self.get_lab(order) 
        elif space == 'hwb':
            self.curr = self.get_hwb(order) 
        elif space == 'rgb8':
            self.curr = self.get_rgb8(order) 
        else: 
            self.curr = list_indexed_by(self.pal, self.orderings[order])

    def set_variant(self, fn):
        self.curr - self.gen(fn)
