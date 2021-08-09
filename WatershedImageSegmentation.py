import cv2
import numpy as np
from matplotlib import image, pyplot as plt

img = cv2.imread("20_Watershed_Image_Segmentation.png")
b,g,r = cv2.split(img)
original = cv2.merge([r,g,b])
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
sure_bg = cv2.dilate(opening, kernel, iterations=3)
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 3)
ret, sure_fg = cv2.threshold(dist_transform, 0.5*dist_transform.max(), 255, 0)
sure_fg = np.uint8(sure_fg)

unknown = cv2.subtract(sure_bg, sure_fg)
ret, markers = cv2.connectedComponents(sure_fg)
markers = markers + 1
markers[unknown == 255] = 0
markers = cv2.watershed(img, markers)
img[markers == -1] = [255, 0, 0]
images = [img_gray, thresh, sure_bg, dist_transform, sure_fg, unknown, markers, img]
titles = ["Gray", "Binary", "SureBG", "Distance", "SureFG", "Unknown", "Markers", "Result"]
fig = plt.figure()
fig.canvas.set_window_title("JetsonNano_Watershed")
plt.subplot(3, 3, 1), plt.imshow(original), plt.title("Original\n")
plt.xticks([]), plt.yticks([])

for i in range(len(images)):
    plt.subplot(3, 3, i+2), plt.imshow(images[i]), plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()