import cv2

# configurable parameters
source = "ttr.jpg"
destination = 'newImage.jpeg'
scale_percent = 51

# cv2.imshow("title", src)
src = cv2.imread(source, cv2.IMREAD_UNCHANGED)

# calculate the 51 percent of the original dimension, 1 is for width and 0 for height
new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

# resize image
output = cv2.resize(src, (new_width, new_height))

cv2.imwrite(destination, output)
cv2.waitKey(0)
