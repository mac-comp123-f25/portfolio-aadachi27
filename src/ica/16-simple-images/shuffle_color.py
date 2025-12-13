from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def color_shuffle(pic):
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        new_pic.setColor(x, y, (b, r, g))
    return new_pic

mushrooms0 = Picture("../SampleImages/mushrooms.jpg")
mushrooms0.show()
mushrooms1 = color_shuffle(mushrooms0)
mushrooms1.show()
mushrooms2 = color_shuffle(mushrooms1)
mushrooms2.show()

keep_windows_open()

