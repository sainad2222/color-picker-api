# ________________________IMPORTS__________________________
import cv2
from collections import defaultdict

# _______________________FUNCTIONS_________________________
def rgb_to_hex(rgba_color):
    """
    @params:
        rgba_color: tuple of rgb colors
    Return hex string for a given rgb tuple
    """
    if len(rgba_color)>3:
        red, green, blue, _ = rgba_color
    else:
        red,green,blue = rgba_color
    return "#{r:02x}{g:02x}{b:02x}".format(r=red, g=green, b=blue)


def border_color(img):
    """
    @params:
        img: cv2 image object
    Returns dominant color at border from given image
    """
    img = cv2.resize(img, (128, 128))
    colors = defaultdict(int)

    # Top
    for pixel in img[0]:
        colors[tuple(pixel)] += 1

    # Bottom
    for pixel in img[-1]:
        colors[tuple(pixel)] += 1

    # Left
    for row in img:
        colors[tuple(row[0])] += 1

    # Right
    for row in img:
        colors[tuple(row[-1])] += 1
    max_color = max(colors, key=lambda x: x[1])
    return rgb_to_hex(max_color)


def dominant_color(img):
    """
    @params:
        img: cv2 image object
    Returns dominant color from given image
    """
    img = cv2.resize(img, (128, 128))
    colors = defaultdict(int)
    for row in img:
        for pixel in row:
            colors[tuple(pixel)] += 1
    max_color = max(colors, key=lambda x: x[1])
    return rgb_to_hex(max_color)

if __name__ == "__main__":
    pass
