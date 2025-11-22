

import imagetools
from src.ica.helpers.dummyWindow import *

def grayscale(pic):
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        lumin = (r + g + b) / 3
        new_pic.setColor(x, y, (lumin, lumin, lumin))

    return new_pic


grayscale('src/ica/16-simple-images/test-image.jpg')

keep_windows_open()
