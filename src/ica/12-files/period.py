# print text up until a period is detected

def up_to_period(file_name):
    text_file = open(file_name, "r")
    text = text_file.read()
    new_string = ""
    for character in text:
        if character != ".":
            new_string = new_string + character
        else:
            new_string = new_string + character
            break
    print(new_string)

up_to_period("../TextFiles/mockingbird.txt")
