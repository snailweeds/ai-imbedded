import cv2
import numpy as np

def nothing(x):
    pass

img = cv2.imread("lena.jpg", cv2.IMREAD_COLOR)
cv2.namedWindow("JetsonNano_Filtering")
cv2.createTrackbar("K", "JetsonNano_Filtering", 1, 20, nothing)

while(1):
    if cv2.waitKey(1) & 0xFF == 27:
        break
    k = cv2.getTrackbarPos("K", "JetsonNano_Filtering")

    if k == 0:
        k = 1

    kernel = np.ones((k, k), np.float32) / (k*2)
    dst = cv2.filter2D(img, -1, kernel)

    cv2.imshow("JetsonNano_Filtering", dst)

cv2.destroyAllWindows()