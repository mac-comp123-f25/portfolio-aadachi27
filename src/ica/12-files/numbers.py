# write out numbers 1 to n in a text file, with one number on each line

def write_to_n(n, file_name):
    text_file = open(file_name, "w")
    for num in list(range(1, n + 1)):
        num_str = str(num) + "\n"
        text_file.write(num_str)

write_to_n(5, "../TextFiles/numbers_text")