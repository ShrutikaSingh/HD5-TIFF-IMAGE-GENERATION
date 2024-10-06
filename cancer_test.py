# small_image_test.py

from utility import timer_start, timer_end
from numba import njit, prange
import numpy as np

@njit(parallel=True)
def calculate_dyed_area(original_image, dyed_image):
    dyed_area = 0
    parasite_area = 0
    for i in prange(original_image.shape[0]):
        for j in range(original_image.shape[1]):
            if original_image[i, j] == 1:
                parasite_area += 1
                if dyed_image[i, j] == 1:
                    dyed_area += 1
    return parasite_area, dyed_area

class CancerTest:
    @staticmethod
    def has_cancer(original_image, dyed_image):
        start_time = timer_start()
        parasite_area, dyed_area_inside = calculate_dyed_area(original_image, dyed_image)

        if parasite_area == 0:
            print("No parasite detected.")
            return False

        ratio = dyed_area_inside / parasite_area
        result = ratio > 0.1

        timer_end(start_time, "Checking for cancer")
        print(f"Parasite area: {parasite_area}")
        print(f"Dyed area inside: {dyed_area_inside}")
        print(f"Cancer detected: {result}")
        return result
