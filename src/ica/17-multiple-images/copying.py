from src.ica.helpers.dummyWindow import keep_windows_open
from src.ica.helpers.imageTools import *

def copy_pic_into(small_pic, big_pic, start_x, start_y):
    for (x, y) in small_pic:
        color = small_pic.getColor(x, y)
        new_x = start_x + x
        new_y = start_y + y
        big_pic.setColor(new_x, new_y, color)

green_turtle = Picture("../SampleImages/greenTurtle.jpg")
scene = Picture("../SampleImages/bearLake.jpg")
copy_pic_into(green_turtle, scene, 25, 25)
copy_pic_into(green_turtle, scene, 200, 200)
copy_pic_into(green_turtle, scene, 400, 200)
scene.show()

keep_windows_open()
