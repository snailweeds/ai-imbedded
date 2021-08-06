import cv2
from matplotlib import pyplot as plt

img = cv2.imread("16_2D_Histogram.jpg")

fig = plt.figure()
fig.canvas.set_window_title("JetsonNano_2D_Histogram")

b, g, r = cv2.split(img)
img_rgb = cv2.merge([r, g, b])

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

plt.subplot(122), plt.imshow(hist), plt.title("Histogram")
plt.xlabel("Saturation"), plt.ylabel("Hue")
plt.subplot(121), plt.imshow(img_rgb), plt.title("JetsonNano_HSV")
plt.xticks([]), plt.yticks([])

plt.show()