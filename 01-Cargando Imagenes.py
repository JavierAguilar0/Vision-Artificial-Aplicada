import cv2

img = cv2.imread('op.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('imagen',img)
cv2.waitKey(0)
cv2.destroyAllWindows()