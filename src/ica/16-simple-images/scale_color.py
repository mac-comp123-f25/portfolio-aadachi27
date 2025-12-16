
from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def weighted_scale(pic, w1, w2, w3):
    pic = Picture(pic)
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        lumin = (w1 * r + w2 * g + w3 * b) / 3
        new_pic.setColor(x, y, (lumin, lumin, lumin))
    new_pic.show()


weighted_scale("../SampleImages/raspberries.jpg", 0.2, 0.5, 0.8)
weighted_scale("../SampleImages/raspberries.jpg", 0.8, 0.0, 0.2)


keep_windows_open()
