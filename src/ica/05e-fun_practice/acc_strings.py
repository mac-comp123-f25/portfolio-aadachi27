# function to repeat a string

def copy_str(string, num_times):
    ans_str = "" # initialize accumulator - empty string
    for x in range(num_times):
        ans_str = ans_str + string # update accumulator
    print(ans_str)
    return ans_str

copy_str("I don't get cute, I get drop dead gorgeous. ", 10)

