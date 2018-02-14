#!/usr/bin/env python

import numpy as np
import lmfit   # module to do Lorentz fitting
import matplotlib.pyplot as plt
import re, sys, time, os
import get_frames

TC = None # 'plastic'

samp_dir = '/home/siefman/AB_project/to_plot'

files_to_plot = os.listdir(samp_dir)

# for file in files_to_plot:
#     if 'csv' in file:
#         print("\n PLOTTING %s" % file)
#         get_frames.plot_samp_file(os.path.join(samp_dir,file), TC)
#     else:
#         pass

file = 'Gel1_GT15NH2_SeroRoth_100mM_10ul_2018-02-12.csv'
get_frames.plot_samp_file(os.path.join(samp_dir,file), TC)