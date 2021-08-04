import cv2

fname = "7_1_Binary_Image.jpg"

img = cv2.imread(fname, cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, dst = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
ret, dst1 = cv2.threshold(gray, 255, 255, cv2.THRESH_OTSU)

cv2.imshow("JetsonNano_Original", img)
cv2.imshow("JetsonNano_Binary", dst)
cv2.imshow("JetsonNano_Otsu", dst1)
cv2.waitKey(0)
cv2.destroyAllWindows()