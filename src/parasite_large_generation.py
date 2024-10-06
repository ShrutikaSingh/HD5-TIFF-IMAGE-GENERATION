# parasite_large_generation.py

import numpy as np
from config import WIDTH, HEIGHT, HDF5_DIR
from constants import WHITE, BLACK
from messages import PARASITE_LARGE_IMAGE_MESSAGE
from utility import write_hdf5, timer_start, timer_end

class ParasiteLargeImageGenerator:
    def __init__(self):
        self.image = np.zeros((HEIGHT, WIDTH), dtype=np.uint8)

    def generate(self):
        start_time = timer_start()

        # Define regions to modify in the image for large images
        regions = [
            (10000, 50000, 20000, 50000, WHITE),  # Example white region
            (10000, 30000, 50000, 70000, BLACK)   # Example black region
        ]

        # Apply modifications to the image
        for x_start, x_end, y_start, y_end, value in regions:
            self.image[x_start:x_end, y_start:y_end] = value

        write_hdf5(f'{HDF5_DIR}/parasite_large.h5', 'parasite_large', self.image, compression="gzip")

        timer_end(start_time, PARASITE_LARGE_IMAGE_MESSAGE)
