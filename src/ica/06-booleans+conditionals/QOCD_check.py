# function to test whether phrase contains at least one of 'QOCD' letters

def has_QOCD(phrase):
    if 'Q' in phrase or 'O' in phrase or 'C' in phrase or 'D' in phrase:
        return True
    else:
        return False

if __name__ == "__main__":
  assert has_QOCD("Quick") == True
  assert has_QOCD("Odd") == True
  assert has_QOCD("MAC") == True
  assert has_QOCD("WiLD") == True
  assert has_QOCD("MATH") == False
  assert has_QOCD("comp123") == False
  print("All tests passed!")
