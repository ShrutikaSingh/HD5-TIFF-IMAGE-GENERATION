# main.py

from parasite_small_image_generation import ParasiteSmallImageGenerator
from dyed_small_image_generation import DyedSmallImageGenerator
from small_image_test import SmallImageTest
from utility import convert_hdf5_to_png
from config import HDF5_DIR, PNG_DIR
import numpy as np

def main():
    # Generate small parasite and dyed images
    parasite_generator = ParasiteSmallImageGenerator()
    parasite_generator.generate()

    dyed_generator = DyedSmallImageGenerator()
    dyed_generator.generate()

    # Convert HDF5 to PNG
    convert_hdf5_to_png(f'{HDF5_DIR}/parasite.h5', f'{PNG_DIR}/parasite.png')
    convert_hdf5_to_png(f'{HDF5_DIR}/dyed.h5', f'{PNG_DIR}/dyed.png')

    # Load images as binary for testing
    original_image = (parasite_generator.image == 0).astype(np.uint8)
    dyed_image = (dyed_generator.image == 0).astype(np.uint8)

    # Check for cancer
    SmallImageTest.has_cancer(original_image, dyed_image)

if __name__ == "__main__":
    main()
