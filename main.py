import numpy as np 
import sys
from PIL import Image
from PIL import ImageFilter
import random
from PIL import ImageDraw
from test_functions.convolution_kernel import kernelOperations
from test_functions.tempmatching import templateMatching
from test_functions.hough import houghTransform
from test_functions.hamming import hamming
from test_functions.sheetmusicreader import sheetmusic

def getResults(image, template1, template2, template3, d):
    # easily able to call classes into main  
    ko = kernelOperations()
    nTM = templateMatching()
    ht = houghTransform()
    ham = hamming()
    sheet = sheetmusic()

    
    image = np.array(image)
    image = ko.rgb2gray(image)
  
    space, firstLines = ht.hough(image)

    _, copyImage = ht.drawLines(image, space, firstLines)
    outImage = Image.fromarray(np.uint8(copyImage))
    outImage.save("detected_staves.png","PNG")
    print("the detected staves are within detected_stave file")

    # convert templates to greyscale for each temp
    template1 = ht.resizeTemplate(template1,space) #increases efficiency in runtime
    template1 = np.array(template1)
    template1 = ko.rgb2gray(template1)

    template2 = ht.resizeTemplate(template2,space*3)
    template2 = np.array(template2)
    template2 = ko.rgb2gray(template2)
    
    template3 = ht.resizeTemplate(template3,space*2)
    template3 = np.array(template3)
    template3 = ko.rgb2gray(template3)
    
    pitchDictionary = sheet.getPitchDictionary(firstLines, space)  # get dict to use


# this is where we formulate text file, utilized
    outText = []
    outImage, outText = ht.final_result(image, template1, d['type1'], outText, "filled_note", pitchDictionary, space, threshold = d['template1Factor'])
    outImage, outText = ht.final_result(outImage, template2, d['type2'], outText, "quarter_rest", pitchDictionary, space, threshold= d['template2Factor'])
    outImage, outText = ht.final_result(outImage, template3, d['type3'], outText, "eighth_rest", pitchDictionary, space, threshold = d['template3Factor'])
    np.savetxt("detected.txt", outText, fmt="%s")
    outImage = Image.fromarray(np.uint8(outImage))
    outImage.save("detected.png","PNG")

    return "results have been updated in the detetected.png file"

if __name__ == '__main__':
    music_file = sys.argv[1] # DO NOT RUN THIS FILE --> INPUT ON TERMINAL OR YOU WILL GET ERROR
    m1, m2, *rest = music_file.split('/')
    print("the file you are running is: " + m2 )
    
    if m2=="music1.png": # have to adjust each factor for different input because sometimes it didnt detect it and identify notes.
        d = {'template1Factor':0.9, 'template2Factor':0.85, 'template3Factor':0.8, 
             'type1':'naive', 'type2':'naive', 'type3':'naive'}
    elif m2=="music2.png":
        d = {'template1Factor':0.83, 'template2Factor':0.68, 'template3Factor':0.33, 
             'type1':'naive', 'type2':'edge', 'type3':'edge'}
    elif m2=="music3.png":
        d = {'template1Factor':0.65, 'template2Factor':0.75, 'template3Factor':0.78,   # can play around with values to see affect it has 
             'type1':'naive', 'type2':'naive', 'type3':'naive'}
    elif m2=="music4.png":
        d = {'template1Factor':0.83, 'template2Factor':0.75, 'template3Factor':0.78, 
             'type1':'naive', 'type2':'naive', 'type3':'naive'}
    else:
        d = {'template1Factor':0.83, 'template2Factor':0.85, 'template3Factor':0.7, 
             'type1':'naive', 'type2':'naive', 'type3':'naive'}
    im_name = "./" + music_file
    template1 = Image.open('./test-images/template1.png')
    template2 = Image.open('./test-images/template2.png')
    template3 = Image.open('./test-images/template3.png')
    image = Image.open(im_name)

    stringOutput = getResults(image, template1, template2, template3, d)
    print(stringOutput)