import numpy as np
import h5py
import time
from tqdm import tqdm
import os
from concurrent.futures import ThreadPoolExecutor
from numba import njit, prange
from PIL import Image

# Create a directory for HDF5 and PNG files if it doesn't exist
hdf5_dir = "./K100img"
png_dir = "./K100img"
os.makedirs(hdf5_dir, exist_ok=True)
os.makedirs(png_dir, exist_ok=True)

# Timer function
def timer_start():
    return time.time()

def timer_end(start_time, description="Operation"):
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"{description} took {elapsed_time:.2f} seconds.")
    return elapsed_time

# Define the image dimensions
width = 100000  
height = 100000  

# Compression options for HDF5
compression_opts = 2  # Lower compression level for faster writing

# Optimized function using Numba for fast image modification
@njit(parallel=True)
def modify_image(image):
    """ Modify the image by applying different pixel values using slicing. """
    image[0:100000, 50000:100000] = 0   # White rectangle (modifies part of the image)

def modify_dyed_image(image):
    """ Modify the image by applying different pixel values using slicing. """
    # image[10000:40000, 20000:50000] = 255
    # image[10000:40000, 50000:70000]=0
    # image[60000:80000, 60000:90000]=0

    # Execution time for 10 by 10 img: 0.552681 seconds
    # Parasite area: 400000
    # Dyed area inside parasite: 120000
    # Dyed to parasite area ratio: 0.30
    # The parasite has cancer: True
    # The parasite has cancer: True

    image[10000:50000, 20000:50000] = 255
    image[10000:30000, 50000:70000]=0 

# Stage 1: Generate images and save them in separate HDF5 files
def generate_hdf5_images_parallel():
    # Create a NumPy array filled with 255 (white pixels)
    parasite_image = np.full((height, width), 255, dtype=np.uint8)
    dyed_image = np.full((height, width), 255, dtype=np.uint8)

    with tqdm(total=2, desc="Processing images") as pbar:
        total_start = timer_start()

        # Modify the image using Numba and slicing
        step_start = timer_start()
        modify_image(parasite_image)
        timer_end(step_start, "Image modification for 100K Parasite")

        step_start = timer_start()
        modify_dyed_image(dyed_image)
        timer_end(step_start, "Image modification for 100K Dyed")

        # Function to write the dataset in parallel
        def write_hdf5(file_name, dataset_name, data):
            with h5py.File(file_name, 'w') as hdf5_file:
                hdf5_file.create_dataset(dataset_name, data=data, compression="gzip", compression_opts=compression_opts)

        # Start parallel HDF5 file writing using ThreadPoolExecutor
        step_start = timer_start()
        with ThreadPoolExecutor(max_workers=2) as executor:
            executor.submit(write_hdf5, f'{hdf5_dir}/parasite.h5', 'parasite', parasite_image)
            executor.submit(write_hdf5, f'{hdf5_dir}/dyed.h5', 'dyed', dyed_image )
        timer_end(step_start, "HDF5 file writing in parallel for 100k by 100k")

        # End timer for the entire process
        timer_end(total_start, "Total image processing for 100k by 100k ")

# Run the HDF5 generation process
generate_hdf5_images_parallel()
