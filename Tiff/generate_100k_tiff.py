import numpy as np
from PIL import Image
from tqdm import tqdm
import os
Image.MAX_IMAGE_PIXELS = None
import time  # To track time

tiff_dir="./K100TiffImg"
os.makedirs(tiff_dir, exist_ok=True)


# Timer function
def timer_start():
    """Starts and returns the current time."""
    return time.time()

def timer_end(start_time, description="Operation"):
    """Ends the timer and prints the elapsed time for the given operation."""
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"{description} took {elapsed_time:.2f} seconds.")
    return elapsed_time


# Define the image dimensions
width = 100000
height = 100000
# Create an empty NumPy array of zeros with the specified dimensions (black pixels)


# Enable compression and save the image with compression
compression = "tiff_lzw"  # You can choose the compression method you prefer
with tqdm(total=2, desc="Processing images") as pbar:
    # Start timer for the entire process
    total_start = timer_start()

    
    step_start = timer_start()
    image = np.zeros((height, width), dtype=np.uint8)
    # Set the left half of the image to white (255)
    image[:height, :width // 2] = 255
    image_pil = Image.fromarray(image)
    image_pil.save(f'{tiff_dir}/parasite.tiff', compression=compression)
    timer_end(total_start, "Parasite tiff image generation time of 100k by 100k tiff image")

    pbar.update(1)

    step_start = timer_start()
    image[10000:40000, 20000:50000] = 0
    image[10000:40000, 50000:70000]=255
    image[60000:80000, 60000:90000]=255
    image_pil = Image.fromarray(image)
    image_pil.save(f'{tiff_dir}/dyed.tiff', compression=compression)
    timer_end(step_start, "Dyed tiff image generation time of 100k by 100k tiff image")

    pbar.update(1)
    timer_end(total_start, "Total image processing 100k by 100k tiff image ")

