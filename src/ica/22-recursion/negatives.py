

def count_negatives(nums : list):
    if len(nums) == 0:
        return 0
    else:
        first_num = nums[0]
        rest_num = count_negatives(nums[1:])
        if first_num < 0:
            neg = 1
            return neg + rest_num
        else:
            return rest_num


print(count_negatives([1, 2, 3, -1, -2, -3]))
print(count_negatives([-3, 0, 1]))
