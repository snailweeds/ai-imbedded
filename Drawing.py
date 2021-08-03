import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
img.fill(255)
img = cv2.line(img, (300, 0), (100, 511), (218, 148, 247), 3) # b,g,r ordered
img = cv2.rectangle(img, (500, 500), (560, 580), (148, 247, 148), -1)
img = cv2.circle(img, (250, 250), 60, (148, 247, 148), -1)
cv2.imshow("JetsonNano_Line", img)
cv2.waitKey(0)
cv2.destroyAllWindows()