""""
Implementation of the Aristid Lindenmayer-system (L-systems)

@author: Amin G. Alhashim (aalhashi@macalester.edu)
"""


def apply_l_system(fractal_name):
    assert type(fractal_name) is dict
    assert len(fractal_name) == 3
    assert 'axiom' in fractal_name.keys()
    assert 'rules' in fractal_name.keys()
    assert 'n' in fractal_name.keys()

    #assert type(axiom) is str
    #assert type(rules) is dict
    #assert type(n) is int

    s = fractal_name.get('axiom')
    for _ in range(int(fractal_name.get('n'))):
        s = apply_rules(s, fractal_name.get('rules'))

    return s


def apply_rules(s: str, rules: dict):
    assert type(s) is str
    assert type(rules) is dict

    new_str = ''
    for c in s:
        rule_found = False
        for key in rules:
            if len(key) != 1:
                print("{} -> {} not supported, LHS is not of length "
                      "1".format(key, rules[key]))
                assert False
            if key == c:
                new_str += rules[key]
                rule_found = True
                break

        # no rule
        if not rule_found:
            new_str += c

    return new_str


if __name__ == "__main__":
    axiom = 'A'
    rules = {('A', 'B'), ('B', 'AB')}

    #for i in range(10):
        #print(apply_l_system(axiom, rules, i))
