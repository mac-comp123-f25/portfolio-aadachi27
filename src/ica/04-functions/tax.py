# calculate tax and return total price including tax

def add_tax(price, tax_rate):
    print('add_tax inputs:', price, tax_rate)
    tax_amt = price * tax_rate
    print(tax_amt, price + tax_amt)
    return price + tax_amt

add_tax(25.99, 0.0725)

'''
Local environment
    price            25.99
    tax_rate         0.0725
    tax_amt          1.884275
    price + tax_amt  27.874275
'''