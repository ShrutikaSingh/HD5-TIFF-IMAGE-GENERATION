# parasite_large_dyed.py

import numpy as np
from config import WIDTH, HEIGHT, HDF5_DIR, DYED_REGIONS
from constants import WHITE, BLACK
from messages import DYED_LARGE_IMAGE_MESSAGE
from utility import write_hdf5, timer_start, timer_end

class ParasiteLargeDyedImageGenerator:
    def __init__(self):
        self.image = np.zeros((HEIGHT, WIDTH), dtype=np.uint8)

    def generate(self):
        start_time = timer_start()

        # Apply modifications from DYED_REGIONS in config.py
        for x_start, x_end, y_start, y_end, value in DYED_REGIONS:
            self.image[x_start:x_end, y_start:y_end] = value

        write_hdf5(f'{HDF5_DIR}/dyed_large.h5', 'dyed_large', self.image, compression="gzip")

        timer_end(start_time, DYED_LARGE_IMAGE_MESSAGE)
