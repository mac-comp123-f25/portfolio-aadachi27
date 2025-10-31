# print string of numbers from 0 to num

def string_of_nums(num):
    string = ""
    for x in range(num + 1):
        x = str(x)
        string = string + x + " "
    print(string)

string_of_nums(15)