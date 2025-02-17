from time import sleep
import cv2 as cv

# Used to determine the cutoff points for the canny thresholds.
MAXCUTOFF, MINCUTOFF = 0.08, 0.95
MAX_WIDTH = MAX_HEIGHT = 200


def main():
    imageLoc = "C:\\Users\\gamec\\Downloads\\wallhaven-01pyvv.jpg"
    image = cv.imread(imageLoc)
    outline(image)


def scaleDown(image):

    # Get diemensions
    h, w = image.shape[:2]

    # If image is within size send back.
    if h <= MAX_HEIGHT and w <= MAX_WIDTH:
        return image

    # Get ratio
    ratio = h / w

    if ratio > 1:
        newWidth = int(MAX_WIDTH * ratio)
        return cv.resize(image, (newWidth, MAX_HEIGHT))
    else:
        newHeight = int(MAX_HEIGHT * ratio)
        return cv.resize(image, (MAX_WIDTH, newHeight))


def tilize(image):
    M = N = 50
    tiles = [image[x:x+M, y:y+N]
             for x in range(0, image.shape[0], M) for y in range(0, image.shape[1], N)]
    return tiles


def outline(ogImage):

    # Get image to a resonable size.
    image = scaleDown(ogImage)

    # Getting the weak and strong threshold for the canny function
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    histogram = cv.calcHist([gray], [0], None, [256], [0, 256])

    # Maximum number of cells that can be drawn
    cutoff = MAXCUTOFF * image.shape[0] * image.shape[1]

    count = 0

    # Goes through historgram
    for i in reversed(range(len(histogram))):

        # adds up the values in histogram
        count += histogram[i][0]

        # Once max value is reached stop tracking
        if cutoff < count:
            lowThresh = int(MINCUTOFF * i)
            maxThresh = i
            break

    #  Produces edge limit
    edges = cv.Canny(gray, lowThresh, maxThresh)

    tiles = tilize(edges)

    # Shows initial image and results, and waitngs for end key
    cv.imshow("part", tiles[len(tiles)//2])
    cv.imshow("ogImg", image)
    cv.imshow("edges", edges)
    cv.waitKey(0)

    return (gray)


main()
