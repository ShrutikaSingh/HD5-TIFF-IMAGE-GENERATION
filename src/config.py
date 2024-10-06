# config.py
import os

# Directory structure
HDF5_10_DIR = "./10Img"
PNG_10_DIR = "./10Img"

HDF5_100K_DIR = "./100KImg"
PNG_100K_DIR = "./100KImg"

# Ensure directories exist
# Ensure directories exist
os.makedirs(HDF5_10_DIR, exist_ok=True)
os.makedirs(HDF5_100K_DIR, exist_ok=True)  # Create the large images directory
os.makedirs(PNG_10_DIR, exist_ok=True)
os.makedirs(PNG_100K_DIR, exist_ok=True)  #

# Image dimensions (modifiable)
WIDTH = 100000  # Can be updated based on need
HEIGHT = 100000  # Can be updated based on need

# Compression settings for HDF5
COMPRESSION_LEVEL = 4  # Level 4 compression (0: no compression, 9: max compression)


# Update to handle different image sizes as well, such as 10x10 for testing
SMALL_WIDTH = 10
SMALL_HEIGHT = 10

# Dyed regions for small image (can be updated for different configurations)
DYED_REGIONS = [
    # NOTE: YOU CAN CHANGE HERE ROWS AND COLUMS TO CHANGE THE WHITE AREA
    (1, 5, 5, 10, 255)  # White region
]


PARASITE_REGIONS =[
    # NOTE: YOU CAN CHANGE HERE ROWS AND COLUMS TO CHANGE THE WHITE AREA
    (1, 10, 0,5 , 255)  # White region
]