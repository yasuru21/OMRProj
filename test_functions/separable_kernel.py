import numpy as np
def separable_kernel(hx,hy, img):
    #Test purposes
    im_arr = np.array(img)
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