# calculate area and cost of installing a green roof given width, length, and sqft cost

import math

def estimate_green_roof(wid, len, sqf_cost):
    area = rect_area(wid, len)
    cost = roof_cost(area, sqf_cost)
    print(" Area =", area)
    print(" Cost =", cost)

def rect_area(wid, len):
    wid = math.ceil(wid)
    len = math.ceil(len)
    return wid * len

def roof_cost(area, sqf_cost):
    return area * sqf_cost

estimate_green_roof(32.8, 54.25, 35)