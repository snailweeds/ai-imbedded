import cv2
from matplotlib import pyplot as plt

img = cv2.imread("13_Image_Contours.png", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 230, 255, 0)

img_contours = img.copy()
contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
img_contours = cv2.drawContours(img_contours, contours, -1, (51, 102, 255), 4)

cv2.imshow("Original", img)
cv2.imshow("Gray", gray)
cv2.imshow("Contours_Thresh", thresh)
cv2.imshow("Contours", img_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()