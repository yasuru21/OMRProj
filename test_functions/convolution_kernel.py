import numpy as np 
import random

class kernelOperations: 

    # This section covers problems #3,4 on assignment1 PDF
    
    def __init__(self):
        self.randomInit = 0

    def rgb2gray(self, rgb):
        r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
        gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
        return gray

    def seperableKernel(self, im, hx, hy):
        
        im_arr = np.array(im)
        n = hy.shape[1]
        midPt = int(np.floor(n/2))
        arr = np.pad(im_arr, midPt, mode='constant')
        h, w = arr.shape
        tempImg = np.random.randn(h-(2*midPt), w)
        # print(tempImg.shape)
        for i in range(h-n+1):
            for j in range(w):
                temp = arr[i:i+n,j].reshape(n,1) * hx.T
                # tempImg[i,j] = int((np.sum(np.abs(temp)))/(divisionFactor)) 
                tempImg[i,j] = np.abs(np.sum(temp))
        divisionFactor = np.sum(hx.T*hy)
        if divisionFactor==0:
            divisionFactor = n
        outImg = np.random.randn(tempImg.shape[0], tempImg.shape[1]-(2*midPt))

        # print(outImg.shape)
        for i in range(tempImg.shape[0]):
            for j in range(tempImg.shape[1]-n):
                temp = tempImg[i,j:j+n] * hy
                outImg[i,j] = int((np.abs(np.sum(temp)))/(divisionFactor))
        outImg = outImg.astype(int)
        outImg = np.where(outImg>255,255,outImg)
        outImg = np.where(outImg<0,0,outImg)
        
        return outImg

    def seperableSobelX(self):
        hx = np.array([[1,0,-1]])
        hy = np.array([[1,2,1]])
        return hx,hy

    def seperableSobelY(self):
        hx = np.array([[1,2,1]])
        hy = np.array([[-1,0,1]])
        return hx,hy
