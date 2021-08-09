import cv2
import numpy as np

original = cv2.imread("19_2_Hough_Circle_Transform.png")
img = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
img = cv2.medianBlur(img, 5)

cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20, param1=50,
param2=25, minRadius=0, maxRadius=0)
circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    cv2.circle(cimg, (i[0], i[1]), i[2], (51, 102, 255), 5)
    cv2.circle(cimg, (i[0], i[1]), 2, (153, 255, 153), 5)

cv2.imshow("JetsonNano_Original", original)
cv2.imshow("JetsonNano_Circle", cimg)

cv2.waitKey(0)