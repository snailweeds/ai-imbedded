import cv2
import numpy as np

def nothing(x):
    pass

fname_1 = '6_2_Image_Blending_A.jpg'
fname_2 = '6_2_Image_Blending_B.jpg'

cv2.namedWindow('JetsonNano_Image_Blending')
cv2.createTrackbar('W', 'JetsonNano_Image_Blending', 0, 100, nothing)

img_1 = cv2.imread(fname_1)
img_2 = cv2.imread(fname_2)

while(True):
    w = cv2.getTrackbarPos('W', 'JetsonNano_Image_Blending')
    dst = cv2.addWeighted(img_1, float(100-w)*0.01, img_2, float(w)*0.01, 0)
    cv2.imshow('JetsonNano_Image_Blending', dst)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()