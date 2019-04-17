import cv2
img = cv2.imread('/home/vivek/PycharmProjects/aws/AWSSearchFaces/golu.jpg')

# Second argument is a flag which specifies the way image should be read.

img1 = cv2.imread('/home/vivek/PycharmProjects/aws/AWSSearchFaces/golu.jpg', 1)

img2 = cv2.imread('/home/vivek/PycharmProjects/aws/AWSSearchFaces/golu.jpg', 0)  # Load an color image in grayscale


img3 =  cv2.imread('/home/vivek/PycharmProjects/aws/AWSSearchFaces/golu.jpg', -1)

# Displaying the images

cv2.imshow('image', img)

cv2.waitKey(1000)  # To hold the image for a while time is in msec if nothing it will wait for any key

cv2.imshow('image', img1)

cv2.waitKey(1000)

cv2.imshow('image', img2)

cv2.waitKey(1000)

cv2.imshow('image', img3)

cv2.waitKey(1000)

cv2.destroyAllWindows()

# simply destroys all the windows we created.
# If you want to destroy any specific window, use the function cv2.destroyWindow()
# where you pass the exact window name as the argument.
