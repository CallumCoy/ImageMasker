import cv2 as cv
import numpy as np

from SymbolTraining import getSymbol


INVERSE_MODE = False
MAX_THRESHOLD = 180

MAX_WIDTH = 300
MAX_HEIGHT = 900


def main():

    imageLoc = "C:\\Users\\gamec\\Downloads\\121017.jpg"
    image = cv.imread(imageLoc)
    rescaledImage = scaleImage(image)

    createText(rescaledImage)

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


def tilize(image):
    h, w = image.shape[:]

    # Splits the image in x rows.
    horizontalSplit = np.array_split(image, h//3)

    # Splits the x rows into y sections, usually 3.
    splitImage = [np.array_split(block, w//3, axis=1)
                  for block in horizontalSplit]

    # Makes an array then sorts it into a 2d array.
    return np.asarray(splitImage, dtype=np.ndarray).reshape([h//3, w//3])


def applyThreshold(tiles):
    mappedRows = []

    if INVERSE_MODE:
        black, white = str(0), str(1)
    else:
        white, black = str(0), str(1)

    for row in tiles:

        # Go through each row, adding the mapped version on each pass
        mappedTiles = []
        for tile in row:
            symbolCode = ""
            darkness = 0

            # Pass through each pixel, adding the results for each tile
            for symbolBit in tile:
                for pixel in symbolBit:
                    # States the map used to lookup the symbol, and sums up the darkness.
                    symbolCode += black if pixel < MAX_THRESHOLD else white
                    darkness += int(pixel)
            mappedTiles.append([symbolCode, darkness])
        mappedRows.append(mappedTiles)

    return mappedRows


def drawASCII(image):
    text = ""
    for row in image:
        for tile in row:
            text += str(getSymbol(tile[0], tile[1]))
        text += "\n"

    return text


def createText(image):

    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)

    tiles = tilize(gray)
    mappedImage = applyThreshold(tiles)
    ASCIIImage = drawASCII(mappedImage)

    with open("image.txt", "w") as f:
        f.write(ASCIIImage)


main()
