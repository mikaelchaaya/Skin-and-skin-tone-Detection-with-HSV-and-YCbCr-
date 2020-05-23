import cv2
import numpy as np
import argparse
#Open a simple image
parser=argparse.ArgumentParser()
parser.add_argument('--image')

args=parser.parse_args()
img=cv2.imread(args.image)
if img is None:
     print("no image available")
     exit()
#converting from gbr to hsv color space
img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#skin color range for hsv color space 
HSV_mask = cv2.inRange(img_HSV, (0, 15, 0), (17,170,255)) 
HSV_mask = cv2.morphologyEx(HSV_mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))

#converting from gbr to YCbCr color space
img_YCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
#skin color range for hsv color space 
YCrCb_mask = cv2.inRange(img_YCrCb, (0, 135, 85), (255,180,135)) 
YCrCb_mask = cv2.morphologyEx(YCrCb_mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))

#merge skin detection (YCbCr and hsv)
global_mask=cv2.bitwise_and(YCrCb_mask,HSV_mask)
global_mask=cv2.medianBlur(global_mask,3)
global_mask = cv2.morphologyEx(global_mask, cv2.MORPH_OPEN, np.ones((4,4), np.uint8))


HSV_result = cv2.bitwise_not(HSV_mask)

YCrCb_result = cv2.bitwise_not(YCrCb_mask)

global_result=cv2.bitwise_not(global_mask)


cv2.imwrite("1_HSV.jpg",HSV_result)
cv2.imwrite("2_YCbCr.jpg",YCrCb_result)
cv2.imwrite("3_global_result.jpg",global_result)
cv2.waitKey(0)
cv2.destroyAllWindows()  


#we get the hsv image and mask it to get only skin
mask = cv2.inRange(img_HSV,(0, 15, 0), (17,170,255))
#merge it with the original image
skin = cv2.bitwise_and(img,img, mask= mask)    
# extract the color RGB and remove the black  pixel from the mask
#remeber that CV2 store pixel in BGR format so we will extract those pixels
rows , cols,channels  = skin.shape
arr = np.array([0,0,0])
k1=[]#blue 
k2=[]#green
k3=[]#red
for i in range(rows):
    for j in range(cols):
         k = skin[i,j]
         if not ((k == arr).all()):
              k1.append(k[0])
              k2.append(k[1])
              k3.append(k[2])
        

Bmediant =sum(k1)/len(k1)
Gmediant =sum(k2)/len(k2)
Rmediant =sum(k3)/len(k3)

Bmax =max(k1)
Gmax =max(k2)
Rmax =max(k3)

cv2.imwrite("coloredHSV-SkinDetection.jpg",skin)

import matplotlib.pyplot as plt
f, axarr = plt.subplots(nrows=1,ncols=2)
plt.sca(axarr[0])
plt.imshow([[(Rmediant/255,Gmediant/255,Bmediant/255)]])
plt.title('Mediant color')
plt.sca(axarr[1]);
plt.imshow([[(Rmax/255,Gmax/255,Bmax/255)]])
plt.title('Max Color')
plt.imshow([[(Rmax/255,Gmax/255,Bmax/255)]])
plt.title('Max Color')


plt.savefig('plot.png')