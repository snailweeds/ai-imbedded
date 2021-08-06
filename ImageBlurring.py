import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("lena.jpg", cv2.IMREAD_COLOR)
b, g, r = cv2.split(img)
img = cv2.merge([r, g, b])

dst1 = cv2.blur(img, (7, 7))
dst2 = cv2.GaussianBlur(img, (5, 5), 0)
dst3 = cv2.medianBlur(img, 9)
dst4 = cv2.bilateralFilter(img, 9, 75, 75)
images = [img, dst1, dst2, dst3, dst4]
titles = ["Original", "Blur(7X7)", "Gaussian Blur(5X5)", "Median Blur", "Bilateral"]
fig = plt.figure()
fig.canvas.set_window_title("JetsonNano_Blurring")
for i in range(5):
    plt.subplot(3, 2, i+1), plt.imshow(images[i])
    plt.title(titles[i]), plt.imshow(images[i])
    
plt.show()