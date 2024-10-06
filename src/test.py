# test.py

import numpy as np
import time
from numba import njit, prange
import concurrent.futures
import h5py

# Updated HDF5 directory for large images
hdf5_dir_small = "./10Img"
hdf5_dir_large = "./K100img"

def check_hdf5_contents(file_path):
    try:
        with h5py.File(file_path, 'r') as f:
            print(f"Available datasets in {file_path}: {list(f.keys())}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    # Check small images
    print("Checking small images...")
    check_hdf5_contents(f'{hdf5_dir_small}/parasite.h5')
    check_hdf5_contents(f'{hdf5_dir_small}/dyed.h5')

    # Check large images
    print("Checking large images...")
    check_hdf5_contents(f'{hdf5_dir_large}/parasite_large.h5')
    check_hdf5_contents(f'{hdf5_dir_large}/dyed_large.h5')

if __name__ == "__main__":
    main()
