import random

from src.ica.helpers.dummyWindow import keep_windows_open
from src.ica.helpers.imageTools import *

def copy_pic_rand(small_pic, big_pic):
    start_x = random.randint(0, (big_pic.width - small_pic.width))
    start_y = random.randint(0, (big_pic.height - small_pic.height))
    for (x, y) in small_pic:
        color = small_pic.getColor(x, y)
        new_x = start_x + x
        new_y = start_y + y
        big_pic.setColor(new_x, new_y, color)

green_turtle = Picture("../SampleImages/greenTurtle.jpg")
scene = Picture("../SampleImages/bearLake.jpg")
copy_pic_rand(green_turtle, scene)
scene.show()
keep_windows_open()
