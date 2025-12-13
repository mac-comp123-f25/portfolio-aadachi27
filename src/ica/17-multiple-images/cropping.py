from src.ica.helpers.dummyWindow import keep_windows_open
from src.ica.helpers.imageTools import *

def crop_picture(pic, up_left_x, up_left_y, crop_width, crop_height):
    crop_pic = Picture(crop_width, crop_height)
    for (x , y) in crop_pic:
        new_x = x + up_left_x
        new_y = y + up_left_y
        color = pic.getColor((new_x), (new_y))
        crop_pic.setColor(x, y, color)
    return crop_pic

dam = Picture("../SampleImages/hooverDam.jpg")
dam_crop1 = crop_picture(dam, 260, 90, 240, 210)
dam_crop2 = crop_picture(dam, 100, 150, 100, 150)
dam_crop1.show()
dam_crop2.show()

keep_windows_open()