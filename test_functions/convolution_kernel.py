import numpy as np 
import random

class kernelOperations: 

    # This section covers problems #3,4 on assignment1 PDF
    
    def __init__(self):
        self.randomInit = 0

    def rgb2gray(self, rgb):
        r = rgb[:,:,0]
        g =  rgb[:,:,1]
        b =  rgb[:,:,2]
        gray_color = 0.2989 * r + 0.5870 * g + 0.1140 * b
        return gray_color

    def seperableKernel(self, im, hx, hy):
        
        image_array = np.array(im)
        nums = hy.shape[1]
        mid_point = int(np.floor(n/2))
        array = np.pad(image_array, mid_point, mode='constant')
        h, w = array.shape
        temp_img = np.random.randn(h-(2*mid_point), w)
        for i in range(h-nums+1):
            for j in range(w):
                temp = array[i:i+nums,j].reshape(nums,1) * hx.T 
                temp_img[i,j] = np.abs(np.sum(temp))
        div_fac = np.sum(hx.T*hy)
        if div_fac==0:
            divisionFactor = nums
        output_img = np.random.randn(temp_img.shape[0], temp_img.shape[1]-(2*mid_point))

        for i in range(temp_img.shape[0]):
            for j in range(temp_img.shape[1]-nums):
                temp = temp_img[i,j:j+nums] * hy
                output_img[i,j] = int((np.abs(np.sum(temp)))/(divisionFactor))
        output_img = output_img.astype(int)
        output_img = np.where(output_img>255,255,output_img)
        output_img = np.where(output_img<0,0,output_img)
        
        return output_img

    def seperableSobelX(self):
        hx = np.array([[1,0,-1]])
        hy = np.array([[1,2,1]])
        return hx,hy

    def seperableSobelY(self):
        hx = np.array([[1,2,1]])
        hy = np.array([[-1,0,1]])
        return hx,hy
