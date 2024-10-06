import numpy as np
from config import WIDTH, HEIGHT, HDF5_100K_DIR
from constants import WHITE, BLACK
from messages import PARASITE_LARGE_IMAGE_MESSAGE
from utility import write_hdf5, timer_start, timer_end
from numba import njit, prange
from concurrent.futures import ThreadPoolExecutor

# Numba optimized function with prange for parallel execution
@njit(parallel=True)
def modify_image(image):
    """ Modify the image with defined regions in parallel. """
    for i in prange(10000, 50000):
        image[i, 20000:50000] = WHITE
    for i in prange(10000, 30000):
        image[i, 50000:70000] = BLACK

@njit(parallel=True)
def modify_dyed_image(image):
    """ Modify the dyed image with defined regions in parallel. """
    for i in prange(0, 10000):
        image[i, 20000:30000] = 255
    for i in prange(0,50000):
        image[i, 550000:100000] = 0

# TRUE
#  image[0:10000, 20000:30000] = 255  # Smaller dyed region (less than 10%)
#    image[0:50000, 50000:100000] = 0   # Parasite remains black in large areas

class ParasiteLargeImageGenerator:
    def __init__(self):
        self.image = np.zeros((HEIGHT, WIDTH), dtype=np.uint8)

    def generate(self):
        start_time = timer_start()

        # Modify image using Numba with prange for parallel execution
        modify_image(self.image)

        # Write to HDF5
        write_hdf5(f'{HDF5_100K_DIR}/parasite_large.h5', 'parasite_large', self.image, compression="lzf")

        timer_end(start_time, PARASITE_LARGE_IMAGE_MESSAGE)

class ParasiteLargeDyedImageGenerator:
    def __init__(self):
        self.image = np.zeros((HEIGHT, WIDTH), dtype=np.uint8)

    def generate(self):
        start_time = timer_start()

        # Modify dyed image using Numba with prange for parallel execution
        modify_dyed_image(self.image)

        # Write to HDF5
        write_hdf5(f'{HDF5_100K_DIR}/dyed_large.h5', 'dyed_large', self.image, compression="lzf")

        timer_end(start_time, "Dyed large image processing")


