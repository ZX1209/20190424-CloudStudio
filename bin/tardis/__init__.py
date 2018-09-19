def is_primer(n):
    i = 2
    if n % 6 != 1 and n % 6 != 5:
        return 0

    while i <= n**(1/2):
        if n%i == 0 :
            return 0
        i += 1

    return 1

def primers(n):
    for i in range(2,n):
        if is_primer(i):
            yield i
