# dyed_small_image_generation.py

import numpy as np
from config import SMALL_WIDTH, SMALL_HEIGHT, HDF5_10_DIR, DYED_REGIONS
from constants import WHITE, BLACK
from messages import DYED_SMALL_IMAGE_MESSAGE
from utility import write_hdf5, timer_start, timer_end

class DyedSmallImageGenerator:
    def __init__(self):
        self.image = np.zeros((SMALL_HEIGHT, SMALL_WIDTH), dtype=np.uint8)

    def generate(self):
        start_time = timer_start()

        # Apply modifications from DYED_REGIONS in config.py
        for x_start, x_end, y_start, y_end, value in DYED_REGIONS:
            self.image[x_start:x_end, y_start:y_end] = value

        # Save the modified image to HDF5
        write_hdf5(f'{HDF5_10_DIR}/dyed.h5', 'dyed', self.image, compression="gzip")

        # Timer end message
        timer_end(start_time, DYED_SMALL_IMAGE_MESSAGE)
