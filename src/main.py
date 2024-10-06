# main.py

from parasite_small_image_generation import ParasiteSmallImageGenerator
from dyed_small_image_generation import DyedSmallImageGenerator
from parasite_large_generation import ParasiteLargeImageGenerator
from parasite_large_dyed import ParasiteLargeDyedImageGenerator
from small_image_test import SmallImageTest
from utility import convert_hdf5_to_png
from config import HDF5_10_DIR, PNG_10_DIR
import numpy as np

def main():
    # Generate small parasite and dyed images
    print("Generating small parasite images...")
    parasite_generator = ParasiteSmallImageGenerator()
    parasite_generator.generate()

    print("Generating small dyed images...")
    dyed_generator = DyedSmallImageGenerator()
    dyed_generator.generate()

    # Convert small HDF5 to PNG
    print("Converting small HDF5 to PNG...")
    convert_hdf5_to_png(f'{HDF5_10_DIR}/parasite.h5', f'{PNG_10_DIR}/parasite.png')
    convert_hdf5_to_png(f'{HDF5_10_DIR}/dyed.h5', f'{PNG_10_DIR}/dyed.png')

    # Load small images as binary for testing
    original_image = (parasite_generator.image == 0).astype(np.uint8)  # Black (0) indicates the parasite area
    dyed_image = (dyed_generator.image == 0).astype(np.uint8)  # Black (0) indicates dyed cancer area

    # Check for cancer in small images
    print("Checking for cancer in small images...")
    SmallImageTest.has_cancer(original_image, dyed_image)

    # Generate large parasite and dyed images
    print("Generating large parasite images...")
    large_parasite_generator = ParasiteLargeImageGenerator()
    large_parasite_generator.generate()

    print("Generating large dyed images...")
    large_dyed_generator = ParasiteLargeDyedImageGenerator()
    large_dyed_generator.generate()

    # Convert large HDF5 to PNG
    # print("Converting large HDF5 to PNG...")
    # convert_hdf5_to_png(f'{HDF5_10_DIR}/parasite_large.h5', f'{PNG_100K_DIR}/parasite_large.png')
    # convert_hdf5_to_png(f'{HDF5_10_DIR}/dyed_large.h5', f'{PNG_100K_DIR}/dyed_large.png')

    # Load large images as binary for testing
    original_large_image = (large_parasite_generator.image == 0).astype(np.uint8)
    dyed_large_image = (large_dyed_generator.image == 0).astype(np.uint8)

    # Check for cancer in large images
    print("Checking for cancer in large images...")
    SmallImageTest.has_cancer(original_large_image, dyed_large_image)

if __name__ == "__main__":
    main()
