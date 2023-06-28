import cv2

# example of source destination scale_percent
# source = 'me.jpg'
# scale_percent = 50
# destination = 'output.jpg'

def imageResizer(source, destination, scale_percent):
    # Reading image
    src = cv2.imread(source)

    # Use for Showing image
    # cv2.imshow('image', src)

    # Setting new height and width and calculating the 50% of original dimensions
    new_Width = int(src.shape[1] * scale_percent / 100)
    new_height = int(src.shape[0] * scale_percent / 100)

    # Resizing image
    output = cv2.resize(src, (new_Width, new_height))

    # Writing image
    cv2.imwrite(destination, output)

    cv2.waitKey(0)


# Usage of imageResizer function
# imageResizer('me.jpg', 'output.jpg', 50)