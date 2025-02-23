from time import sleep
import cv2 as cv

# Used to determine the cutoff points for the canny thresholds.
DEFAULT_MAX_CUTOFF, DEFAULT_MIN_CUTOFF = 0.45, 0.05
DEFAULT_MAX_WIDTH = DEFAULT_MAX_HEIGHT = 600
DEFAULT_IMAGE_LOC = "C:\\Users\\gamec\\Downloads\\wallhaven-01pyvv.jpg"


def main():

    edges = outline()

    # Shows result and waits for input to close.
    cv.imshow("edges", edges)
    cv.waitKey(0)


def scaleDown(image, targHeight, targWidth):

    # Get diemensions
    curHeight, curWidth = image.shape[:2]

    # If image is within size send back.
    if curHeight <= targHeight and curWidth <= targWidth:
        return image

    # Get ratio
    ratio = curHeight / curWidth

    if ratio > 1:
        newWidth = int(targWidth * ratio)
        return cv.resize(image, (newWidth, targHeight))
    else:
        newHeight = int(targHeight * ratio)
        return cv.resize(image, (targWidth, newHeight))


def outline(imageLoc=DEFAULT_IMAGE_LOC, minCutoff=DEFAULT_MIN_CUTOFF, maxCutoff=DEFAULT_MAX_CUTOFF, width=DEFAULT_MAX_WIDTH, height=DEFAULT_MAX_HEIGHT):

    ogImage = cv.imread(imageLoc)

    # Get image to a reasonable size.
    image = scaleDown(ogImage, targHeight=height, targWidth=width)

    # Getting the weak and strong threshold for the canny function
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    histogram = cv.calcHist([gray], [0], None, [256], [0, 256])

    # Maximum number of cells that can be drawn
    cutoff = maxCutoff * image.shape[0] * image.shape[1]

    count = 0

    # Goes through historgram
    for i in reversed(range(len(histogram))):

        # adds up the values in histogram
        count += histogram[i][0]

        # Once max value is reached stop tracking
        if cutoff < count:
            lowThresh = int(minCutoff * i)
            maxThresh = i
            break

    #  Produces edge limit
    edges = cv.Canny(gray, lowThresh, maxThresh)

    return (edges)


if __name__ == "__main__":
    main()
