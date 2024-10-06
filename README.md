# DragonFruit.ai Assesment

### The Project have code based Python Class Structure


| Folder/File Name                              | Description                   |
|-----------------------------------------------|-------------------------------|
| `100KImg`                                    | Folder for 100K images        |
| `10Img`                                      | Folder for 10 images          |
| `HD5`                                        | Folder for HD5 files          |
| `Tiff`                                       | Folder for TIFF files         |
| `__pycache__`                                | Folder for cached Python files |
| `dyed_large_image_generation.py`             | Script for generating large dyed images |
| `dyed_small_image_generation.py`             | Script for generating small dyed images |
| `cancer_test.py`                             | Script for cancer test        |
| `main.py`                                    | Main application script       |
| `requirements.txt`                           | List of project dependencies   |
| `README.md`                                  | Documentation file            |
| `constants.py`                               | File for constant variables    |
| `config.py`                                  | Configuration file            |
| `messages.py`                                | File for message handling     |
| `utility.py`                                 | Utility functions file        |
| `venv`                                       | Virtual environment folder     |
| `parasite_large_image_generation.py`         | Script for generating large parasite images |
| `parasite_small_image_generation.py`         | Script for generating small parasite images |
| `src`                                        | Source code directory         |


**Steps for running this Code**
### Installation

Clone the repository and navigate to the project directory:
```bash
git clone https://github.com/ShrutikaSingh/HD5-TIFF-IMAGE-GENERATION.git
```

```
python3 -m venv venv  # on Windows, use "python -m venv venv" instead

. venv/bin/activate   # on Windows, use "venv\Scripts\activate" instead

pip install -r requirements.txt
```

***Run the code***

```
python main.py
```

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Implementation Details

## Thought Process

1. **Initial Doubts:**
   - **Flow of Dye**: Should I consider only the dye inside the body or also if it flows outside?
   - **Edge Cases**: Uncertainty about cases where the dye extends outside the body.
   - **Image Shape**: The shape of parasite as well as dye was mentioned that it can be any random shape but The pixels were unclear—would the pixel be square? Or was the question asking me to consider cases where a square pixel might not be fully filled? 
   
   <img width="36" alt="image" src="https://github.com/user-attachments/assets/76354f86-c8ba-40ae-b5b7-3e2841fcbf25">

     

2. **Problem Understanding:**
   - I reread the problem statement carefully two-three times.
   - Then prepare a diagram to understand it fully using google docs
   - <img width="446" alt="image" src="https://github.com/user-attachments/assets/a7020f83-6376-4b8e-99bf-665cbba5f8a8">

   - **Key Insight**: For detecting cancer, I  needed to focus on the dyed area in the dyed image just considering only those areas in which parasite was present in parasite image and ignore any dye outside the parasite area in dyed image.

