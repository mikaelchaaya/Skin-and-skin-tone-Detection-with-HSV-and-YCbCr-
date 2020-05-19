
The above entire procedure is applied to each and every pixel of the image.
The RGB image value is converted to HSV as well as YCbCr value using the cv2 (OpenCV) library, the HSV and YCbCr value of each pixel is compared to the standard values of a skin pixel and the decision is made whether the pixel is a skin pixel or not depending on whether the values lie in a range of predefined threshold values for each parameter.
The ranges for a skin pixel used in this algorithm are as follows:
HSV:    0<=H<=17 and 15<=S<=170 and 0<=V<=255
			and		
  YCbCr:   0<=Y<=255 and 135<=Cr<=180 and 85<=Cb<=135
After many researches and testing on the results we predefined those ranges.

After that for the sake of the project we will take the hsv image and extract the skin color only from it and transform it to rgb and display the median skin color and the max intensity skin color.
The median of the skin tone will show us the usual skin tone in this lighting and the max intensity tone will show us the brighter color seen on the skin in bright day light.
