import numpy as np
import h5py
from PIL import Image
from tqdm import tqdm
import os
import time  # To track time

# Create a directory for HDF5 and PNG files 
hdf5_dir = "./10Img"
png_dir = "./10Img"


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


# Image 10 * 10
width = 10
height = 10

# Enable compression for HDF5
compression_opts = 4  # Compression level 4 (0: no compression, 9: max compression)

# Stage 1: Generate images and save them in separate HDF5 files
def generate_hdf5_images():

    # Create an empty NumPy array of zeros with the specified dimensions (black pixels)
    image = np.zeros((height, width), dtype=np.uint8) 

    with tqdm(total=7, desc="Processing images") as pbar:

        # Start timer for the entire process
        total_start = timer_start()

        # Image 1: Parasite with left side white (50% black/white)
        step_start = timer_start()
        image[:height, :width // 2] = 255
        with h5py.File(f'{hdf5_dir}/parasite.h5', 'w') as hdf5_file:
            hdf5_file.create_dataset('parasite', data=image, compression="gzip", compression_opts=compression_opts)
        timer_end(step_start, "Parasite 50% original image generation")
        pbar.update(1)

        # Image 3: 12x12 region in top-left is black
     
        step_start = timer_start()
        # this image should  have cancer
        # image[1:4, 2:5] = 0
        # image[1:4, 5:7]=255
        # image[6:8, 6:9]=255
        # regions = [
        #     (1, 4, 2, 5, 0),      # Black region (0)
        #     (1, 4, 5, 7, 255),    # White region (255)
        #     (6, 8, 6, 9, 255)     # White region (255)
        # ]
        
    #    1st image = 0 & 2nd image have 0 or 1  final image 0
    
    #     after than count number of 1ins in final image
    
       #  No cancer
        # image[1:3, 1:3] = 0
        # image[1:10, 3:10] = 255
        regions = [
                (1, 3, 1, 3, 0),      # Black region (0)
                (1, 10, 3, 10, 255),    # White region (255)
            ]

        # Apply regions
        for x_start, x_end, y_start, y_end, value in regions:
            image[x_start:x_end, y_start:y_end] = value

        with h5py.File(f'{hdf5_dir}/dyed.h5', 'w') as hdf5_file:
            hdf5_file.create_dataset('dyed', data=image, compression="gzip", compression_opts=compression_opts)
        timer_end(step_start, "Dyed and cancer")
        pbar.update(1)

        timer_end(total_start, "Total image processing")


# Run the HDF5 generation process
generate_hdf5_images()


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
    convert_hdf5_to_png(f'{hdf5_dir}/parasite.h5', f'{png_dir}/parasite.png')
    convert_hdf5_to_png(f'{hdf5_dir}/dyed.h5', f'{png_dir}/dyed.png')

# Run the conversion process
# png()
# print("Images successfully stored in separate HDF5 files and converted to PNG.")
