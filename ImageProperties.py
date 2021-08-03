import cv2

img = "5_Image_Properties.jpg"
green_color = (0, 0, 255)
img_1 = cv2.imread(img, cv2.IMREAD_COLOR)
img_2 = img_1.copy()
img_3 = img_1.copy()

shape = img_1.shape
size = img_1.size
dtype = img_1.dtype

cv2.putText(img_1, "Shape: " + str(shape), (20, 806-100),
cv2.FONT_HERSHEY_PLAIN, 1.5, (51, 15, 124), 2)
cv2.putText(img_1, "Size: " + str(size), (20, 806-75),
cv2.FONT_HERSHEY_PLAIN, 1.5, (51, 15, 124), 2)
cv2.putText(img_1, "dtype: " + str(dtype), (20, 806-50),
cv2.FONT_HERSHEY_PLAIN, 1.5, (51, 15, 124), 2)
cv2.imshow("JetsonNano_Basic_Operation", img_1)
    
b, g, r = cv2.split(img_2)
img_2 = cv2.merge((r, g, b))
cv2.imshow("JetsonNano_Basic_Operation_splitNmerge", img_2)

img_3[:,:,2] = 0
cv2.imshow("JetsonNano_Basic_Operation_Channel", img_3)
cv2.waitKey(0)