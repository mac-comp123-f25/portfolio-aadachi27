from src.ica.helpers.dummyWindow import keep_windows_open
from src.ica.helpers.imageTools import *

def simple_blend(pic1, pic2):
    new_pic = Picture(pic1.getWidth(), pic1.getHeight())
    for (x, y) in pic1:
        (r1, g1, b1) = pic1.getColor(x, y)
        (r2, g2, b2) = pic2.getColor(x, y)
        r = (r1 + r2) / 2
        g = (g1 + g2) / 2
        b = (b1 + b2) / 2
        new_pic.setColor(x, y, (r, g, b))
    return new_pic

def blend2(pic1, pic2):
    width = min(pic1.getWidth(), pic2.getWidth())
    height = min(pic1.getHeight(), pic2.getHeight())
    new_pic = Picture(width, height)
    for (x, y) in new_pic:
        (r1, g1, b1) = pic1.getColor(x, y)
        (r2, g2, b2) = pic2.getColor(x, y)
        r = (r1 + r2) / 2
        g = (g1 + g2) / 2
        b = (b1 + b2) / 2
        new_pic.setColor(x, y, (r, g, b))
    return new_pic

def weighted_blend(pic1, pic2, wgt1):
    wgt2 = 1.0 - wgt1
    width = min(pic1.getWidth(), pic2.getWidth())
    height = min(pic1.getHeight(), pic2.getHeight())
    new_pic = Picture(width, height)
    for (x, y) in new_pic:
        (r1, g1, b1) = pic1.getColor(x, y)
        (r2, g2, b2) = pic2.getColor(x, y)
        r = wgt1 * r1 + wgt2 * r2
        g = wgt1 * g1 + wgt2* g2
        b = wgt1 * b1 + wgt2 * b2
        new_pic.setColor(x, y, (r, g, b))
    return new_pic

p1 = Picture("../SampleImages/daylilies.jpg")
p2 = Picture("../SampleImages/wildColumbine.jpg")
p3 = simple_blend(p1, p2)
p3.show()

forest = Picture("../SampleImages/glacierOldBurn2.jpg")
muir = Picture("../SampleImages/muirWoods.jpg")
blend = blend2(forest, muir)
blend.show()

weight_blend = weighted_blend(forest, muir, 0.7)
weight_blend.show()
weight_blend2 = weighted_blend(forest, muir, 0.3)
weight_blend2.show()

keep_windows_open()