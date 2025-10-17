# remove every instance of input value from input list

def remove_all(value, list):
    while list.count(value) > 0:
        list.remove(value)
    return list

print(remove_all(2, [2, 8, 7, 3, 5, 2]))