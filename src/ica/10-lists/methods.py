# find minimum and maximum

def end_points(num_list):
    tuple = num_list
    largest = num_list[0]
    smallest = num_list[0]
    for x in num_list:
        if x >= largest:
            largest = x
    for x in num_list:
        if x <= smallest:
            smallest = x
    print(largest, "and", smallest)
    return largest, smallest

print(end_points([1, 2, 3, 4, 5]))
