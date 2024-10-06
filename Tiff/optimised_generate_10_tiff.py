import numpy as np
from PIL import Image
import time
import os
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
from numba import njit

# Create a directory for TIFF files if it doesn't exist
tiff_dir = "./10TiffImg"
png_dir = "./10TiffImg"
os.makedirs(tiff_dir, exist_ok=True)

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

# Optimized function using Numba for fast image modification
@njit(parallel=True)
def modify_parasite_image(image):
    """ Modify the image by applying different pixel values using slicing. """
    image[:, :width // 2] = 255  # Set left half to white

@njit(parallel=True)
def modify_dyed_image(image):
    """ Modify the image by applying different pixel values using slicing. """
    image[1:5, 2:5] = 255
    image[1:3, 5:7] = 0

def generate_tiff_images():
    # Create a NumPy array filled with 0 (black pixels)
    parasite_image = np.zeros((height, width), dtype=np.uint8)
    dyed_image = np.zeros((height, width), dtype=np.uint8)

    with tqdm(total=2, desc="Processing images") as pbar:
        total_start = timer_start()

        # Modify the images using Numba
        step_start = timer_start()
        modify_parasite_image(parasite_image)
        timer_end(step_start, "Image modification for Parasite")

        step_start = timer_start()
        modify_dyed_image(dyed_image)
        timer_end(step_start, "Image modification for Dyed")

        # Function to save images
        def save_image(filename, data):
            img = Image.fromarray(data)
            img.save(filename, compression="tiff_lzw")

        # Start parallel saving of TIFF files
        step_start = timer_start()
        with ThreadPoolExecutor(max_workers=2) as executor:
            executor.submit(save_image, f'{tiff_dir}/parasite.tiff', parasite_image)
            executor.submit(save_image, f'{tiff_dir}/dyed.tiff', dyed_image)
        timer_end(step_start, "TIFF file saving in parallel")

        # End timer for the entire process
        timer_end(total_start, "Total image processing")

# Run the TIFF generation process
generate_tiff_images()


# Function to convert TIFF to PNG
def convert_tiff_to_png(tiff_filename, png_filename):
    try:
        # Open the TIFF image
        img = Image.open(tiff_filename)
        img.save(png_filename, format='PNG')
        print(f"Converted {tiff_filename} to {png_filename}")
    except FileNotFoundError as e:
        print(f"Error: File {tiff_filename} not found. {e}")
    except Exception as e:
        print(f"Error during conversion: {e}")

# Main function to check and convert TIFF to PNG
def png():
    convert_tiff_to_png(f'{tiff_dir}/parasite.tiff',f'{tiff_dir}/parasite.png')
    convert_tiff_to_png(f'{png_dir}/dyed.tiff', f'{png_dir}/dyed.png')



# Run the conversion process
png()
