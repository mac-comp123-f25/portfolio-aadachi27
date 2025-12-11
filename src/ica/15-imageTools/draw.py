from src.ica.helpers.dummyWindow import *
from src.ica.helpers.imageTools import *

def draw_something():
    pic = Picture(500, 500)

    pic.drawPolygon([(190, 250), (235, 250), (250, 200),
                              (265, 250), (310, 250), (270, 275),
                              (280, 320), (250, 290), (215, 320), (230, 275)],
                    "black", "pink")
    return pic



def main():
    drawing = draw_something()
    drawing.show()

    keep_windows_open()


if __name__ == "__main__":
    main()
