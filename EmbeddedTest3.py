import cv2

fname1 = "6_3_Bitwise_Operation_A.png"
fname2 = "lena.jpg"
img1 = cv2.imread(fname1, cv2.IMREAD_COLOR)
img2 = cv2.imread(fname2, cv2.IMREAD_COLOR)

H, W, C = img1.shape
pos = img2[0:H, 0:W]

gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

fg = cv2.bitwise_and(img1, img1, mask = mask)
bg = cv2.bitwise_and(pos, pos, mask = mask_inv)
output = cv2.add(fg, bg)

img2[0:H, 0:W] = output
cv2.imshow("JetsonNano_Result", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()