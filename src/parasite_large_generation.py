import numpy as np
from config import WIDTH, HEIGHT, HDF5_100K_DIR
from constants import WHITE, BLACK
from messages import PARASITE_LARGE_IMAGE_MESSAGE
from utility import write_hdf5, timer_start, timer_end
from numba import njit, prange
from concurrent.futures import ThreadPoolExecutor

@njit(parallel=True)
def modify_image(image):
    """ Modify the image with defined regions in parallel. """
    image[10000:50000, 20000:50000] = WHITE
    image[10000:30000, 50000:70000] = BLACK

@njit(parallel=True)
def modify_dyed_image(image):
    """ Modify the dyed image with defined regions in parallel. """
    image[10000:50000, 20000:50000] = 255
    image[10000:30000, 50000:70000] = 0

class ParasiteLargeImageGenerator:
    def __init__(self):
        self.image = np.zeros((HEIGHT, WIDTH), dtype=np.uint8)

    def generate(self):
        start_time = timer_start()
        modify_image(self.image)  # Pass the image to the Numba function

        # Write to HDF5 in a thread pool
        with ThreadPoolExecutor(max_workers=1) as executor:
            executor.submit(write_hdf5, f'{HDF5_100K_DIR}/parasite_large.h5', 'parasite_large', self.image, compression="gzip")

        timer_end(start_time, PARASITE_LARGE_IMAGE_MESSAGE)

class ParasiteLargeDyedImageGenerator:
    def __init__(self):
        self.image = np.zeros((HEIGHT, WIDTH), dtype=np.uint8)

    def generate(self):
        start_time = timer_start()
        modify_dyed_image(self.image)  # Pass the image to the Numba function

        # Write to HDF5 in a thread pool
        with ThreadPoolExecutor(max_workers=1) as executor:
            executor.submit(write_hdf5, f'{HDF5_100K_DIR}/dyed_large.h5', 'dyed_large', self.image, compression="gzip")

        timer_end(start_time, "Dyed large image processing")

# Main function to generate images and test for cancer
def main():
    # Generate large parasite and dyed images
    print("Generating large parasite images...")
    large_parasite_generator = ParasiteLargeImageGenerator()
    large_parasite_generator.generate()

    print("Generating large dyed images...")
    large_dyed_generator = ParasiteLargeDyedImageGenerator()
    large_dyed_generator.generate()

if __name__ == "__main__":
    main()