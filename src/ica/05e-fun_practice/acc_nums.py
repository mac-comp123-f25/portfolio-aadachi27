# add sum of list of numbers in specified range

def sum_range(start_val, end_val):
    cnt = 0 # initialize accumulator
    for x in range(start_val, end_val + 1):
        cnt = cnt + x # update accumulator
    return cnt

print(sum_range(5, 10))

print(sum_range(25, 25))

print(sum_range(10, 4))

print(sum_range(-2, -13))
