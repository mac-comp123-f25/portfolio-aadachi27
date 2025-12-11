from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def red_channel(pic):
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        new_pic.setColor(x, y, (r, 0, 0))
    return new_pic

def green_channel(pic):
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        new_pic.setColor(x, y, (0, g, 0))
    return new_pic

def blue_channel(pic):
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        new_pic.setColor(x, y, (0, 0, b))
    return new_pic

pine = Picture("../SampleImages/bristleconePine.jpg")
red_pine = red_channel(pine)
red_pine.show()
green_pine = green_channel(pine)
green_pine.show()
blue_pine = blue_channel(pine)
blue_pine.show()

keep_windows_open()
