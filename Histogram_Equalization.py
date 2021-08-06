import cv2
from matplotlib import pyplot as plt

img = cv2.imread("15_Histogram_Equlization.jpg", 0)
eqhist = cv2.equalizeHist(img)
hist1 = cv2.calcHist([img], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([eqhist], [0], None, [256], [0, 256])

fig = plt.figure()
fig.canvas.set_window_title("JetsonNano_Histogram_Equalization")

plt.subplot(223), plt.plot(hist1), plt.xlim([0, 256])
plt.subplot(224), plt.plot(hist2), plt.xlim([0, 256])

plt.subplot(221), plt.imshow(img, "gray"), plt.title("Original")
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(eqhist, "gray"), plt.title("Histogram Equalization")
plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.plot(hist1), plt.xlim([0, 256])
plt.subplot(224), plt.plot(hist2), plt.xlim([0, 256])

plt.show()