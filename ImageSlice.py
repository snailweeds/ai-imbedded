import cv2

def image_slice():
    original = cv2.imread("7_3_Object_Tracking.jpg", cv2.IMREAD_COLOR)
    
    slice_img = original.copy()
    slice_img = original[200:310, 220:325]
    
    cv2.imshow("JetsonNano_Slice_Original", original)
    cv2.imshow("JetsonNano_Slice_Image", slice_img)
    

    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_slice()
