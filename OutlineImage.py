from time import sleep
import cv2

# Used to determine the cutoff points for the canny thresholds.
MAXCUTOFF, MINCUTOFF = 0.08, 0.95
MAX_WIDTH = MAX_HEIGHT = 1000

def main():
    imageLoc = "C:\\Users\\gamec\\Downloads\\wallhaven-01pyvv.jpg"
    image = cv2.imread(imageLoc)
    outline(image)

def scaleDown(image):

    # Get diemensions
    h,w = image.shape[:2]

    #If image is within size send back.
    if h <= MAX_HEIGHT and w <= MAX_WIDTH:
        return image

    # Get ratio
    ratio = h / w

    if ratio > 1:
        newWidth = int(w * ratio)
        return cv2.resize(image, (newWidth, MAX_HEIGHT))
    else:
        newHeight = int(h*ratio)
        return cv2.resize(image,(MAX_WIDTH, newHeight))


def outline(ogImage):

    #Get image to a resonable size.
    image = scaleDown(ogImage)

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
