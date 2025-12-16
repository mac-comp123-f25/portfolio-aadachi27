# function that determines whether letter 'q' is in string

def has_q(words):
    if 'q' in words:
        return True
    else:
        return False

print(has_q("qwertyui"))
print(has_q("wertyui"))

if __name__ == "__main__":
  assert has_q("quick") == True
  assert has_q("math") == False
  print("All tests passed!")
