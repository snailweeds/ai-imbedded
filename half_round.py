import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
img.fill(255)
img = cv2.ellipse(img, (256, 256), (90, 50), 0, 180, 360, (247, 221, 148), 2)
cv2.imshow("JetsonNano_Ellipse", img)
cv2.waitKey(0)
cv2.destroyAllWindows()