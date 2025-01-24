import cv2 as cv
import numpy as np

FONT_SIZE = 1
MAX_THRESHOLD = 190

def main():

    img = createImage("H")
    splitImage = imageSplitter(img)

    darkness = blockDarkness(splitImage)

    for y in range(splitImage.shape[0]):
        for x in range(splitImage.shape[1]):
            print(" " + str(darkness[x][y]) + " coords: " + str(x) + ", " + str(y))
            cv.imshow(str(darkness[y][x])+ " " + str(x) + str (y),
                      cv.resize(splitImage[y, x], None, fx=60, fy=60))
    

    print(darkness)
    print(mapArray(darkness))

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

    return MapChart, 



main()
