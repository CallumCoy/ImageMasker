import cv2 as cv
import numpy as np

FONT_SIZE = 1
MAX_THRESHOLD = 190
SYMBOL_INPUT = []
MAP_CATALOG = dict()
BASIC_ASCII_CHARS = "@%#*+=-:. "


def setSymbols():
    global SYMBOL_INPUT

    # Inputs all ACII Values
    for i in range(33, 127):
        SYMBOL_INPUT.append(chr(i))


def main():

    setSymbols()

    for symbol in SYMBOL_INPUT:

        # Creates an image for the current symbol.
        img = createImage(symbol)

        # Splits the image up, normally into 3x3.
        splitImage = imageSplitter(img)

        # Assigns each sections a darkness Value.
        darkness = blockDarkness(splitImage)

        # Assigns each section with a 1 or a 0 depending if it is within the threshold.
        mappedArray = mapArray(darkness)

        # Inputs the new data into the map Catalog.
        inputCatalog(mappedArray, darkness, symbol)


def getSymbol(bitString, darkness):

    # Use the basic method if it doesn't have a good fit
    if bitString not in MAP_CATALOG:
        return BASIC_ASCII_CHARS[darkness//(32*9)]

    closestMatch = 255*9
    idealSymbol = ""

    for symbol in MAP_CATALOG[bitString]:
        # Chekcs if newest symbol is closer, is so update with the new data
        if abs(darkness - symbol) < closestMatch:
            idealSymbol = MAP_CATALOG[bitString][symbol]
            closestMatch = symbol

    return idealSymbol


def inputCatalog(mappedArray, shadowArray, symbol):
    global MAP_CATALOG

    # Gets the overall darkness for this symbol.
    totalDarkness = int(np.sum(shadowArray))
    key = ""

    # Cycles through the array, turning it into a 9 bit string.
    for y in mappedArray:
        for x in y:
            key += str(x)

    # Checks if the key exists, if it does insert the that darkness level doesn't exist, else create the new dict key.
    if key in MAP_CATALOG:
        if totalDarkness not in MAP_CATALOG[key]:
            MAP_CATALOG[key].update({totalDarkness: symbol})
    else:
        MAP_CATALOG[key] = {totalDarkness: symbol}

    return


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


def blockDarkness(splitLetter):
    darknessGraph = []

    # Find the average darkness of each square
    for i in range(len(splitLetter)):
        tempArray = []
        for j in range(len(splitLetter[i])):
            width, height = splitLetter[i][j].shape
            tempArray.append(int(np.sum(splitLetter[i][j])/(width*height)))

        darknessGraph.append(tempArray)

    return darknessGraph


def mapArray(DarknessChart):
    MapChart = []

    # If within threshhold mark with 0 else 1
    for i in range(len(DarknessChart)):
        tempArray = []
        for j in range(len(DarknessChart[i])):
            tempArray.append(0 if DarknessChart[i][j] > MAX_THRESHOLD else 1)

        MapChart.append(tempArray)

    return MapChart


main()
