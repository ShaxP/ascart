import PIL.Image

ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

def resize(image, new_width = 100):
    width, height = image.size
    new_height = int(new_width * height / width)
    return image.resize((new_width, new_height))

def to_greyscale(image):
    return image.convert("L")

def pixel_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "";
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel//25];

    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img=""
    #Split the string based on width  of the image
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
    return ascii_img

def main():
    #path = input("Enter the path to the image file:  ")
    image = ""
    path = '.\\shazam.jpg'
    width = 50
    try:
       image = PIL.Image.open(path)
    except:
        print(path, "Unable to find image ")

    image = resize(image, new_width=width)
    greyscale_image = to_greyscale(image)
    ascii_img = pixel_to_ascii(greyscale_image)

    print(ascii_img)

main()