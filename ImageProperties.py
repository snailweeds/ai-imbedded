import cv2

def basic_operation():
    img_1 = cv2.imread("5_Image_Properties.jpg", cv2.IMREAD_COLOR)
    img_2 = img_1.copy()
    img_3 = img_1.copy()

    shape = img.shape
    size = img.size
    dtype = img.dtype

    cv2.putText(img_1, "Shape: " + str(shape), (20, h-100),
    cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 255, 0), 2)
    cv2.putText(img_1, "Size: " + str(size), (20, h-75),
    cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 255, 0), 2)
    cv2.putText(img_1, "dtype: " + str(dtype), (20, h-50),
    cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 255, 0), 2)
    cv2.imshow("JetsonNano_Basic_Operation", img)
    
    b, g, r = cv2.split(img_2)
    img_2 = cv2.merge((r, g, b))
    cv2.imshow("JetsonNano_Basic_Operation_splitNmerge", img_2)

    img_3[:,:,2] = 0
    cv2.imshow("JetsonNano_Basic_Operation_Channel", img_3)
    cv2.waitKey(0)
    cv2.destroyAllWindow()

basic_operation()