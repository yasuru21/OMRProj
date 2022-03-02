import numpy as np 
import random
# attempt at hamming distance (may or may not be used depending on what template matching we do)
class hamming:  
    def hamming_distance(self,image,template):
        image = np.array(image)
        template = np.array(template)
        
        width = image.shape[1] - template.shape[1] + 1
        height = image.shape[0] - template.shape[0] + 1
        result = np.empty((height,width))
        
        for i in range(height):
            for j in range(width):
                result[i,j] = np.abs(np.sum(np.subtract(image[i:i+template.shape[0],j:j+template.shape[1]],template)))
        c = (255*(result - np.min(result))/np.ptp(result)).astype(int) 
        return c

#hamming_distance()