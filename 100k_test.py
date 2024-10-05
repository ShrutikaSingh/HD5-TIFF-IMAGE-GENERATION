import numpy as np

import time
from numba import njit, prange
import concurrent.futures

import h5py

hdf5_dir = "./K100img"

def check_hdf5_contents(file_path):
    try:
        with h5py.File(file_path, 'r') as f:
            print(f"Available datasets in {file_path}: {list(f.keys())}")
    except Exception as e:
        print(f"Error: {e}")

# Check the original file
check_hdf5_contents(f'{hdf5_dir}/parasite.h5')
check_hdf5_contents(f'{hdf5_dir}/dyed.h5')

# Optimized function using Numba for fast computation
@njit(parallel=True)
def calculate_dyed_area(original_image, dyed_image):
    dyed_area_inside = 0
    parasite_area = 0

    # Parallel loop to count parasite area and dyed area inside the parasite
    for i in prange(original_image.shape[0]):
        for j in range(original_image.shape[1]):
            if original_image[i, j] == 1:  # Parasite region
                parasite_area += 1
                if dyed_image[i, j] == 1:  # Dyed region inside parasite
                    dyed_area_inside += 1

    return parasite_area, dyed_area_inside

def has_cancer_parallel(original_image, dyed_image):
    """Determine if the parasite has cancer based on images using optimized parallel code."""
    start_time = time.time()

    # Calculate the parasite area and dyed area inside using parallelized function
    parasite_area, dyed_area_inside = calculate_dyed_area(original_image, dyed_image)

    if parasite_area == 0:
        print("No parasite detected.")
        return False

    # Calculate the ratio of dyed area to parasite area
    ratio = dyed_area_inside / parasite_area

    # Determine if the parasite has cancer
    result = ratio > 0.1

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Print the execution time and other details
    print(f"Execution time for 10 by 10 img: {elapsed_time:.6f} seconds")
    print(f"Parasite area: {parasite_area}")
    print(f"Dyed area inside parasite: {dyed_area_inside}")
    print(f"Dyed to parasite area ratio: {ratio:.2f}")
    print(f"The parasite has cancer: {result}")

    return result

def load_h5_data_parallel(file_path, dataset_name):
    """Load HDF5 data in parallel using a thread pool."""
    with h5py.File(file_path, 'r') as f:
        dataset = f[dataset_name]

        # Split the data into chunks and load in parallel using threads
        def load_chunk(chunk_index):
            return dataset[chunk_index]

        num_chunks = dataset.shape[0]
        chunk_size = dataset.shape[0] // 8  # Adjust based on available threads

        # Load data in parallel
        with concurrent.futures.ThreadPoolExecutor() as executor:
            data = np.vstack(list(executor.map(load_chunk, range(0, num_chunks, chunk_size))))

    return data

def main():
    # Define the file paths and dataset names
    original_file = f'{hdf5_dir}/parasite.h5'
    dyed_file = f'{hdf5_dir}/dyed.h5'
    dataset_name_original = '/parasite'
    dataset_name_dyed = '/dyed'

    # Load microscope data in parallel
    print("Loading original image data...")
    original_image = load_h5_data_parallel(original_file, dataset_name_original)

    print("Loading dyed image data...")
    dyed_image = load_h5_data_parallel(dyed_file, dataset_name_dyed)

    # Convert images to binary (1 for relevant pixels, 0 for background)
    original_binary = (original_image == 0).astype(np.uint8)  # Black (0) indicates the parasite area
    dyed_binary = (dyed_image == 0).astype(np.uint8)  # Black (0) indicates dyed cancer area

    # Check for cancer using the optimized parallel function
    print("Processing images to check for cancer...")
    has_cancer_result = has_cancer_parallel(original_binary, dyed_binary)
    print(f"The parasite has cancer: {has_cancer_result}")

if __name__ == "__main__":
    main()
