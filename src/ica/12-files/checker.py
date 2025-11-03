# return words in text file that contain inputed string

def select_words(s, fn):
    file = open(fn, "r")
    string_list = []
    for line in file:
        if s in line:
            string_list.append(line)
    print(len(string_list))
    return string_list

print(select_words("ii", "../TextFiles/shortcross.txt"))
print(select_words("ii", "../TextFiles/crosswords.txt"))
print(select_words("quo", "../TextFiles/shortcross.txt"))
print(select_words("quo", "../TextFiles/crosswords.txt"))