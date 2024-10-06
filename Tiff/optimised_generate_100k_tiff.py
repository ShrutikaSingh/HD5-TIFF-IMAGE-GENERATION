import numpy as np
from PIL import Image
import time
import os
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
from numba import njit, prange

# Create a directory for TIFF files if it doesn't exist
tiff_dir = "./K100TiffImg"
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
width = 100000  
height = 100000  

# Optimized function using Numba for fast image modification (parallel processing)
@njit(parallel=True)
def modify_parasite_image(image):
    """ Modify the entire parasite image by setting the left half to white. """
    for i in prange(height):
        image[i, :width // 2] = 255  # Set the left half of the image to white

@njit(parallel=True)
def modify_dyed_image(image):
    """ Modify the entire dyed image with specified regions. """
    for i in prange(10000, 50000):
        image[i, 20000:50000] = 255  # Set region to white
    for i in prange(10000, 30000):
        image[i, 50000:70000] = 0    # Set region to black

# Function to save the image using Pillow
def save_image(filename, data):
    img = Image.fromarray(data)
    img.save(filename, compression="tiff_lzw")

# Main function to generate and save both TIFF images
def generate_tiff_images():
    # Create empty images
    parasite_image = np.zeros((height, width), dtype=np.uint8)
    dyed_image = np.zeros((height, width), dtype=np.uint8)

    with tqdm(total=2, desc="Processing images") as pbar:
        total_start = timer_start()

        # Modify the parasite image
        step_start = timer_start()
        modify_parasite_image(parasite_image)
        timer_end(step_start, "Image modification for Parasite")

        # Modify the dyed image
        step_start = timer_start()
        modify_dyed_image(dyed_image)
        timer_end(step_start, "Image modification for Dyed")

        # Save the images in parallel
        step_start = timer_start()
        with ThreadPoolExecutor(max_workers=2) as executor:
            executor.submit(save_image, f'{tiff_dir}/parasite.tiff', parasite_image)
            executor.submit(save_image, f'{tiff_dir}/dyed.tiff', dyed_image)
        timer_end(step_start, "TIFF file saving in parallel")

        # End timer for the entire process
        timer_end(total_start, "Total image processing")

# Run the TIFF generation process
generate_tiff_images()
