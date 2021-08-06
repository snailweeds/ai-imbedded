import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread("14_Histogram_A.jpg")
img2 = cv2.imread("14_Histogram_B.jpg")

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

def cvt(i):
    b, g, r = cv2.split(i)
    i = cv2.merge([r, g, b])
    return i

img1 = cvt(img1)
img2 = cvt(img2)

fig = plt.figure()
fig.canvas.set_window_title("JetsonNano_Histogram")

hist1 = cv2.calcHist([gray1], [0], None, [256], [0, 256])
plt.subplot(223), plt.plot(hist1), plt.xlim([0, 256])
hist2 = cv2.calcHist([gray2], [0], None, [256], [0, 256])
plt.subplot(224), plt.plot(hist2), plt.xlim([0, 256])

plt.subplot(221), plt.imshow(img1), plt.title("Image_A")
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(img2), plt.title("Image_B")
plt.xticks([]), plt.yticks([])

plt.show()