import random


def is_primer(n):
    if n == 2 or n == 3:
        return 1

    if n % 6 != 1 and n % 6 != 5:
        return 0

    i = 5
    while i <= n**(1/2):
        if n % i == 0:
            return 0
        i += 1

    return 1


def rprimers(n):
    for i in range(2, n+1):
        if is_primer(i):
            yield i


def rangePrimers(*args):
    """generator of range primers
    [start,end)
    rangePrimers(end)
    rangePrimers(start,end)
    """
    if len(args) == 1:
        start = 2
        end, = args  # args like (int,) not (int)
    elif len(args) == 2:
        start, end = args
    else:
        print("too many or too less args")
        start = 2
        end = 100

    for i in range(start, end):
        if is_primer(i):
            yield i


def howManyArgs(*args):
    print(len(args))
    print(args)


def nprimers(n):
    count = 0
    i = 2
    while count < n:
        if is_primer(i):
            yield i
            count += 1
        i += 1


# random?

# [start,end] char
def randomChar(start=97, end=122):
    return chr(random.randint(start, end))


def randomStr():
    r = []
    for i in range(random.randint(3, 5)):
        r.append(randomChar())
    return "".join(r)


def randomDic(num=5):
    rdic = {}
    for i in range(num):
        rdic["key-"+randomStr()] = "value-"+randomStr()
    return rdic


def randomList(length=5):
    return [random.randint(0, 100) for i in range(length)]

def randomInts(length=100,start=0,end=100):
    yield random.randit(start,end)

# math

# 等差数列?
def Sn(a1,an,n,d=None):
    if d!=None:
        n = 1 + (an-a1)/d
        
    return n*(a1+an)/2

# 等比数列
def Sq(a1,an,n,q=None):
    if q!=None:
        n = 1 + (an-a1)/d
        
    return n*(a1+an)/2