import cv2

image = cv2.imread("me.jpeg")

cv2.imshow("Me", image)

while True:
    key = cv2.waitKey(1) & 0xFF

    if key == 27:
        break

cv2.destroyAllWindows()
