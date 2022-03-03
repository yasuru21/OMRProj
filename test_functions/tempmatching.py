import numpy as np
from test_functions.convolution_kernel import kernelOperations


# This covers problem # 6 on assignment pdf using scoring function with edge maps

ko = kernelOperations()

class templateMatching():

    def __init__(self):
        self.randomInit = 0
    # referenced online resources 
    def scoring(self, scoreArr, threshold = 0.5):
        if scoreArr==[]:
            return []
        scoreArr = np.array(scoreArr)
        scores = scoreArr[:, 0]
        start_x = scoreArr[:, 1]
        start_y = scoreArr[:, 2]
        end_x = scoreArr[:, 3]
        end_y = scoreArr[:, 4]
        picked_boxes = []
        areas = (end_x - start_x + 1) * (end_y - start_y + 1)
        order = np.argsort(scores)
        while order.size > 0:
            index = order[-1]
            picked_boxes.append(scoreArr[index])
            x1 = np.maximum(start_x[index], start_x[order[:-1]])
            x2 = np.minimum(end_x[index], end_x[order[:-1]])
            y1 = np.maximum(start_y[index], start_y[order[:-1]])
            y2 = np.minimum(end_y[index], end_y[order[:-1]])
            w = np.maximum(0.0, x2 - x1 + 1)
            h = np.maximum(0.0, y2 - y1 + 1)
            intersection = w * h
            ratio = intersection / (areas[index] + areas[order[:-1]] - intersection)
            left = np.where(ratio < threshold)
            order = order[left]
        return picked_boxes

    def naiveTemplateMatching(self, image, template1, confidenceInterval = 0.90):
        image = np.where(image>128,1,0)
        template1 = np.where(template1>128,1,0)
        h, w = image.shape
        tempH, tempW = template1.shape
        scoreArr = []
        threshold = int(confidenceInterval*tempH*tempW)
        for i in range(h-tempH):
            for j in range(w - tempW):
                subImage = image[i:i+tempH, j:j+tempW]
                score = np.sum((subImage * template1) + (1-subImage) * (1- template1))
                if score>=threshold:
                    scoreArr.append([int(score), i, j, i+tempH, j+tempW])
        scoreArr1 = self.scoring(scoreArr)
        return scoreArr1

    def getEdges(self, im, threshold = 128): #using sobel and seperable kernel to get edges
        hx, hy = ko.seperableSobelY()
        imageEdgey = ko.seperableKernel(im, hx, hy)

        hx, hy = ko.seperableSobelX()
        imageEdgex = ko.seperableKernel(im, hx, hy)

        imageEdge = np.sqrt(imageEdgex**2 + imageEdgey**2)
        imageEdge = np.where(imageEdge>threshold, 255, 0)
        
        return imageEdge, imageEdgex, imageEdgey

    
    # ----------------------------------------------------------------------------------
    # code below was created based of referencing other code that was written (refer to references section)
    def scanRange(self, f): #needed for edge temp matching
        for i, fi in enumerate(f):
            if fi == np.inf: continue
            for j in range(1,i+1):
                x = fi+j*j
                if f[i-j] < x: break
                f[i-j] = x

    def distanceTransform(self, inputArray):
        f = np.where(inputArray, 0.0, np.inf)
        for i in range(f.shape[0]):
            self.scanRange(f[i,:])
            self.scanRange(f[i,::-1])
        for i in range(f.shape[1]):
            self.scanRange(f[:,i])
            self.scanRange(f[::-1,i])
        # np.sqrt(f,f)
        return f


# ------------------------------------------------------------------------------------------------
    def edgeDetectionTemplateMatching(self, image, template1, thresholdFactor = 0.25):
        imageEdge, imageEdgex, imageEdgey = self.getEdges(image)
        templateEdge1, templateEdgex1, templateEdgey1 = self.getEdges(template1)
        D_imageEdge = self.distanceTransform(imageEdge)
        h, w = D_imageEdge.shape
        h1, w1 = templateEdge1.shape
        outArr, threshold = [], int(np.sum(templateEdge1)*thresholdFactor)
        for i in range(0, h - h1 + 1):
            for j in range(0, w - w1):
                temp = D_imageEdge[i:i+h1,j:j+w1] * templateEdge1
                score = np.sum(temp)
                if score <= threshold:
                    outArr.append([int(score), i, j, i+h1, j+w1])
        scoreArr1 = self.scoring(outArr)
        return scoreArr1

