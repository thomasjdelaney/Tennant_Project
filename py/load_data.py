import os, sys, argparse, glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

proj_dir = os.path.join(os.environ['PROJ'], 'Tennant_Project')
data_dir = os.path.join(proj_dir, 'data', 'python_3')

spatial_firing_frame = pd.read_pickle(os.path.join(data_dir, 'spatial_firing.pkl'))
processed_position_frame = pd.read_pickle(os.path.join(data_dir, 'processed_position_data.pkl'))

