"""Main module."""

from PIL import Image

def convert_img_ascii(source, output):
    img_source = source
    img = Image.open(img_source)

    width, height = img.size
    aspect_ratio = height / width
    new_width = 70
    new_height = aspect_ratio * new_width * 0.55
    img = img.resize(
        (new_width, int(new_height))
    )

    img = img.convert('L')
    pixels = img.getdata()


    chars = ["B","S","#","&","@","$","%","*","!",":","."]
    new_pixels = [chars[pixel//25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)

    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)

    with open(output, "w") as f:
        f.write(ascii_image)
    return ascii_image