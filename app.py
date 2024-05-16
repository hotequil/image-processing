import cv2

image = cv2.imread("me.jpeg")

cv2.imshow("Me", image)

key = cv2.waitKey(0)

if key == 27:
    cv2.destroyAllWindows()
