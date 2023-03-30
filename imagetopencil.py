import cv2
image = cv2.imread("input.jpeg")
grey_filter = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_filter)
blur = cv2.GaussianBlur(invert, (25,25),6)
inverted_blur = cv2.bitwise_not(blur)
sketch_filter = cv2.divide(grey_filter,inverted_blur,scale=256.0)
cv2.imwrite("output.png",sketch_filter)