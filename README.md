# a1-group1 # 

## Problem: ##
Our task for this assignment is to create an OMR (Optical Music Recognition) program to analyze a portion of a musical score and accurately give a symbolic representation of the music as the output.

Our program must be able to analyze the notes on the staff from a musical score and then be able to identify the musical note and symbolically represent it.

## Running The File: ##
There are two commands to run our program, depending on which image you want to use. 

To run the program on any of the provided test images, within your terminal type: 
	py    main.py    “test-images/file_name.png”

To run the program on your own image, type:
	py    main.py   “ path_to_your_image/file_name.png”

## Initial Approach: ##
Before attempting to locate and classify the notes in the image, we first familiarized ourselves with the basic operations of convolution and edge detection. To do so, we wrote code specifically to perform a single convolution of an image with a given kernel, being sure to account for different sized images and even allowing for an arbitrary “stride” parameter that would be able to convolve the kernel with selected ranges, as we believed this might be useful for ignoring whitespace between staves. We then performed edge detection using a single convolution with a Laplacian kernel on a gray-scaled version of the music sheet. We discovered no Gaussian blur was needed before convolution because of the black-or-white nature of the images. After we successfully achieved edge detection, we implemented a Hough Transformation on the resulting image, but found our program was identifying extraneous lines. So, we opted to use a Sobel Operator to perform edge detection instead, which led us directly into the implementation that now stands as our final solution. These initial attempts and their results can be found in the old_testing_functions and old_test_images folder, respectively. 

## Final Solution: ##
To be able to accurately represent the musical score in our program, we implemented a combination of 5 classes along with a main file for collecting those classes and giving an output. More details on each file and what is done within is outlined below. 

### Convolve/Kernel Operations: ###
In this section we write functions to convert input image to grayscale and then colvolve it with Sobel kernels separately.

### Hough Transform: ###

- This method consisted of utilizing said images above and finding the staph lines within the input image, reformatting the size of templates for efficiency, and writing a function that spits out the image with results. 
- The lines are drawn based on the rule that every staph line is of equal distance from each other which allows for a good way to predict where they would be at. Template is resized based on the template that is detected; changes scale for each symbol. (eight-rest,quarter-rest, etc)
- Final results utilizes all said work above as well as all of the other classes that we created and spits out everything needed for results.  (ie. image with notes seen, .txt file)

### Dictionary for Reading Sheet: ###

- This file simply associates the letters of notes with locations relative to the detected staves. 
	+ We first distinguish between notes that are located directly on a staff line or in between them.
	+ Then, we simply store the notes in a dictionary according to how far away they are from the current line, taking into account the space between the lines that is generated as part of the Hough Transform above.

### Hamming Distance: ###

- This file takes the hamming distance between the input image and template image given:
	+ It is done by converting each image to an array using numpy and getting a resulting array from that. Using numpy, we then take the result and subtract it by the template pixels to get the difference between the two
	+ We found that we would rather use edge/naive detection to match between the two and didn’t end up taking this function any farther.

### Template Matching: ###
- This section is quite possibly the most important part of the assignment and required a lot of outside sources and brainstorming to complete
- ***Scoring****
	+ We introduce a function to initialize the way that we are going to go about scoring for accuracy. We do this by looking at the amount of overlap between the detection areas and say that when it passes a certain point to say that they contain the same object. 
- ***Naive Matching****
	+ We implemented a naive way of template matching (as referenced in A1.pdf) that essentially finds how similar a region of the input image is to the template in order to match each symbol. 
- ***Edge Matching****
	+ We also implemented a template matching in the form of edge matching. This method gets the edges from an image and compares them using matrix algebra. Similar to above we use these values to discern whether they match or not. 
	
### Main.py: ###

## Results: ##

## References: ##
Fakhfakh, Sana. “Image Retrieval Based on Using Hamming Distance.” 2015, p. 8, https://pdf.sciencedirectassets.com/280203/1-s2.0-S1877050915X00342/1-s2.0-S1877050915035012/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQDjUiNvn9k1FP7ZRpx0SjAKS6c9rOsNVBzkwyrAGInalAIhAPE3AZ6XqQmlX.

Rosebrock, Adrian. “Building an Image Search Engine: Defining Your Similarity Metric (Step 3 of 4).” PyImageSearch, 17 February 2014, https://pyimagesearch.com/2014/02/17/building-an-image-search-engine-defining-your-similarity-metric-step-3-of-4/. Accessed 2 March 2022

B-457 Lecture Slides/Google Cloud

 



