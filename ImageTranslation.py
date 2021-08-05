import cv2
import numpy as np

img = cv2.imread("9_1_Transformations.png", cv2.IMREAD_COLOR)
rows, cols = img.shape[:2]

M = np.float32([[1, 0, 10], [0, 1, 20]])

dst = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow("JetsonNano_Original", img)
cv2.imshow("JetsonNano_Translation", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()