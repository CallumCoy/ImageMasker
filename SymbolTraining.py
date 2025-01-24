import cv2 as cv
import numpy as np

FONT_SIZE = 1


def main():

    img = createImage("M")
    cv.resize(img, None, fx=10, fy=10)

    cv.imshow("edges", cv.resize(img, None, fx=10, fy=10))
    cv.waitKey(0)


def createImage(letter):
    # Gets sizing of the input
    font = cv.FONT_HERSHEY_SIMPLEX
    textWidth, textHeight = cv.getTextSize(letter, font, FONT_SIZE, 2)[0]

    # Makes the canvas that is to be used.
    img = np.zeros((int(textHeight/2), int(textWidth/2), 3), dtype=np.uint8)
    img.fill(255)

    # Puts the letter centered on a blank canvas.
    cv.putText(img, letter, (0, textHeight//2), font, FONT_SIZE/2, (0, 0, 0), 1, cv.LINE_AA)

    # Grey scales the image.
    return cv.cvtColor(img, cv.COLOR_RGB2GRAY)


main()
