#!/usr/bin/env python

import numpy as np
import lmfit   # module to do Lorentz fitting
import matplotlib.pyplot as plt
import re, sys, time, os
import get_frames

TC = None # 'plastic'
separate = False

samp_dir = '/home/siefman/AB_project/to_plot'
files_to_plot = os.listdir(samp_dir)

# samp_file = 'Gel1_GT15NH2_SeroRoth_100mM_10ul_2018-02-12.csv'
# files_to_plot =[samp_file]

# If multiple plots found, print all their first/last frame data
# to one file called FirstLast_data.txt
if len(files_to_plot) > 1:
	first_last = open(os.path.join(samp_dir, 'FirstLast_data.txt'), 'w')
	first_last.write('{0:<50s}{1:>20s}{2:>13s}{3:>12s}{4:>13s}{5:>13s}{6:>18s}{7:>13s}{8:>17s}\n'.format(
		              'Sample', 'I_first', 'I_first_unc',
		              'I_last', 'I_last_unc',
		              'lambda_first', 'lambda_first_unc',
		              'lambda_last', 'lambda_last_unc'))

for samp_file in files_to_plot:
    if 'csv' in samp_file:

    	print("PROCESSING " + samp_file)

    	samp_name = samp_file[:-4]
    	samp_path = os.path.join(samp_dir, samp_file)

        [x, frames]  = get_frames.get_frames(samp_path, TC)
        [heights, centers] = get_frames.fit_samp_file(x, frames)

		# Do plotting
        if separate:
            get_frames.plot_peak_1yaxis(centers, heights, samp_path)
        else: 
            get_frames.plot_peak_2yaxis(centers, heights, samp_path)

		# Print txt output data files
        get_frames.print_frame_data(centers, heights, samp_path)

        if len(files_to_plot) > 1:
            first_last.write('{0:<50s}{1:>20.4e}{2:>13.4e}{3:>12.4e}{4:>13.4e}{5:>13.4e}{6:>18.4e}{7:>13.4e}{8:>17.4e}\n'.format(
                              samp_name,  heights[0, 0], heights[0, -1],
                              heights[-1, 0], heights[-1, -1],
                              centers[0, 0], centers[0, -1],
                              centers[-1, 0], centers[-1, -1]))
    else:
        pass

if len(files_to_plot) > 1:
    first_last.close()