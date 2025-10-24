# find the combination of numbers out of a set of 3 with the least absolute difference

def smallest_diff(x, y, z):
    print('smallest_diff inputs:', x, y, z)
    diff1 = abs(x - y)
    diff2 = abs(y - z)
    diff3 = abs(x - z)
    min_diff = min(diff1, diff2, diff3)
    print(diff1, diff2, diff3, 'return value:', min_diff)
    return min_diff

smallest_diff(3, 9, 5)

'''
Local environment
x         3
y         9
z         5
diff1     6
diff2     4
diff3     2
min_diff  2
'''

smallest_diff(2, 4, 6)

'''
Local environment
x         2
y         4
z         6
diff1     2
diff2     2
diff3     4
min_diff  2
'''