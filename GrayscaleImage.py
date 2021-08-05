import cv2
import numpy as np

def exponential_function(channel, exp):
    table = np.array([min((i**exp), 255) for i in np.arange(0, 256)]).astype("uint8")
    channel = cv2.LUT(channel, table)
    return channel

def tone(img, number):
    for i in range(3):
        if i == number:
            img[:, :, i] = exponential_function(img[:, :, i], 1.05)
        else:
            img[:, :, i] = 0
    return img

fname = "7_2_Grayscale_Image.jpg"
original = cv2.imread(fname, cv2.IMREAD_COLOR)
cv2.imshow("JetsonNano_Grayscale_Original", original)

img_1 = original.copy()
img_1 = tone(img_1, 2)
cv2.imshow("JetsonNano_Grayscale_Red", img_1)
red2Gray = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)
cv2.imshow("JetsonNano_Grayscale_Red2Gray", red2Gray)

img_2 = original.copy()
img_2 = tone(img_2, 1)
cv2.imshow("JetsonNano_Grayscale_Green", img_2)
green2Gray = cv2.cvtColor(img_2, cv2.COLOR_BGR2GRAY)
cv2.imshow("JetsonNano_Grayscale_Green2Gray", green2Gray)

img_3 = original.copy()
img_3 = tone(img_3, 0)
cv2.imshow("JetsonNano_Grayscale_Blue", img_3)
blue2Gray = cv2.cvtColor(img_3, cv2.COLOR_BGR2GRAY)
cv2.imshow("JetsonNano_Grayscale_Blue2Gray", blue2Gray)

cv2.waitKey(0)
cv2.destroyAllWindows()