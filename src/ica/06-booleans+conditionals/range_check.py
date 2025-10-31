# checks if number is between 1-10, changes it if not in range to be 1 if too low,
# 10 if too high

def range_limit(num):
    if 1 <= num <= 10:
        return num
    elif num < 1:
        return 1
    elif num > 10:
        return 10

print(range_limit(5))

if __name__ == "__main__":
  assert range_limit(8) == 8
  assert range_limit(-1) == 1
  assert range_limit(50) == 10
  print("All tests passed!")
