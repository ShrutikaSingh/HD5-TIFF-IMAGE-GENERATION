# parasite_small_image_generation.py

import numpy as np
from config import SMALL_WIDTH, SMALL_HEIGHT, HDF5_DIR, PARASITE_REGIONS
from constants import WHITE, BLACK
from messages import PARASITE_SMALL_IMAGE_MESSAGE
from utility import write_hdf5, timer_start, timer_end

class ParasiteSmallImageGenerator:
    def __init__(self):
        self.image = np.zeros((SMALL_HEIGHT, SMALL_WIDTH), dtype=np.uint8)

    def generate(self):
        start_time = timer_start()

        # Apply modifications from DYED_REGIONS in config.py
        for x_start, x_end, y_start, y_end, value in PARASITE_REGIONS:
            self.image[x_start:x_end, y_start:y_end] = value

        # Fill left half with white
        self.image[:, :SMALL_WIDTH // 2] = WHITE

        write_hdf5(f'{HDF5_DIR}/parasite.h5', 'parasite', self.image, compression="gzip")

        timer_end(start_time, PARASITE_SMALL_IMAGE_MESSAGE)
