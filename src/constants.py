# config.py

# Directory structure
HDF5_DIR = "./10Img"
PNG_DIR = "./10Img"

# Image dimensions (modifiable)
WIDTH = 100000  # Can be updated based on need
HEIGHT = 100000  # Can be updated based on need

# Compression settings for HDF5
COMPRESSION_LEVEL = 4  # Level 4 compression (0: no compression, 9: max compression)

# Regions for modifying images
MODIFY_REGIONS = {
    "parasite": [(10000, 50000, 20000, 50000, 255), (10000, 30000, 50000, 70000, 0)]
}

# Update to handle different image sizes as well, such as 10x10 for testing
SMALL_WIDTH = 10
SMALL_HEIGHT = 10

# constants.py
WHITE = 255  # White pixel value
BLACK = 0    # Black pixel value

