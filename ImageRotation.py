import cv2

img = cv2.imread("9_1_Transformations.png", cv2.IMREAD_COLOR)
rows, cols = img.shape[:2]

M = cv2.getRotationMatrix2D((cols/2, rows/2), 75, 0.5)

dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow("JetsonNano_Original", img)
cv2.imshow("JetsonNano_Rotation", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()