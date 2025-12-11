from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def negative(pic):
    pic = Picture(pic)
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        new_pic.setColor(x, y, (255 - r, 255 - g, 255 - b))
    new_pic.show()

negative("../SampleImages/butterfly.jpg")
negative("../SampleImages/daylilies.jpg")
keep_windows_open()