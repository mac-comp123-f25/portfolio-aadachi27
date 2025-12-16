from src.ica.helpers.dummyWindow import *
from src.ica.helpers.imageTools import *

def change_blue(picture, factor):
    for (x, y) in picture:
        (red, grn, blu) = picture.getColor(x, y)
        new_blue = blu * factor
        picture.setColor(x, y, (new_blue, grn, blu))

def remove_blue(picture):
    for (x, y) in picture:
        (red, grn, blu) = picture.getColor(x, y)
        picture.setColor(x, y, (red, grn, 0))

def fix_green(picture, value):
    for (x, y) in picture:
        (red, grn, blu) = picture.getColor(x, y)
        picture.setColor(x, y, (red, value, blu))



def main():
    # example calls:
    fruit_pic = Picture("../SampleImages/raspberries.jpg")
    corn_pic = Picture("../SampleImages/stateFairCorn.jpg")
    flower_pic = Picture("../SampleImages/wildColumbine.jpg")
    fruit_pic.show()
    change_blue(fruit_pic, -10.0)
    corn_pic.show()
    remove_blue(corn_pic)
    corn_pic.show()
    flower_pic.show()
    fix_green(flower_pic, 50)
    flower_pic.show()

    keep_windows_open()


if __name__ == "__main__":
    main()
