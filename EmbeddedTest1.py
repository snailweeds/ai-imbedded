import cv2

fname = "2_1_Image_RSW.jpg"
original = cv2.imread(fname, cv2.IMREAD_COLOR)

img1 = original.copy()
img1 = cv2.putText(img1, "Ai HUB", (50, 100), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

img2 = original.copy()
img2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
img2 = cv2.putText(img2, "HYUNJI", (650, 80), cv2.FONT_HERSHEY_PLAIN, 5, (0, 255, 0), 5)

cv2.imwrite("Image_1.png", img1)
cv2.imwrite("Image_2.png", img2)

cv2.imshow("Image_1", img1)
cv2.imshow("Image_2", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

