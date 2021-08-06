import cv2
from matplotlib import pyplot as plt

img = cv2.imread("MopTest1.png", cv2.IMREAD_GRAYSCALE)
ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
dst1 = thresh.copy()
dst2 = thresh.copy()

dilation = cv2.dilate(dst1, kernel, iterations = 1)
erosion = cv2.erode(dst2, kernel, iterations = 1)

plt.subplot(1, 3, 1), plt.imshow(thresh, "gray")
plt.title("Treshold"), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 2), plt.imshow(dilation, "gray")
plt.title("Dilation"), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 3), plt.imshow(erosion, "gray")
plt.title("Erosion"), plt.xticks([]), plt.yticks([])

plt.show()