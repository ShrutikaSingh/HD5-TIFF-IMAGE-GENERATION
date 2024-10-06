import numpy as np
from config import WIDTH, HEIGHT, HDF5_100K_DIR, DYED_REGIONS
from constants import WHITE, BLACK
from messages import DYED_LARGE_IMAGE_MESSAGE, PARASITE_LARGE_IMAGE_MESSAGE
from utility import write_hdf5, timer_start, timer_end
from numba import njit
from concurrent.futures import ThreadPoolExecutor

class ParasiteLargeImageGenerator:
    def __init__(self):
        self.image = np.zeros((HEIGHT, WIDTH), dtype=np.uint8)

    @njit
    def modify_image(self):
        """ Modify the image with defined regions. """
        # Example regions for modification
        self.image[10000:50000, 20000:50000] = WHITE
        self.image[10000:30000, 50000:70000] = BLACK

    def generate(self):
        start_time = timer_start()
        self.modify_image()  # Call the optimized function to modify the image

        # Write to HDF5 in a thread pool
        with ThreadPoolExecutor(max_workers=1) as executor:
            executor.submit(write_hdf5, f'{HDF5_100K_DIR}/parasite_large.h5', 'parasite_large', self.image, compression="gzip")

        timer_end(start_time, PARASITE_LARGE_IMAGE_MESSAGE)


class ParasiteLargeDyedImageGenerator:
    def __init__(self):
        self.image = np.zeros((HEIGHT, WIDTH), dtype=np.uint8)

    @njit
    def modify_dyed_image(self):
        """ Modify the dyed image with defined regions. """
        for x_start, x_end, y_start, y_end, value in DYED_REGIONS:
            self.image[x_start:x_end, y_start:y_end] = value

    def generate(self):
        start_time = timer_start()
        self.modify_dyed_image()  # Call the optimized function to modify the image

        # Write to HDF5 in a thread pool
        with ThreadPoolExecutor(max_workers=1) as executor:
            executor.submit(write_hdf5, f'{HDF5_100K_DIR}/dyed_large.h5', 'dyed_large', self.image, compression="gzip")

        timer_end(start_time, DYED_LARGE_IMAGE_MESSAGE)

# Example usage in main.py remains unchanged
