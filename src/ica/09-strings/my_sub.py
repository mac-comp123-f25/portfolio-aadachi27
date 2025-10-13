

def name_subst(name, sentence):
    new_sentence = sentence.replace("ZZZ", name)
    return new_sentence

print(name_subst("Annabelle", "My friend ZZZ is very kind."))

