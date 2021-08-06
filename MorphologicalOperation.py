import cv2
from matplotlib import pyplot as plt

original = cv2.imread("11_Morphology_Transform_A.png", cv2.IMREAD_GRAYSCALE)
dot = cv2.imread("11_Morphology_Transform_B.png", cv2.IMREAD_GRAYSCALE)
hole = cv2.imread("11_Morphology_Transform_C.png", cv2.IMREAD_GRAYSCALE)

ret_o, th_o = cv2.threshold(original, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret_d, th_d = cv2.threshold(dot, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret_h, th_h = cv2.threshold(hole, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))

erosion = cv2.erode(th_o, kernel, iterations = 1)
dilation = cv2.dilate(th_h, kernel, iterations = 1)
opening = cv2.morphologyEx(th_d, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(th_h, cv2.MORPH_CLOSE, kernel)
gradient = cv2.morphologyEx(th_o, cv2.MORPH_GRADIENT, kernel)
tophat = cv2.morphologyEx(th_o, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(th_o, cv2.MORPH_BLACKHAT, kernel)

images = [th_d, erosion, opening, th_h, dilation, closing, gradient, tophat, blackhat]
titles = ["Dot Image", "Erosion", "Opening", "Hole Image", "Dilation", "Closing", "Gradient", "Tophat", "Blackhot"]

fig = plt.figure()
fig.canvas.set_window_title("JetsonNano_Morphological_Transformations")

for i in range(9):
    plt.subplot(3, 3, i+1), plt.imshow(images[i], "gray"),
    plt.title(titles[i]), plt.xticks([]), plt.yticks([])

plt.show()