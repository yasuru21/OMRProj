import numpy as np
from PIL import Image
from PIL import ImageFilter
import random
from PIL import ImageDraw, ImageFont
from tempmatching import templateMatching
nTM = templateMatching()

class houghTransform():

    def __init__(self):
        self.randomCount = 0

    def hough(self, image):
        space = 0
        image = np.where(image<128,0,1)
        x, y = image.shape
        votesDict = {}
        for i in range(x):
            votesDict[i] = 0
            for j in range(y):
                if image[i][j]==0:
                    votesDict[i] +=1
        l = [key for key,value in votesDict.items() if value > int(0.5*y)]
        
        # Calculating the Space between the lines.
        for i in range(0,len(l)-1):
            if l[i]+1 != l[i+1]:
                if space == 0:
                    space = l[i+1]-l[i]
                elif space == l[i+1]-l[i]:
                    break
        # Finding the row coordinates for the first lines
        firstLines = [l[0]]
        currentLine = l[0]
        for i in range(1,len(l)):
            if l[i] - currentLine > space*2:
                firstLines.append(l[i])
            currentLine = l[i]
        
        return space, firstLines

    def drawLines(self, image, space, firstLines): # stave detection
        outArr = []
        for i in firstLines:
            for j in range(5):
                outArr.append(i + j*space)
      
        copyImage = np.zeros_like(image)

        for elem in outArr:
            copyImage[elem,:] = 255
        return outArr, copyImage

    def resizeTemplate(self, template, space):
        factor = space/template.height
        temp = template.resize((int(template.width * factor), int(template.height * factor)))
        return temp


    def final_result(self, image, template, mT, txtResult, symbol_type, p, dist, threshold = 0.9): # referenced various sources to figure how to work PIL and get this correct
        imgH, imgW = image.shape
        tempH, tempW = template.shape
    #     outImage = Image.fromarray(np.uint8(image)).convert("RGB")
        copy_image = image.copy()
        padding = 2
        if mT=='naive':
            maxScore = tempH * tempW
            matches = nTM.naiveTemplateMatching(image, template, confidenceInterval = threshold)
        elif mT=='edge':
            templateEdge, _, _ = nTM.getEdges(template)
            maxScore = np.sum(templateEdge)
            matches = nTM.edgeDetectionTemplateMatching(image, template, thresholdFactor=threshold)
        else:
            return copy_image, txtResult
        
       
        if matches==[]:
            return copy_image, txtResult
        for score, start_x, start_y, end_x, end_y in matches:
            if end_x >= copy_image.shape[0]-3 or end_y >= copy_image.shape[1]-3:
                continue
            copy_image[start_x-padding:end_x+(padding*2),start_y-padding] = 5
            copy_image[start_x-padding:end_x+(padding*2),end_y+padding] = 5
            copy_image[start_x-padding,start_y-padding:end_y+(padding*2)] = 5
            copy_image[end_x+padding,start_y-padding:end_y+(padding*2)] = 5
            pitch = '_'
            
            if symbol_type == 'filled_note':
                for q in range(int(dist/2)):
                    if q+start_x in p:
                        pitch = p[q+start_x]
                    elif start_x-q in p:
                        pitch = p[start_x-q]
                copy_image = Image.fromarray(np.uint8(copy_image))
                draw = ImageDraw.Draw(copy_image)
                font = ImageFont.truetype('./arial.ttf', 15) 
                draw.text((start_y-15, start_x-15),pitch,(70),font=font)
                copy_image = np.array(copy_image)
            txtResult.append([start_x, start_y, end_x, end_y, symbol_type, pitch, float(np.round(((score/maxScore)*100), 2))])
            
        return copy_image, txtResult

