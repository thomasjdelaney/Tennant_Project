import os, sys, argparse, glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

proj_dir = os.path.join(os.environ['PROJ'], 'Tennant_Project')
data_dir = os.path.join(proj_dir, 'data', 'python_3')

spatial_firing_frame = pd.read_pickle(os.path.join(data_dir, 'spatial_firing.pkl'))
processed_position_frame = pd.read_pickle(os.path.join(data_dir, 'processed_position_data.pkl'))

def getSpatialBinsByBinWidth(bin_width, min_x_pos=0.0, max_x_pos=200.0):
    """
    Arguments:  bin_width, float, the desired bin width, in cm
    Returns:    bins, numpy.array (float), the bin borders in cm
    """
    num_full_bins = np.floor((max_x_pos - min_x_pos)/bin_width)
    last_bin_width = (max_x_pos - min_x_pos) - (num_full_bins*bin_width)
    full_bins = bin_width * np.arange(0, num_full_bins+1)
    all_bins = np.hstack([full_bins, max_x_pos]) if last_bin_width > 0 else full_bins
    return all_bins

def getSpatialBinsByNumberOfBins(num_bins=100, min_x_pos=0.0, max_x_pos=200.0):
    return np.linspace(min_x_pos, max_x_pos, num_bins+1)

def getSpatialHistForCell(spatial_firing_frame, cell_id, bins, density=False):
    firing_positions = spatial_firing_frame.loc[cell_id, 'x_position_cm']
    return np.histogram(firing_positions, bins=bins, density=density)

def plotSpatialHistForCell(spatial_firing_frame, cell_id, bins, density=False):
    firing_positions = spatial_firing_frame.loc[cell_id, 'x_position_cm']
    plt.hist(firing_positions, bins=bins, density=density, label=str(cell_id))
    plt.legend(fontsize='large')
    return None

bins = getSpatialBinsByNumberOfBins()

for i, cell_id in enumerate(spatial_firing_frame.index.values):
    plt.subplot(10,1,i+1)
    plotSpatialHistForCell(spatial_firing_frame, cell_id, bins)
    if (i+1) == spatial_firing_frame.shape[0]:
        plt.xlabel('position (cm)', fontsize='large')

plt.show(block=False)
