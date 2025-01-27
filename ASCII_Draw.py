import cv2 as cv
import numpy as np

MAX_WIDTH = 600
MAX_HEIGHT = 1800


def main():

    imageLoc = "C:\\Users\\gamec\\Downloads\\wallhaven-01pyvv.jpg"
    image = cv.imread(imageLoc)
    rescaledImage = scaleImage(image)

    cv.imshow("main", image)
    cv.imshow("edges", rescaledImage)
    cv.waitKey(0)
    return


def scaleImage(image):

    # Get original diemensions.
    h, w = image.shape[:2]

    # No work needed if the image is small enough.
    if h <= MAX_HEIGHT and w <= MAX_WIDTH:
        return image

    # Setting Ratio
    ratio = h/w

    if (MAX_HEIGHT-h)*ratio < MAX_WIDTH-w:
        return cv.resize(image, (int(MAX_HEIGHT*ratio), MAX_HEIGHT))
    else:
        return cv.resize(image, (MAX_WIDTH, int(MAX_WIDTH*ratio)))

main()
