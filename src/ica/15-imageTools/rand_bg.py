import time
import random
from src.ica.helpers.dummyWindow import *
from src.ica.helpers.imageTools import *



def get_rand_bg():
    pic = Picture(100, 100)
    red = random.randrange(0, 255)
    green = random.randrange(0, 255)
    blue = random.randrange(0, 255)
    pic.setAllPixels((red, green, blue))
    return pic




def main():
    for i in range(10):
        pic = get_rand_bg()
        pic.show()
        time.sleep(1)

    keep_windows_open()


if __name__ == "__main__":
    main()
