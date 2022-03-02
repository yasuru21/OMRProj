import numpy as np
#Sobel operator for eventual template matcher
class Sobel:
    def __init__(self):
        self.randomInit = 0

    def rgb2gray(self, rgb):
        r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
        gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
        return gray

    def seperableSobelX(self):
        hx = np.array([[1,0,-1]])
        hy = np.array([[1,2,1]])
        return hx,hy

    def seperableSobelY(self):
        hx = np.array([[1,2,1]])
        hy = np.array([[-1,0,1]])
        return hx,hy

    def seperableRandomNumbers(self):
        scaling1, scaling2 = np.random.randint(1,4),np.random.randint(1,4)
        hx = np.abs(np.random.randn(1,3)*scaling1)
        hy = np.abs(np.random.randn(1,3)*scaling2)
        return hx, hy    
