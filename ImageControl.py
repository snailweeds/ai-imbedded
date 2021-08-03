import cv2

fname = "lena.png"

orginal = cv2.imread(fname, cv2.IMREAD_COLOR)
cv2.imshow("JetsonNano_Original", orginal)

gray = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
cv2.imshow("JetsonNano_Gray", gray)

unchange = cv2.imread(fname, cv2.IMREAD_UNCHANGED)
cv2.imshow("JetsonNano_Unchanged", unchange)

cv2.imwrite("GrayImage.png", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()