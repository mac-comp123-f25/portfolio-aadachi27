"""
Examples of while and for loops for the Iteration activity

@author: Susan Fox
@author: Amin Alhashim
"""


def print_every_other(x):
    """
    Prints every other value from a given number down to zero
    """
    while x >= 0:      # x is the loop variable
        print(x)
        x = x - 2

    # when indentation stops, while loop is over
    print("Done!")

def print_every_fifth(x):
    '''
    prints every fifth value from x down to
    '''
    while x >= 0:
        print(x)
        x = x - 5
    print("Done!")

print_every_fifth(20)

def square_user_nums():
    """
    Reads in numbers from the user, stopping when the user enters a negative
    number. For each user number, it prints the number and the square of
    the number.

    If the user_inp and user_num definitions are taken out from the beginning,
    the while loop isn't able to run because user_num hasn't been defined.

    If the user_inp and user_num definitions are taken out of the while loop,
    the user is only asked to input a number once, and the print statement keeps
    running forever.
    """
    user_inp = input("Enter the next number (negative to quit): ")
    user_num = int(user_inp)
    while user_num >= 0:
        print(user_num, "squared is", user_num ** 2)
        user_inp = input("Enter the next number (negative to quit): ")
        user_num = int(user_inp)

def square_user_nums2():
    while True:
        user_inp = input("Enter the next number (negative to quit): ")
        user_num = int(user_inp)
        if user_num < 0:
            break
        print(user_num, "squared is", user_num ** 2)

print(square_user_nums2())

def sum_to_n(top_num):
    """
    Takes in a number and computes and returns the sum of the numbers
    from zero to the input number.
    """
    curr_val = 0  # loop variable
    total = 0    # accumulator variable
    while curr_val <= top_num:
        total = total + curr_val
        curr_val = curr_val + 3

    return total

def add_user_nums():
    sum_of_nums = 0
    user_num = int(input("enter a number, enter 0 to end "))
    while user_num != 0:
        sum_of_nums = sum_of_nums + user_num
        user_num = int(input("enter a number, enter 0 to end "))
    return(sum_of_nums)

print(add_user_nums())


def next_word(text):
    """
    Takes in a string of text and builds and returns a new string
    that is the next "word" in the text. In other words, the next sequence
    of characters up to a space, tab, or newline.
    """
    word_str = ""
    i = 0
    for ch in text:
        if ch in " \t\n":
            break
        else:
            word_str = word_str + ch
    return word_str


def print_seperator_line():
    """
    Prints a seperator line proceeded by an empty line
    """
    print()
    print("------------------------------")


if __name__ == '__main__':
    print_seperator_line()
    print("Sample calls to printEveryOther:")
    print("printEveryOther(11) does:")
    print_every_other(11)
    print("printEveryOther(4) does:")
    print_every_other(4)

    print_seperator_line()
    print("Sample call to squareUserNums:")
    square_user_nums()

    print_seperator_line()
    print("Sample calls to sumToN:")
    print("sumToN(3) does:")
    print(sum_to_n(3))
    print("sumToN(100) does:")
    print(sum_to_n(100))
    
    print_seperator_line()
    print("Sample calls to nextWord:")
    print("nextWord('Friends, Romans, countrymen') does:")
    print(next_word('Friends, Romans, countrymen'))
    print("nextWord('Bananas and apples') does:")
    print(next_word('Bananas and apples'))
    print("nextWord('Frederick!') does:")
    print(next_word('Frederick!'))
