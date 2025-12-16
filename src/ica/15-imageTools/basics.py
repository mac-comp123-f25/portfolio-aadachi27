

from src.ica.helpers.imageTools import *

def num_pixels(img):
    # find and print number of pixels in image
    pic = Picture(img)
    width = pic.getWidth()
    height = pic.getHeight()
    print(width * height, "pixels")
    # copy image and change corners to red
    new_pic = pic.copy()
    new_pic.setColor(0, 0, (255, 0, 0))
    new_pic.setColor(0, (height-1), (255, 0, 0))
    new_pic.setColor((width-1), 0, (255, 0, 0))
    new_pic.setColor((width-1), (height-1), (255, 0, 0))
    new_pic.save("mightyMidway-redCorners.jpg")

num_pixels("mightyMidway.jpg")