3. **Initial Research:**
   - I began researching **microscopic image formats** and came across useful documents:
   - Just searching goolgle which is [ microscopic image Formats](https://www.google.com/search?q=microscopic+image+formats&rlz=1C5GCEM_enUS1111US1113&oq=microscopic+image+formats&gs_lcrp=EgZjaHJvbWUqBggAEEUYOzIGCAAQRRg7MgYIARBFGEAyCAgCEAAYFhgeMgoIAxAAGA8YFhgeMg0IBBAAGIYDGIAEGIoFMg0IBRAAGIYDGIAEGIoFMg0IBhAAGIYDGIAEGIoFMg0IBxAAGIYDGIAEGIoF0gEIMTU3MGowajeoAgCwAgA&sourceid=chrome&ie=UTF-8))
          - Most of the results showed Tiff Format
          - But some mentioned that HD5 is better format
   - So I began my research to find out the differences
        
        - [Microscoptic Image Different File Formats](https://bioimagebook.github.io/chapters/1-concepts/6-files/files.html)
        - [Things to know about Microscopy Formats](https://colocalizer.com/microscopy-image-file/)
        - [HDF5 Formta For Microscopic Image](https://svi.nl/HDF5)
        - [Biological Image Formats with HDF5](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3016045/)
   - After understanding these formats, I used ChatGPT to clarify which format, **HDF5** or **TIFF**, would be better for storing microscopic images.

4. **Conclusion: HDF5 vs TIFF**
   - **Use HDF5 if:**
     - You need to handle multiple datasets (e.g., images, sensor data, annotations) in a single file.
     - You require **random access** to specific regions of large images or need to efficiently handle sparse data.
     - You plan to store **complex metadata** or need an expandable dataset structure.
     - Your workflow involves **scientific computing**, where HDF5 is natively supported.
   - **Use TIFF if:**
     - You only need to store **single images** or small sets of images.
     - You need a **widely-supported format** for general-purpose image processing or visualization.
     - You don’t need extensive metadata or hierarchical data structures.
     - Your images are relatively simple, and **compression** methods like LZW are sufficient for your use case.

5. **Realization After Research:**
   - Despite LLMs (like ChatGPT and Gemini) recommending HDF5, many Google articles preferred TIFF for microscopy images.
   - I decided to trust Google and create a small **10x10 TIFF image** to test it out.

6. **Understanding TIFF Images:**
   - **Compression Techniques**:
     - TIFF supports multiple compression methods, including:
       - **LZW** (Lossless)
       - **JPEG** (Lossy)
       - **Deflate** (Lossless)
     - TIFF is effective for compressing images with large uniform regions, such as microscopic images.

7. **Understanding TIFF Images:**
   - **Compression Techniques**:
     - TIFF supports multiple compression methods, including:
       - **LZW** (Lossless)
       - **JPEG** (Lossy)
       - **Deflate** (Lossless)
     - TIFF is effective for compressing images with large uniform regions, such as microscopic images.


8. **Understanding and Applying different optimisation techniques mage Processing Optimizations**

   1. **Numba for JIT Compilation**:
      - Numba, the JIT (Just-In-Time) compilation, enhances performance via Just-In-Time compilation and parallel execution.
   
   2. **Pre-allocated Memory**:
      - Allocates memory upfront, which is more efficient in the sense that reused memory does not need to be reallocated at the time when the program is running.
   
   3. **Concurrent File I/O**:
      - Utilizes the `ThreadPoolExecutor` so that I/O tag on reading files is minimized, whereas I/O concurrency of file writing is improved.
   
   4. **Progress Monitoring**:
      - Employs TQDM to give progress indications in real-time, thus increasing user experience.
   
   5. **Performance Timing**:
      - Monitors execution times of specific regions to detect where the bottleneck is.
   
   6. **Parallel Loop Execution**:
      - The operation of parallel processing on large arrays is done concurrently via `prange`, which dramatically improves CPU utilization.
   
   7. **In-place Image Modifications**:
      - This is the direct modifiable of the array data for memory saving and for better performance.
   
   8. **File Compression**:
      - Reducing the size of a file while maintaining or improving its speed can be achieved by zipping or compressing HDF5 files during storage.


8. **Performing Experiment for finding which image would be better for generatioin and storing between TIFF & HD5:**
   - <img width="608" alt="image" src="https://github.com/user-attachments/assets/46c47b18-a13b-43bb-8275-64df1041891d">

   - **Result OF TIFF & HD5**:
       - **For 10 * 10 Img**
         <img width="809" alt="image" src="https://github.com/user-attachments/assets/3c8606fd-4933-47ab-8897-f048b50b1618">
       - **For 100000 * 100000 Imh**
       - <img width="810" alt="image" src="https://github.com/user-attachments/assets/b0438e09-22f5-4933-bb85-148159bae9d2">


   - **Conclucion After perfoming the Experiment mentioned in detailed below** (Lossless)
     - **HD5 is Good For Generating Microscopic image as it to 18-11 = 9 seconds less time than TIFF Images Geneartion with all the optimisation processes mentioned above as well as for storing large size image**


## How to Run a Specific Example Application?

**Before run a specific example application, make sure you have activated the virtual enviroment.**

For example, if you want to run the Hello application, just execute these commands:

```bash
cd hello
flask run
```

10. **After Perfoming the above experiment for both TIFF & HD5**
    - **I decided to use 100000k by 100000k HD5 images for Checking the presence of cancer***

# PROCEDURES, LOGIC, CODE  & OPTIMISATION TECHNIQUES EXPLAINATION




## First Steps For Understaing Image:**

   - I generated **two basic TIFF images** (10x10) without optimization.

        ## **WHY 10*10?**

     - So I had to do two tasks before moving one
        - **1st Sub Task**: To conclued which format to chose hd5 or tiff by understading the actual memory used by them and also by examining the processing time of each image
        
        - **2nd Sub Task**: To visualise the image , since we cannot convert 100000 * 100000 image to PNG format, so I though lets create 10*10 image and then i will verify it on 10 * 10 images and using that image pixels i will scale for the 100000 * 100000 image
           
           - I added a function to convert the images to **PNG** format, allowing me to visually inspect the **parasite** and **dyed** images.

             ## Methods Used For TIFF Image Generation and Compression Process For 10*10 Images
      
               1. **Created small 10x10 TIFF images:**
                  - Defined the image size as 10x10 pixels and generated a black image (all zeros) using NumPy arrays to simulate pixel data for TIFF images.
                  
               2. **Generated the first TIFF image (original):**
                     - Divided the left half of the 10x10 image into white (255) and the right half as black (0) to simulate a basic binary image. This image was saved as `original.tiff` using LZW compression for efficient file storage.
               
               3. **Generated the second TIFF image (dyed):**
                     - Modified specific sections of the original image to create patterns simulating a dyed region. The image was saved as `dyed.tiff` with LZW compression to optimize the file size.
               
               4. **TIFF to PNG conversion:**
                      - Implemented a conversion function to convert the TIFF images (`original.tiff` and `dyed.tiff`) to PNG format. This was useful for compatibility with other image processing tools or viewers that support PNG. 
               
               5. **Applied compression (LZW):**
                     - The LZW compression technique was chosen to reduce the file size while preserving image quality, ensuring efficient storage and handling of the TIFF images.


             ## Methods Used For HD5 Image Generation and Compression Process For 10*10 Images
       

            ## PNG Format Coverted image for both TIFF and HDF Format 

             ### Parasite Example Image (Original Parasite)
             <img width="214" alt="image" src="https://github.com/user-attachments/assets/0616669c-6fd1-4f9d-83d8-78388a4705a5">
                  
                
             ### Dyed Example Image  (Cancerous)
             <img width="226" alt="image" src="https://github.com/user-attachments/assets/14763a8e-b3ec-4820-be10-85ac576e4849">
   
             ### Dyed Example Image  (Non Cancerous)
             <img width="204" alt="image" src="https://github.com/user-attachments/assets/24962019-1a39-4e7a-a1f3-6b4d80959deb">

           


            ## Results For 10*10 image of Both TIFF and HDF for above shape
      
            ### Processing time for generating 10 * 10 TIFF Img is around 0.06 seconds
            <img width="1032" alt="image" src="https://github.com/user-attachments/assets/222aad48-c169-4086-bb26-bdcaaab9796b">


            ### Memory used by 10*10 is around 160 bytes 
            <img width="507" alt="image" src="https://github.com/user-attachments/assets/8b7144cf-c470-4aa4-bc9c-7968624fd8fa">

            ### Processing time for generating 10 * 10 HD5 Img is around 0.01 seconds
            <img width="1032" alt="image" src="https://github.com/user-attachments/assets/637b5be4-43bd-436a-9243-ed5e9bbb4927">

            ### Memory used by 10*10 is around 4 Kilobytes 
            <img width="582" alt="image" src="https://github.com/user-attachments/assets/60a72315-9c07-465b-ac7b-6b4683a154fd">


          ## Conslusion 
         <img width="759" alt="image" src="https://github.com/user-attachments/assets/bcb9323b-caaf-42a2-9add-5f29c35de3b6">

         - ***Hence, I noticed that though generation time for TIFF was little more than HD5 Formta but Still The Size of Tiff was much lesser than the HD5 Format***

         - So I decided To first go for geneartion of 100000 BY 10000 TIFF Images and SEE If any Optimisation Techniques for Generating TIFF Images can bring down  the processing time 

         

 
             


  **Seond Step**

  - I genereated HD5 images of (100000*100000) for Both parasite.h5 and dyed.h5 A
  - I genereated TIFF images of (100000*100000) for Both parasite.tiff and dyed.tiff


## 100K * 100K Image HD5 IMAGE FORMAT GENEARTION Using RLE for Optimising Image Storage

### GENERATION 
1. **Created large 100k x 100k HDF5 compressed images:** Created large images to simulate the microscope data of the parasite and dyed regions using the HDF5 format, which is optimized for handling large datasets. 

2. **Converted the images into dense NumPy matrices:** The generated images were converted into NumPy matrices for efficient processing and manipulation during analysis.Defined the image size as 100,000 x 100,000 pixels and generated white images (all pixels set to 255) using NumPy arrays to simulate the parasite and dyed regions.

3. **Defined an RLE encoder function:** The encoder function compresses the image by converting the 2D NumPy matrices into a compact run-length encoding (RLE) format, where consecutive pixel values are stored as a single value along with their count. This reduces storage requirements, especially for large, repetitive images.

    ***WHY RLE?***
   
- The encoder function compresses the image by converting the 2D NumPy matrices into a compact run-length encoding (RLE) format, where consecutive pixel values are stored as a single value with their count. This reduces the storage requirements, especially for large, repetitive images.

5. **Stored the encoded matrices in a dictionary:** The encoded parasite and dyed image data were stored in a dictionary

    ***WHY?***
      - To keep track of their compressed representations, reducing memory usage and improving access speed for further processing.
        

7. **Specified an RLE decoder function:** The decoder function takes the RLE-compressed data and reconstructs the original dense NumPy matrix on demand, allowing the retrieval of the full image for further analysis.

    ***WHY?***
      - To access back the full image 


### RESULTS WITHOUT ANY OPTMISATION TECHNIQUES FOR PROCESSING TIME FOR HD5

<img width="1270" alt="image" src="https://github.com/user-attachments/assets/c59b9e9b-dfc9-453c-a41a-3520cc787862">

#### SIZE OF GENERATED HD5 FORMAT AFTER RLE ARE 44 MEGA BYTES
<img width="999" alt="image" src="https://github.com/user-attachments/assets/d5d1eeac-6625-465b-b9fb-ba83f031c58c">


## 100K * 100K Image TIFF IMAGE FORMAT GENEARTION Using RLE for Optimising Image Storage
      
         1 Created a directory (`K100TiffImg`) to store the generated TIFF images and initialized timers to measure the process time.
           
         2 Defined a large image size (100,000 x 100,000 pixels) and created a NumPy array to hold pixel data, starting with a black image (all zeros).
           
         3 For the first image (parasite image), set the left half of the image to white (255), while the right half remained black (0), simulating a binary image.
           
         4 Converted the NumPy array to a TIFF image using the Python Imaging Library (PIL), and applied LZW compression to reduce file size, emphasizing efficient storage of such a large image.
           
         5 Saved the first generated TIFF image (`parasite.tiff`), capturing the time taken for this process.
           
         6 For the second image (dyed image), modified specific regions of the original NumPy array to create patterns of black and white, simulating dyed regions.
           
         7 Saved this modified image as another compressed TIFF file (`dyed.tiff`), again using LZW compression to optimize the file size.
           
         8 Used `tqdm` to display the progress of generating both TIFF images step-by-step.
           
         9 Tracked the time taken for each individual image generation and for the overall process, providing insights into performance and efficiency for large-scale TIFF image generation.
           
         10 Both TIFF images (parasite and dyed) were successfully compressed and generated as large 100k x 100k pixel files.


## RESULTS WITHOUT ANY OPTMISATION TECHNIQUES FOR PROCESSING TIME FOR TIFF Took 112 seconds

<img width="1222" alt="image" src="https://github.com/user-attachments/assets/3c680089-2cdb-45e5-a105-d7399de596d9">


### SIZE OF GENERATE TIFF IMAGES ARE 70 MEGA BYTES
<img width="986" alt="image" src="https://github.com/user-attachments/assets/a65f8047-e89c-423a-99d5-db6de72723d9">

# Optimizations Techniques Used for Faster Image Generation For BOTH HD5 & TIFF

## Numba JIT Compilation for Parallel Processing:
The `@njit()` function decorator from Numba with the argument `parallel=True` is used for the functions `modify_image()` and `modify_dyed_image()`. It allows Just-In-Time compilation and execution of that code to be parallelized over multiple CPU cores, increasing the performance of pixel modifications in large images.

## Efficient Memory Allocation with NumPy:
Pre-allocate large NumPy arrays, `parasite_image` and `dyed_image`, with pixel values ≈ 255 representing white pixels. This ensures that from the very beginning, memory management is optimized to avoid reallocation during processing, allowing direct modifications on the allocated space.

## Writing to Files Concurrently with ThreadPoolExecutor:
The HDF5 files in `parasite.h5` and `dyed.h5` are written in parallel using Python's `ThreadPoolExecutor`. This reduces the I/O bottleneck by enabling multiple threads to handle file writing tasks in memory concurrently, thus speeding up the process.

## Monitoring Progress with TQDM:
`Tqdm` is used to provide visual feedback on image processing and saving progress. Although it does not speed up the processing, it enhances the user experience by providing real-time progress updates during the operation.

## Timed Execution for Performance Measurement:
Custom timing functions are employed to measure the execution time of each stage, giving the user precise insights into where bottlenecks may exist and areas that could benefit from further optimization.

---

# MO Image Representation

## MO Image:
The MO image comprises a blob of black pixels, which occupies roughly 25% of the total area of the image. These pixels are continuous, meaning all black pixels are grouped together, and the white pixels form the complement of the black pixel set.

## Run Length Encoding (RLE):
The structure of the MO image makes it an ideal candidate for Run Length Encoding (RLE). RLE is a lossless compression scheme that encodes a binary image by counting consecutive pixels of the same color (black or white), thereby significantly reducing storage space for long sequences of uniform pixel values.

---

# DYE Image Representation

## DYE Image:
The dye image represents the region affected by a dye applied to the MO body. The dye may partially or fully cover the MO, and in some cases, may even spill beyond the MO body.

## Worst Case Scenario and Dense Array Representation:
In the worst-case scenario, the dye could cover 100% of the image, representing maximum leakage. Due to this complexity, the dye image is represented using dense NumPy arrays, which store pixel data in its raw form without compression. This representation is crucial as it allows for flexibility in modeling varying levels of dye coverage.




## Comparasion Of TIFF AND HD5 Generation with optimisation

### TIFF IMAGE GENERATION WITHOUT OPTIMZ TOOK took 18.27 sec ~ 18 sec
<img width="956" alt="image" src="https://github.com/user-attachments/assets/cf00788d-d7c2-4b0d-ba1d-aa4197bb0dff">

### TIFF IMAGE STORAGE For 100000 * 100000 pixel image is around 80Mega Bytes
<img width="641" alt="image" src="https://github.com/user-attachments/assets/b465552b-916e-46ef-8a1f-5e5661aad3f0">


### HD5 IMAGE GENERATION WITH OPTIMZATION TOOK 10.59 sec ~ 11 sec
<img width="843" alt="image" src="https://github.com/user-attachments/assets/bdbe192b-02e7-48be-843b-b01d8777ef90">

## HD5 IMAGE STORAGE For 100000 * 100000 pixel image 9Giga Bytes

<img width="636" alt="image" src="https://github.com/user-attachments/assets/e724dda0-d951-4010-a7ad-275e7cdecd3a">



# CONCLUSION OF TIFF & HD5

### For 10 * 10 Img
<img width="809" alt="image" src="https://github.com/user-attachments/assets/3c8606fd-4933-47ab-8897-f048b50b1618">

### For 100000 * 100000 Imh
<img width="813" alt="image" src="https://github.com/user-attachments/assets/629a2fff-5ef8-49e4-9213-e19571d203cb">

## HD5 is Good For Generating Microscopic image as it to 18-11 = 9 seconds less time than TIFF Images Geneartion with all the optimisation processes mentioned above as well as for storing large size image

## Comparison of TIFF and HDF5

### HDF5 Advantages:
- **Efficient Handling of Large Datasets:** HDF5 supports multiple datasets, such as images and annotations, in a single file.
- **Faster Processing:** HDF5 allows random access to specific regions in large images.
- **Better for Scientific Computing:** If your workflow involves scientific computing or complex metadata, HDF5 offers more flexibility.

### TIFF Advantages:
- **Widely Supported Format:** TIFF is a standard format for image processing and visualization.
- **Compression Options:** TIFF supports lossless and lossy compression, which makes it effective for compressing uniform images.

### Performance Summary:
- **TIFF:** Generated 100k x 100k images in approximately 0.79 seconds with a file size of 70 MB.
- **HDF5:** Generated 100k x 100k images in 0.01 seconds without optimization, with a file size of around 44 MB.

## Optimizations

### Applied Techniques:
- **Parallel Image Generation:** Using `ThreadPoolExecutor`, images are generated and written in parallel, reducing total processing time.
- **Compression for HDF5:** Used compression options like `compression_opts=4` to reduce file sizes without compromising speed significantly.
- **Memory Efficiency:** By handling large datasets efficiently in memory, the project reduces memory overhead during the generation process.

### Optimized Results:
- **TIFF:** 100k x 100k images took 8.17 seconds to generate with optimizations.
- **HDF5:** After optimizations, large HDF5 images took 8.17 seconds, but the file size was reduced to 12 MB.



- **TIFF** images are larger but are more widely supported and are ideal for simple use cases.
- **HDF5** images offer faster generation times and smaller file sizes, making them suitable for handling complex, large-scale datasets.
- The project demonstrates the trade-off between processing time and file size, offering insights into when each format should be used.


# CANCER RESULTS VERIFICATION

***CANCER Positive***

<img width="368" alt="image" src="https://github.com/user-attachments/assets/d244d8ab-7fd9-4de1-81bb-46536546ff62">

<img width="368" alt="image" src="https://github.com/user-attachments/assets/efe3c752-cb54-4954-b47d-00f3961d2474">

<img width="528" alt="image" src="https://github.com/user-attachments/assets/5572f035-0378-4b0c-8da7-ab8c9a2e2892">




-----
**CANCER Negative**

<img width="368" alt="image" src="https://github.com/user-attachments/assets/c7615fa2-8be2-409b-b57a-7e865f68e3da">

<img width="368" alt="image" src="https://github.com/user-attachments/assets/efe3c752-cb54-4954-b47d-00f3961d2474">


## Tested Image examples

***Parasitic Microscopic Image Used for this Case***

<img width="368" alt="image" src="https://github.com/user-attachments/assets/53b041b5-e1dc-4173-b944-298d3c7beb40">

***Dyed Images Caner Positive for above Parasitic Image***

<img width="368" alt="image" src="https://github.com/user-attachments/assets/75d7489d-6cab-4ca5-9312-7ba24b692e72">

<img width="368" alt="image" src="https://github.com/user-attachments/assets/c0ce79ac-cbda-4c8f-9246-be0afc1a36ae">

<img width="368" alt="image" src="https://github.com/user-attachments/assets/e3354e1d-a98a-43e5-a0b2-d7d71709e70a">

***NON CANCEROUS***

<img width="368" alt="image" src="https://github.com/user-attachments/assets/a624e5d3-2297-47bd-a1c7-17bf77514fe6">

--------------------------- ----------------------------------------------------
# Running the code in your Local Machiene

## Prerequisites

 ## Main Folder Structure with Class Based Implementation 
<img width="685" alt="image" src="https://github.com/user-attachments/assets/3b838d17-7b13-4313-8935-2288508f4401">

- Python 3.x
- Libraries: h5py, PIL, NumPy, tqdm, concurrent.futures, numba

## Installation

First, you need to clone this repository:
```bash
git clone https://github.com/ShrutikaSingh/HD5-TIFF-IMAGE-GENERATION.git
```
Clone the repository and navigate to the project directory:


Now, we will need to create a virtual environment and install all the dependencies:

```bash
python3 -m venv venv  # on Windows, use "python -m venv venv" instead
. venv/bin/activate   # on Windows, use "venv\Scripts\activate" instead
pip install -r requirements.txt
```

## Run the code

```bash
cd src
python main
```

<img width="516" alt="image" src="https://github.com/user-attachments/assets/d714a1ac-5135-45de-83c2-d13b4fd3e2ba">





## Other Utilities To Generate and Test different types of images generation Usage

### Generating TIFF Images
To generate small TIFF images (10x10 pixels), you can run the following script:

```bash
cd Tiff
python generate_10_tiff.py
```

This will generate four files in the 10TiffImg directory, including both parasite and dyed images. You can view the size and structure of the generated files:

```ls -lh 10TiffImg
```

### Generating HDF5 Images
To generate small HDF5 images (10x10 pixels), run:

```
cd HD5
python generate_10_hd5.py
```

This script will generate two HDF5 files (parasite.h5 and dyed.h5) inside the 10HDF5Img directory. Compression options are applied during file generation.

## Generating 100k x 100k Images
To generate large-scale 100k x 100k images using both formats, you can run the following commands:

For TIFF images:
```
cd Tiff
python generate_100k_tiff.py
```

## For HDF5 images:
``cd HD5
python generate_100k.py```

Both scripts will generate large images, and you can analyze the results using ls -lh to check file sizes and formats.


----------------------------------------------------------------------------------------------------------------------------

# Answers 

# Question 1

#### FIRST AFTER UNDERSTAING THE POINTS MENTIONED ABOVE, I GENERATED TWO KINDS OF IMAGES (also for q5)

#### 1)HD5 (RLE COMPRESSION) - for question 1

#### 2)TIFF (LZW COMPRESSION) - for question 5



### PART A) FOR BOTH HD5 & TIFF Storing format in support of question 1 & question 5, I chose the below different represtion for Parasite Microcopic image & Dyed Sensor Image


## Parasite Microscopic Image Data Structure for HDF5 and TIFF 

### 1. HDF5 Representation for Parasite Micro Scopic Image 

- Since the Parasite Micro Scopic Image has large blocks of contiguous black and white pixels occupying about 25% of the total are, RLE can efficiently encodes it by recording the number of pixels before a change in color (from white to black or black to white).  

- The parasite image is first created as a NumPy array, where the parasite region is modified using Numba for fast processing. 

- The image is represented by counting the number of pixels before a color change (from black to white or vice versa), processing the pixels from left to right and top to bottom. 
 
 - Each run of pixels is encoded using uint8 for small pixel runs and uint16 for longer runs. This will ensures a compact representation since longer runs can be efficiently stored with fewer elements. 
 
- Additionally, the size of the image (#rows and #cols) is encoded in a unit8-safe format, and **a check byte** is included to confirm the processing technique used (RLE). 


**Reason for Selection:**

**Contiguous Pixels**: 25% black pixels (blob) allow for efficient compression.
**Storage Efficiency:** RLE encodes sequences of the same pixel values, significantly reducing storage.

**Implementation Details:**

**Processing Order**: Pixels processed from left to right, top to bottom.
**Data Types:** Uses uint8 for short runs and uint16 for longer runs.
**Metadata:** Stores image dimensions and a check byte for RLE confirmation.



### 2. TIFF Representation for Parasite Micro Scopic Image (for Question 5)

- For TIFF ALSO, the Parasite Micro Scopic image is similarly generated and modified using NumPy and Numba for fast image modification.

-  The image is saved using ***LZW compression, a lossless format ideal*** for images with large uniform regions like the 
image. 

- It works by replacing repeated sequences of pixel values with shorter codes. As here, the Parasite Microcopic Image, contains large areas of contiguous pixels (e.g., black and white)


**Representation:** LZW Compression

**Reason for Selection:**

**Uniform Regions: **LZW compression is ideal for images with large blocks of uniform color.
**Lossless:** Maintains image quality without data loss.


**Implementation Details:**

**Processing Order:** Similar to HDF5, pixels processed left to right, top to bottom.
**Metadata:** Includes image dimensions and a check byte.

## DYE Image Data Structure for HDF5 and TIFF

### 3. HDF5 Representation (DYED SImage)

- The DYEd image is stored in its **dense NumPy array** form, representing the dye regions covering the Parasite Micro Scopic Image  image. 

- Since the dye pattern may cover irregular parts of the image, RLE is not suitable for this image type. 

- Instead, each pixel is stored as 1 bit (1 for a dyed pixel, 0 for a background pixel), which provides flexibility for handling different coverage patterns. 

- The image dimensions (#rows and #cols) are  encoded in a unit8-safe way, along with a check byte that confirms the processing technique used (dense array). 

**Representation:** Dense Array (1 Bit per Pixel)

**Reason for Selection:**

Irregular Patterns: Dye coverage may be inconsistent; dense representation allows flexibility.
Compactness: Storing each pixel as 1 bit (0 for background, 1 for dyed).

**Implementation Details:**

Metadata: Stores image dimensions and a check byte for processing confirmation.
Parallel Processing: Numba ensures efficient image modification.

### 4. TIFF Representation (DYEd Image)
- In the TIFF format, the DYEd image is saved with LZW compression, similar to the  image. 

-The image is processed with NumPy and modified using Numba to represent the dyed areas effectively. 

-The pixel data is stored as **1 bit per pixel** in the TIFF file, and the image dimensions and metadata are stored similarly to HDF5. 


Point 1: The DYE image uses a dense array representation, storing each pixel as 1 bit for maximum flexibility in representing complex dye patterns.

Point 2: The image dimensions (#rows and #cols) are encoded in a unit8-safe way, and a check byte is used to confirm the processing technique for future decoding.

**Representation:** LZW Compression

**Reason for Selection:**

Lossless Compression: Maintains quality, suitable for images with complex patterns.
Efficient Storage: Works well with the 1-bit pixel data representation.

**Implementation Details:**

Pixel Storage: Each pixel stored as 1 bit.
Metadata: Includes image dimensions and a check byte.

## PARTB) WORST CASE COMPLETIY


# Image Storage Analysis

## Image Size Calculations

| Image Type      | Compression Method     | Formula                                         | Size   |
|------------------|------------------------|-------------------------------------------------|--------|
| Parasite Image    | RLE (HDF5)            | Size RLE worst = 2 × (100,000 × 100,000)      | 20 GB  |
|                  | LZW (TIFF)            | Size LZW worst ≈ (100,000 × 100,000)          | 10 GB  |
| Dyed Image        | Dense Array (HDF5)    | Size dense worst = (100,000 × 100,000) / 8    | 1.25 GB|
|                  | LZW (TIFF)            | Size LZW worst ≈ (100,000 × 100,000) / 8      | 1.25 GB|


  
# Question2) Simulation code And Method


## **Methods Used  100000*100000 Images**

### Methods Used:


  
  1.  **Numba for JIT Compilation**:
         - Numba, the JIT (Just-In-Time) compilation, enhances performance via Just-In-Time compilation and parallel execution.

      ```
         @njit(parallel=True)
         def modify_parasite_image(image):
             """ Modify the entire parasite image by setting the left half to white. """
             for i in prange(height):
                 image[i, :width // 2] = 255  # Set the left half of the image to white
         
         @njit(parallel=True)
         def modify_dyed_image(image):
             """ Modify the entire dyed image with specified regions. """
  
   2. **Pre-allocated Memory**:
         - Allocates memory upfront, which is more efficient in the sense that reused memory does not need to be reallocated at the time when the program is running.
  
   3. **Concurrent File I/O**:
         - Utilizes the `ThreadPoolExecutor` so that I/O tag on reading files is minimized, whereas I/O concurrency of file writing is improved.

       ```with ThreadPoolExecutor(max_workers=2) as executor:
            executor.submit(write_hdf5, f'{hdf5_dir}/parasite.h5', 'parasite', parasite_image)
            executor.submit(write_hdf5, f'{hdf5_dir}/dyed.h5', 'dyed', dyed_image )
      ```
 
   4. **Progress Monitoring**:
         - Employs TQDM to give progress indications in real-time, thus increasing user experience like start and end timer.

          ``with tqdm(total=2, desc="Processing images") as pbar:```
         

   6. **Performance Timing**:
         - Monitors execution times of specific regions to detect where the bottleneck is.

        ```step_start = timer_start()
          modify_image(parasite_image)
          timer_end(step_start, "Image modification for 100K Parasite")
          
   7. **In-place Image Modifications**:
         - This is the direct modifiable of the array data for memory saving and for better performance.
 
   8. **File Compression using  GZIP Compression**:
         - Reducing the size of a file while maintaining or improving its speed can be achieved by zipping or compressing HDF5 files during storage.
         - GZIP compression with a lower compression level was applied to both `parasite.h5` and `dyed.h5` to reduce file size while maintaining fast write times.
   
   9. **Loading Data Paralleley**
        
           ```def load_h5_data_parallel(file_path, dataset_name):
             """Loading HDF5 data in parallel using thread pool."""
             with h5py.File(file_path, 'r') as f:
                 dataset = f[dataset_name]
         
                 # Split the data into chunks and load in parallel using threads
                 def load_chunk(chunk_index):
                     return dataset[chunk_index]
         
                 num_chunks = dataset.shape[0]
                 chunk_size = dataset.shape[0] // 8   # We can Adjust based on available threads
         
                 # Load data in parallel
                 with concurrent.futures.ThreadPoolExecutor() as executor:
                     data = np.vstack(list(executor.map(load_chunk, range(0, num_chunks, chunk_size))))
             return data```

 10. **RLE ENCODE with parallelization**
   - The RLE encode function's main role is to compress the original data (in this case, an image or array) into a more compact form by replacing consecutive runs of the same value with a pair of values: the pixel value and the count of consecutive pixels
   
   - How It Works: It iterates through the image or array and counts consecutive identical pixel values, storing them in the format [value, count].
Example: Instead of storing 100000 black pixels (0) individually, it would store them as [0, 100000], drastically reducing the storage size.

   - Why Needed: This function allows us to minimize the data size by compressing uniform areas (like large blocks of the same color in images), leading to efficient memory and storage usage.
   - ``` @njit(parallel=True) def rle_encode(img_array):
    rows, cols = img_array.shape
    rle_data = []
    
    prev_value = img_array[0, 0]
    count = 1

    # Add tqdm for progress tracking
    for r in tqdm(prange(rows), desc="Encoding RLE"):
        for c in range(cols):
            if (r == 0 and c == 0):  
                continue
            
            current_value = img_array[r, c]

            if current_value == prev_value:
                count += 1
            else:
                rle_data.extend([prev_value, count])
                prev_value = current_value
                count = 1

    rle_data.extend([prev_value, count]) 
    return rle_data```
 
11. **RLE Decode RLE with parallelization**
      - The RLE decode function is responsible for reconstructing the original data from its compressed form (RLE encoded format). It takes the compressed format and expands it back into the full image or array.

      - IT takes the encoded data (pairs of [value, count]) and converts it back into a full array by repeating each value according to its count. Example: If it reads [0, 100000], it will generate 100,000 black pixels (0), restoring the original image.
      - Why Needed: Without decoding, we cannot work with or visualize the original data. Decoding is essential to recover the full image or data set from its compressed state, especially when analysis or further processing requires the full data.

    ```@njit(parallel=True)
    def rle_decode(rle_data, shape):
    """Decodes an RLE encoded array to its original form."""
    array = np.zeros(shape, dtype=np.uint8)
    position = 0
    
    for i in range(0, len(rle_data), 2):
        value = rle_data[i]
        count = rle_data[i+1]
        
        # Fill in the positions with the given value
        array.flat[position:position+count] = value
        position += count
    
    return array
    ```
 

## MAIN CODE CLASS

```

class BASE64_ParasiteLargeImageGenerator:
    def __init__(self):
        self.image = np.zeros((HEIGHT, WIDTH), dtype=np.uint8)

    def generate(self):
        start_time = timer_start()

        # Modify image using Numba with prange for parallel execution
        modify_image(self.image)

        # Write to HDF5
        write_hdf5(f'{HDF5_100K_DIR}/parasite_large.h5', 'parasite_large', self.image, compression="lzf")

        timer_end(start_time, PARASITE_LARGE_IMAGE_MESSAGE)

class BASE64_ParasiteLargeDyedImageGenerator:
    def __init__(self):
        self.image = np.zeros((HEIGHT, WIDTH), dtype=np.uint8)

    def generate(self):
        start_time = timer_start()

        # Modify dyed image using Numba with prange for parallel execution
        modify_dyed_image(self.image)

        # Write to HDF5
        write_hdf5(f'{HDF5_100K_DIR}/dyed_large.h5', 'dyed_large', self.image, compression="lzf")

        timer_end(start_time, "Dyed large image processing")

 ```                    

# QUESTION 3) CODE FOR HAS CANCER

### Calculating overlapped areas with counts of 1

```
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
```

### Class CancerTest

```class CancerTest:
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
```


# Question4) Optimisation for hasCancer

### OTIMISATIONS
  ***Optimized function using Numba, spliiting into chunks and use & for Take Element Wise Product for fast computation
   
   ### Just Count 1, Use & Operator to Take Element Wise Product and sum them parrallel**
       
          ```def count_parasite_area_chunk(original_chunk):
                     return np.count_nonzero(original_chunk == 1).```
              
          ```def count_dyed_area_chunk(original_chunk, dyed_chunk):
               """""
               return np.count_nonzero((original_chunk == 1) & (dyed_chunk == 1))```
               
   ### using parallel processing***
               ```def has_cancer_parallel(original_image, dyed_image, num_workers=8):
               """using parallel processing.```

   ### Split the image into chunks for parallel processing
            ```chunks = np.array_split(np.arange(original_image.shape[0]), num_workers)```

   ### Use a ThreadPoolExecutor to parallelize the counting of parasite area and dyed area
              `with ThreadPoolExecutor(max_workers=num_workers) as executor:
   ## Submit tasks for counting parasite area in parallel
               parasite_futures = [executor.submit(count_parasite_area_chunk, original_image[chunk]) for chunk in chunks]
             
   ### Submit tasks for counting dyed area in parallel
            ```dyed_futures = [executor.submit(count_dyed_area_chunk, original_image[chunk], dyed_image[chunk]) for chunk in chunks]```
   ### Wait for results and sum them
            ``` parasite_area = sum(f.result() for f in parasite_futures)
            dyed_area_inside = sum(f.result() for f in dyed_futures)```
        
   ### Sum them parallely 
        ```parasite_area = sum(f.result() for f in parasite_futures)
        dyed_area_inside = sum(f.result() for f in dyed_future```
        
   ### Optimisation for Ration
       ````result = dyed_area_inside > ratio_threshold```
     
  # QUESTION 5)
  
  ANS - As explained in Question 1, **I have used RLE Compression FOR HD5 and LZW Compression for TIFF**
  
  
   ***HDF5 uses Run-Length Encoding (RLE) for compressing the Parasite Microscopic Image, which efficiently stores contiguous pixel blocks, and a dense array representation for the Dyed Image, storing each pixel as 1 bit.***
  
  ***TIFF, on the other hand, employs LZW compression, a lossless method ideal for images with repeated pixel values, efficiently compressing both the Parasite Microscopic and Dyed Images.***
  
  
  
## For an Image Dimension of 100000 * 100000 px:##

   ### Generation Time Without Optimisation:
      # TIFF Format: 100.2 sec
      # HD5 Format: 34.15 sec
      
   ### Generation Time With Optimisation:
   
      # TIFF Format: 7.27 sec
      # HD5 Format: 6.58 sec
   
   ### Memory Used:
   
      # TIFF Format: 83 MB
      # HD5 Format: 44 MB


**Conslucion After perfoming the Experiment (mentioned in detailed below)** 
     - HD5 is Good For Generating Microscopic image as it takes **7.27-6.58 = 0.69 seconds less time** than TIFF Images Geneartion with all the optimisation processes mentioned
     - Also HD5 almost half (83/44) memory than TIFF format for larger images 


# QUETSION 6

### **USED GOOGLE**

   - I began researching **microscopic image formats** and came across useful documents:
   - Just searching goolgle which is [ microscopic image Formats](https://www.google.com/search?q=microscopic+image+formats&rlz=1C5GCEM_enUS1111US1113&oq=microscopic+image+formats&gs_lcrp=EgZjaHJvbWUqBggAEEUYOzIGCAAQRRg7MgYIARBFGEAyCAgCEAAYFhgeMgoIAxAAGA8YFhgeMg0IBBAAGIYDGIAEGIoFMg0IBRAAGIYDGIAEGIoFMg0IBhAAGIYDGIAEGIoFMg0IBxAAGIYDGIAEGIoF0gEIMTU3MGowajeoAgCwAgA&sourceid=chrome&ie=UTF-8))
          - Most of the results showed Tiff Format
          - But some mentioned that HD5 is better format
 
### **ARTICLES & PAPERS & LLM** FOR UNDERSTANING DIFFERECE BETWEEN TIFF & HD5 FOR STORING IMAGES
   - So I began my research to find out the differences
   
        - [Microscoptic Image Different File Formats](https://bioimagebook.github.io/chapters/1-concepts/6-files/files.html)
        - [Things to know about Microscopy Formats](https://colocalizer.com/microscopy-image-file/)
        - [HDF5 Formta For Microscopic Image](https://svi.nl/HDF5)
        - [Biological Image Formats with HDF5](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3016045/)
   - After understanding these formats, I used ChatGPT to clarify which format, **HDF5** or **TIFF**, would be better for storing microscopic images.

### **OFFICIAL DOCUMETATION** OF
  - **prange**,
  - **njit** for parralisation @njit(parallel=True)

### **Chat GPT**
   - Used chat gpt for debugging and generating initial basic code structure


