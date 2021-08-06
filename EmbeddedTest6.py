import cv2
import numpy as np

img = cv2.imread("lena.jpg", cv2.IMREAD_COLOR)
h, w, c = img.shape

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cntr, hrchy = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

dst1 = np.zeros((h, w, c), np.uint8)+255
dst1 = cv2.drawContours(dst1, cntr, -1, (255, 0, 0), 1)
dst2 = gray.copy()
dst2 = cv2.drawContours(dst2, cntr, -1, (255, 0, 0), 1)

cv2.imshow("Original", img)
cv2.imshow("Threshold", th)
cv2.imshow("Contours", dst1)
cv2.imshow("DrawContours", dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()