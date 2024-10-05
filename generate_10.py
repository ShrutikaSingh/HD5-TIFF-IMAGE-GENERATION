import numpy as np
import h5py
import time
from tqdm import tqdm
import os
from concurrent.futures import ThreadPoolExecutor
from numba import njit, prange
from PIL import Image

# Create a directory for HDF5 and PNG files if it doesn't exist
hdf5_dir = "./10img"
png_dir = "./10img"
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
width = 10
height = 10

# Compression options for HDF5
compression_opts = 2  # Lower compression level for faster writing

# Optimized function using Numba for fast image modification
@njit(parallel=True)
def modify_image(image):
    """ Modify the image by applying different pixel values using slicing. """
    image[0:10, 5:10] = 0   # White rectangle (modifies part of the image)

def modify_dyed_image(image):
    """ Modify the image by applying different pixel values using slicing. """
    
    # image[1:4, 2:5] = 255
    # image[1:4, 5:7]=0 
    # image[6:8, 6:9]=0 

    # Parasite area: 50
    # Dyed area inside parasite: 12
    # The parasite has cancer: True

    image[1:4, 2:5] = 255
    image[1:3, 5:7]=0 

    # Parasite area: 50
    # Dyed area inside parasite: 4
    # The parasite has cancer: False
    
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
        timer_end(step_start, "Image modification for Parasite")

        step_start = timer_start()
        modify_dyed_image(dyed_image)
        timer_end(step_start, "Image modification for Dyed")

        # Function to write the dataset in parallel
        def write_hdf5(file_name, dataset_name, data):
            with h5py.File(file_name, 'w') as hdf5_file:
                hdf5_file.create_dataset(dataset_name, data=data, compression="gzip", compression_opts=compression_opts)

        # Start parallel HDF5 file writing using ThreadPoolExecutor
        step_start = timer_start()
        with ThreadPoolExecutor(max_workers=2) as executor:
            executor.submit(write_hdf5, f'{hdf5_dir}/parasite.h5', 'parasite', parasite_image)
            executor.submit(write_hdf5, f'{hdf5_dir}/dyed.h5', 'dyed', dyed_image )
        timer_end(step_start, "HDF5 file writing in parallel")

        # End timer for the entire process
        timer_end(total_start, "Total image processing")

# Run the HDF5 generation process
generate_hdf5_images_parallel()

# Function to convert HDF5 image dataset to PNG
def convert_hdf5_to_png(hdf5_filename, png_filename):
    try:
        # Open the HDF5 file
        with h5py.File(hdf5_filename, 'r') as hdf5_file:
            # Assuming there is only one dataset in the file or we are targeting the first dataset
            dataset_name = list(hdf5_file.keys())[0]  # Get the first dataset's name
            image_data = hdf5_file[dataset_name][:]   # Load image data as a NumPy array
            img = Image.fromarray(image_data)         # Convert NumPy array to PIL Image
            img.save(png_filename, format='PNG')      # Save as PNG
            print(f"Converted {hdf5_filename} to {png_filename}")
    except FileNotFoundError as e:
        print(f"Error: File {hdf5_filename} not found. {e}")
    except Exception as e:
        print(f"Error during conversion: {e}")

# Main function to check and convert HDF5 to PNG
def png():
    convert_hdf5_to_png(f'{hdf5_dir}/parasite.h5',f'{hdf5_dir}/parasite.png')
    convert_hdf5_to_png(f'{png_dir}/dyed.h5', f'{png_dir}/dyed.png')

# Run the conversion process
png()
