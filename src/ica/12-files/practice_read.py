# open alice text file and print each line

file_in = open("../TextFiles/alice.txt", 'r')
count = 0
for text_line in file_in:
  text_line = text_line.strip()    # remove newline from end of line
  print("Line", count, ":", text_line)
  count = count + 1
file_in.close()


