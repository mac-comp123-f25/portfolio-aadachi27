from src.ica.helpers.dummyWindow import keep_windows_open
from src.ica.helpers.imageTools import *
import math

def scale_down(pic):
    new_width = math.ceil(pic.getWidth() / 2 )
    new_height = math.ceil(pic.getHeight() / 2 )
    new_pic = Picture(new_width, new_height)
    pic_x = 0
    pic_y = 0
    for (x, y) in new_pic:
        color = pic.getColor(x * 2, y * 2)
        new_pic.setColor(x, y, color)
    return new_pic

def scale_up(pic):
    new_width = 2 * pic.getWidth()
    new_height = 2 * pic.getHeight()
    new_pic = Picture(new_width, new_height)
    new_x = 0
    new_y = 0
    for x in range(0, new_width, 2):
        for y in range(0, new_height, 2):
            color = pic.getColor(x / 2, y / 2)
            new_pic.setColor(x, y, color)
            new_pic.setColor(x + 1, y, color)
            new_pic.setColor(x, y + 1, color)
            new_pic.setColor(x + 1, y + 1, color)


    return new_pic


lake = Picture("../SampleImages/bearLake.jpg")
lake.show()
crop_lake = scale_down(lake)
crop_lake.show()

canyon = Picture("../SampleImages/canyonlands.jpg")
canyon.show()
scale_canyon = scale_up(canyon)
scale_canyon.show()

keep_windows_open()



