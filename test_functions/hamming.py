import numpy as np 
import random
# attempt at hamming distance (may or may not be used depending on what template matching we do)
class hamming:  
    def hamming_distance(self,im,temp):
        im = np.array(im)
        temp = np.array(temp)
        
        width = im.shape[1] - temp.shape[1] + 1
        height = im.shape[0] - temp.shape[0] + 1
        area = width * height
        
        result = np.empty((height,width))
        test1 = area * im / temp
        for i in range(height):
            for j in range(width):
                result[i,j] = np.abs(np.subtract(im[i:i+temp.shape[0],j:j+temp.shape[1]],temp))
        c = (255*(result - np.min(result))/np.ptp(result)).astype(int) 
        return c

