import cv2
import numpy as np

def nothing(x):
    pass

def trackbar():
    img = np.zeros((300, 512, 3), np.uint8)
    cv2.namedWindow("JetsonNano_Trackbar")
    cv2.createTrackbar("R", "JetsonNano_Trackbar", 0, 255, nothing)
    cv2.createTrackbar("G", "JetsonNano_Trackbar", 0, 255, nothing)
    cv2.createTrackbar("B", "JetsonNano_Trackbar", 0, 255, nothing)

    switch = "0:OFF\n1:On"
    cv2.createTrackbar(switch, "JetsonNano_Trackbar", 1, 1, nothing)

    while(1):
        cv2.imshow("JetsonNano_Trackbar", img)
        if cv2.waitKey(1) & 0xFF == 27:
            break
        r = cv2.getTrackbarPos("R", "JetsonNano_Trackbar")
        g = cv2.getTrackbarPos("G", "JetsonNano_Trackbar")
        b = cv2.getTrackbarPos("B", "JetsonNano_Trackbar")
        s = cv2.getTrackbarPos(switch, "JetsonNano_Trackbar")
        if s == 0:
            img[:] = 0
        else:
            img[:] = [b, g, r]
    cv2.destoryAllWindows()

trackbar()