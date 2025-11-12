# sum3 function adds up first three items in inputted list - only if input is list, is
# at least 3 long, and first three items in list are integers

def sum3(my_list):
    assert type(my_list) in [list]
    assert len(my_list) >= 3
    assert type(my_list[0]) in [int, float]
    assert type(my_list[1]) in [int, float]
    assert type(my_list[2]) in [int, float]
    return my_list[0] + my_list[1] + my_list[2]

print(sum3([0, 1, 2, 'a', 'b', 'c']))

if __name__ == "__main__":
  print( sum3([5, 2, 8, -2, 6, 15]) )
  print( sum3([5, 2]) ) # assertion error: list too short, length of list < 3
  print( sum3(5) ) # assertion error: input given is not a list
  print( sum3(["h", "i", 1, 2, 3]) ) # assertion error: first 3 in list not ints
  print( sum3([1, 2, 3, "h", "i"]) )



