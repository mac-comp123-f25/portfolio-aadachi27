# function to print pairs of numbers from 0 to n-1 and 0 to m-1

def printPairs(n, m):
    """
    Prints pairs of numbers, the first number varies from 0 to n-1 and each first number is paired
    with each second number. The second number varies from 0 to m-1.
    """
    for i in range(n):
        for j in range(m):
            print( "(", i, j, ")" )

printPairs(6, 15)