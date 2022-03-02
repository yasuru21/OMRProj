import numpy as np 
import sys
from PIL import Image
from PIL import ImageFilter
import random
from PIL import ImageDraw
from hough import houghTransform
from hamming import hamming
from sheetmusicreader import sheetmusic

def getResults(image, template1, template2, template3, d):
    # easily able to call seperate files 
    
    ht = houghTransform()
    ham = hamming()
    pR = sheetmusic()