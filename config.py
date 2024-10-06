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

WIDTH = 100000
HEIGHT= 100000

LARGE_WIDTH=10
LAREG_HEIGHT=10
# Compression settings for HDF5
COMPRESSION_LEVEL = 4  # Level 4 compression (0: no compression, 9: max compression)


# Update to handle different image sizes as well, such as 10x10 for testing
SMALL_WIDTH = 10
SMALL_HEIGHT = 10

# Dyed regions for small image (can be updated for different configurations)


# These all are for 10 values

#     #False
#     image[0:10, 0:10]=255 #full white
#     image[5:6, 9:10]=0  #little black


#False more white rgions very small black region
DYED_REGIONS = [
    # NOTE: YOU CAN CHANGE HERE ROWS AND COLUMS TO CHANGE THE WHITE AREA
    (0, 10, 0, 10, 255),  # White region
    (5,6,7,10, 0)
]


PARASITE_REGIONS =[
    # NOTE: YOU CAN CHANGE HERE ROWS AND COLUMS TO CHANGE THE WHITE AREA
    (0, 10, 0, 5, 255),  # White region

]

# # Different Pasite region less than 50
# PARASITE_REGIONS =[
#     # NOTE: YOU CAN CHANGE HERE ROWS AND COLUMS TO CHANGE THE WHITE AREA
#     (0, 10, 0, 5, 255),  # White region
#      (1,7,9,10, 255)
# ]