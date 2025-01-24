import cv2 as cv
import numpy as np

FONT_SIZE = 1


def main():

    img = createImage("M")
    splitImage = imageSplitter(img)

    for y in range(splitImage.shape[0]):
        for x in range(splitImage.shape[1]):
            cv.imshow("Piece" + str(x) + str(y),
                      cv.resize(splitImage[y, x], None, fx=10, fy=10))

    cv.waitKey(0)


def createImage(letter):
    # Gets sizing of the input.
    font = cv.FONT_HERSHEY_SIMPLEX
    textWidth, textHeight = cv.getTextSize(letter, font, FONT_SIZE, 2)[0]

    # Makes the canvas that is to be used.
    img = np.zeros((int(textHeight/2), int(textWidth/2), 3), dtype=np.uint8)
    img.fill(255)

    # Puts the letter centered on a blank canvas.
    cv.putText(img, letter, (0, textHeight//2), font,
               FONT_SIZE/2, (0, 0, 0), 1, cv.LINE_AA)

    # Grey scales the image.
    return cv.cvtColor(img, cv.COLOR_RGB2GRAY)


def imageSplitter(img, blocks=(3, 3)):
    # Splits the image in x rows, usually 3.
    horizontalSplit = np.array_split(img, blocks[0])

    # Splits the x rows into y sections, usually 3.
    splitImage = [np.array_split(block, blocks[1], axis=1)
                  for block in horizontalSplit]

    # Makes an array then sorts it into a 2d array.
    return np.asarray(splitImage, dtype=np.ndarray).reshape(blocks)


main()
