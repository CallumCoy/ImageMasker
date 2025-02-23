from PIL import Image

# ASCII characters used to build the output text
ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width)
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")

def pixels_to_ascii(image, inverseMode):
    pixels = image.getdata()
    ascii_str = ""

    modifyingVal = 255 if inverseMode else 0

    for pixel in pixels:
        ascii_str += ASCII_CHARS[abs(modifyingVal - pixel) // 32]
    return ascii_str

def image_to_ascii(image_path, new_width=100, inverseMode = False):
    # Load the image
    image = Image.open(image_path)

    # Convert the image to gray scale
    image = grayify(image)

    # Resize the image
    image = resize_image(image, new_width)

    # Convert pixels to ASCII characters
    ascii_str = pixels_to_ascii(image, inverseMode)
    
    # Format the ASCII string into multiple lines
    pixel_count = len(ascii_str)
    ascii_image = "\n".join([ascii_str[i:(i + new_width)] for i in range(0, pixel_count, new_width)])
    
    return ascii_image

def main ():
    # Example usage
    image_path = "C:\\Users\\gamec\\Downloads\\wallhaven-01pyvv.jpg"  # Replace with your image path
    ascii_art = image_to_ascii(image_path)

    with open("image2.txt", "w") as f:
        f.write(ascii_art)

if __name__ == "__main__":
    main()

