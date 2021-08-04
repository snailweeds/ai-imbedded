import cv2

fname = "lena.png"
original = cv2.imread(fname, cv2.IMREAD_COLOR)

blue, green, red = cv2.split(original)
original[:,:,0] = 0

cv2.imshow("Image", original)
cv2.imwrite("ChangeChannel.png", original)
cv2.waitKey(0)
cv2.destroyAllWindows()