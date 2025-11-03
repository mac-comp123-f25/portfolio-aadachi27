# read text file and print first 20 characters in each line

def print_abbrev(file_name):
    text = open(file_name, "r")
    for text_line in text:
        text_line = text_line.strip()
        text_line = text_line[0:20]
        print(text_line)
    text.close()

print_abbrev("../TextFiles/alice.txt")