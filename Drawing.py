import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
img.fill(255)
img = cv2.line(img, (300, 0), (0, 300), (235, 174, 245), 3) # b,g,r ordered
img = cv2.rectangle(img, (150, 150), (300, 300), (148, 244, 247), 3)
img = cv2.circle(img, (360, 360), 85, (148, 247, 148), 2)
img = cv2.putText(img, "Draw", (430, 420), cv2.FONT_HERSHEY_PLAIN, 1.5, (247, 221, 148), 2)
cv2.imshow("JetsonNano_Drawing", img)
cv2.waitKey(0)
cv2.destroyAllWindows()