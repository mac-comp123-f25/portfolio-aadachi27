# count how frequently words occur in a document

import string

def compute_frequencies(file_name):
    text = open(file_name, "r")
    text = text.read()
    text = text.split()

    new_text = []

    for word in text:
        for character in word:
            if character in string.punctuation:
                word = word.replace(character, "")
        new_text.append(word)

    freq_dict = {}

    for word in new_text:
        if word in freq_dict.keys():
            freq_dict[word] = freq_dict[word] + 1
        else:
            freq_dict[word] = 1


    return freq_dict

print(compute_frequencies("../TextFiles/alice.txt"))





