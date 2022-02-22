import numpy as np
from PIL import Image
import single_convolution as sc

def get_edges():
    image=Image.open("test-images/music1.png")
    image=image.convert("L")
    image=np.array(image)
    lap_kernel= np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
    image = sc.convolve(image,lap_kernel)
    print(image)
    image=image.astype(np.uint8)
    for i in range(len(image)):
        for j in range(len(image[i])):
            image[i][j]= image[i][j]*255
    image= Image.fromarray(image)
    image.save("Edge_sample.png")

get_edges()