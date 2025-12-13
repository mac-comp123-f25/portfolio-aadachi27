

def countdown(n):
    if n == 0:
        print("Blast Off!")
        return
    else:
        print(n)
        n = n - 1
        countdown(n)


countdown(5)
