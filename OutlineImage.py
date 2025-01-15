from time import sleep
import cv2

# Used to determine the cutoff points for the canny thresholds.
MAXCUTOFF, MINCUTOFF = 0.05, 0.6


def main():
    imageLoc = "C:\\Users\\gamec\\Downloads\\JPEG_007.jpg"
    image = cv2.imread(imageLoc)
    outline(image)


def outline(image):

    # Getting the weak and strong threshold for the canny function
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    histogram = cv2.calcHist([gray], [0], None, [256], [0, 256])

    # Maximum number of cells that can be drawn
    cutoff = MAXCUTOFF * image.shape[0] * image.shape[1]

    count = 0

    # Goes through historgram
    for i in reversed(range(len(histogram))):

        #adds up the values in histogram
        count += histogram[i][0]

        #Once max value is reached stop tracking
        if cutoff < count:
            lowThresh = int(MINCUTOFF * i)
            maxThresh = i
            break

    #  Produces edge limit
    edges = cv2.Canny(gray, lowThresh, maxThresh)

    # Shows initial image and results, and waitngs for end key
    cv2.imshow("ogImg", image)
    cv2.imshow("edges", edges)
    cv2.waitKey(0)

    return(gray)


main()
