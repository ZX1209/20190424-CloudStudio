import random

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


# random?

# [start,end] char
def randomChar(start=97,end=122):
    return chr(random.randint(start,end))

def randomStr():
    r = []
    for i in range(random.randint(3,5)):
        r.append(randomChar())
    return "".join(r)


def randomDic(num=5):
    rdic = {}
    for i in range(num):
        rdic["key-"+randomStr()] = "value-"+randomStr()
    return rdic

def randomList(length=5):
    return [random.randint(0,100) for i in range(length)]