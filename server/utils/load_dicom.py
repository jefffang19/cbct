import glob
import os
import pydicom
from pydicom.pixel_data_handlers.util import apply_voi_lut
import numpy as np
import matplotlib.pyplot as plt


def read_dicom(path):
    g = glob.glob(os.path.join(path, '*'))
    slices = [pydicom.read_file(s) for s in g]

    # adjust hu value
    slices = [hu_window(s, window_level=0, window_width=1000) for s in slices]

    return slices


def hu_window(scan, window_level=40, window_width=80, show_hist=False):
    scan = scan.pixel_array.copy()
    window = [window_level-window_width/2, window_width/2-window_level]

    scan = np.where(scan < window[0], window[0], scan)
    scan = np.where(scan > window[1], window[1], scan)

    if show_hist:
        plt.figure(0, figsize=(6, 6))
        plt.imshow(scan, 'gray')

        plt.figure(1, figsize=(6, 6))
        plt.hist(scan.flatten(), color='c')
        plt.xlabel("Hounsfield Units (HU)")
        plt.ylabel("Frequency")
        plt.show()

    return scan
