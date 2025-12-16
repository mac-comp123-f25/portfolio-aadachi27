

def every_other(list):
    length = int(len(list))
    return(list[1:length:2])

def sum_positive(sumlist):
    sum = 0
    for x in sumlist:
        if x > 0 :
            sum = sum + x
    return sum

print(every_other([2, 4, 6, 8]))

print(sum_positive([2, 5, 5, -3]))

