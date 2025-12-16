from my_sum import *

def test_sum3_ints():
    assert sum3([0, 1, 2, 3, 4, 5]) == 3
    assert sum3([5, 2, 8, -2, 6, 15]) == 15
    assert sum3([1, 2, 3, "h", "i"]) == 6

def test_sum3_floats():
    assert sum3([0.0, 1.0, 2.0, 3.0, 4.0, 5.0]) == 3.0
    assert sum3([1.2, 2.2, 3.2, 4.2, 5.2, 6.2]) == 6.6000000000000005