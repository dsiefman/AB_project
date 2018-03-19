#!python2.7

import os
import numpy as np
import sys

import get_frames

def smooth(a,WSZ):

    ''' 
    a: NumPy 1-D array containing the data to be smoothed
    WSZ: smoothing window size needs, which must be odd number,
    as in the original MATLAB implementation

    Taken from https://stackoverflow.com/questions/40443020/matlabs-smooth-implementation-n-point-moving-average-in-numpy-python
    '''

    out0 = np.convolve(a,np.ones(WSZ,dtype=int),'valid')/WSZ    
    r = np.arange(1,WSZ-1,2)
    start = np.cumsum(a[:WSZ-1])[::2]/r
    stop = (np.cumsum(a[:-WSZ:-1])[::2]/r)[::-1]
    return np.concatenate((  start , out0, stop  ))