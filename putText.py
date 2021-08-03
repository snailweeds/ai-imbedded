import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
img.fill(255)

img = cv2.putText(img, "HELLO", (100, 400), cv2.FONT_HERSHEY_PLAIN, 6, (0, 180, 256), 5)
cv2.imshow("JetsonNano_PutText", img)
cv2.waitKey(0)
cv2.destroyAllWindows()