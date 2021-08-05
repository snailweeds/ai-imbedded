import cv2
from matplotlib import pyplot as plt

img = cv2.imread("lena.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
th = 127
th_max = 255

ret, th1 = cv2.threshold(gray, th, th_max, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(gray, th_max, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 2)
th3 = cv2.adaptiveThreshold(gray, th_max, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 2)

titles = ["Original", "Gaussian", "Mean"]
images = [img, th2, th3]

fig = plt.figure()
fig.canvas.manager.set_window_title("Thresholding")
for i in range(3):
    plt.subplot(1, 3, i+1), plt.imshow(images[i], "gray")
    plt.title(titles[i]), plt.xticks([]), plt.yticks([])

plt.show()