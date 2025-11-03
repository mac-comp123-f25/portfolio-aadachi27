# count how frequently words occur in a document


def compute_frequencies(file_name):
    text = open(file_name, "r")
    print(text.read())

compute_frequencies("../TextFiles/alice.txt")





