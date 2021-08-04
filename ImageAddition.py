import cv2

def image_add():
    img1 = cv2.imread("6_2_Image_Blending_B.jpg", cv2.IMREAD_COLOR)
    img2 = cv2.imread("6_3_Bitwise_Operation_A.png", cv2.IMREAD_COLOR)

    h, w, c = img2.shape

    img_add = img1.copy()
    img_add[50:h + 50, 100:w + 100] = img2

    cv2.imshow("JetsonNano_Add_Image1", img1)
    cv2.imshow("JetsonNano_Add_Image2", img2)
    cv2.imshow("JetsonNano_Add_Result", img_add)
    
    cv2.waitKey(0)
    cv2.destroyWindows()

image_add()
