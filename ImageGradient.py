import cv2
from matplotlib import pyplot as plt

img = cv2.imread("lena.jpg")

laplacian = cv2.Laplacian(img, cv2.CV_8U)
sobelx = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=3)
canny = cv2.Canny(img, 70, 80)

images = [img, laplacian, sobelx, sobely, canny]
titles = ["Original", "Laplacian", "Sobelx", "Sobely", "Canny"]

fig = plt.figure()
fig.canvas.set_window_title("JetsonNano_Image_Gradient")

plt.subplot(2, 2, 1), plt.imshow(images[0]), plt.title(titles[0])
plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(images[1]), plt.title(titles[1])
plt.xticks([]), plt.yticks([])

for i in range(3):
    plt.subplot(2, 3, i+4), plt.imshow(images[i+2]), plt.title(titles[i+2])
    plt.xticks([]), plt.yticks([])

plt.show()