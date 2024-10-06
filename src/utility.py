# utility.py

import time
import h5py
from PIL import Image
from constants import WHITE, BLACK

def timer_start():
    return time.time()

def timer_end(start_time, description="Operation"):
    elapsed_time = time.time() - start_time
    print(f"{description} took {elapsed_time:.2f} seconds.")
    return elapsed_time

def write_hdf5(file_name, dataset_name, data, compression=None):
    with h5py.File(file_name, 'w') as hdf5_file:
        hdf5_file.create_dataset(dataset_name, data=data, compression=compression)

def convert_hdf5_to_png(hdf5_filename, png_filename):
    try:
        with h5py.File(hdf5_filename, 'r') as hdf5_file:
            dataset_name = list(hdf5_file.keys())[0]
            image_data = hdf5_file[dataset_name][:]
            img = Image.fromarray(image_data)
            img.save(png_filename, format='PNG')
            print(f"Converted {hdf5_filename} to {png_filename}")
    except FileNotFoundError as e:
        print(f"File {hdf5_filename} not found. {e}")
    except Exception as e:
        print(f"Error during conversion: {e}")
