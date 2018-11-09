import random
from math import sqrt,factorial

def indexAll(l,v):
    tmp = []
    i = 0
    while i<len(l):
        try:
            i = l.index(v,i)
            tmp.append(i)
        except ValueError:
            return tmp

        i+=1
    return tmp

def splitList(l,v):
    tmp = []
    tmpindex = indexAll(l,v)
    tmpindex = tmpindex

    tmp.append(l[:tmpindex[0]])

    i = 0
    while i<len(tmpindex)-1:
        tmp.append(l[tmpindex[i]+1:tmpindex[i+1]])
        i+=1

    tmp.append(l[tmpindex[-1]+1:])
    return tmp
    


def splitNum(n):
    ans = []
    while n>0:
        ans.append(n%10)
        n//=10
    return ans

# 排列组合 C_n^m
def C(n,m):
    return math.factorial(n)//(math.factorial(n-m)*math.factorial(m))

# 因数分解
def Factorization(n):
    res = []
    for i in range(1,int(sqrt(n))+1):
        if n%i == 0:
            res.append(i)
            res.append(n//i)
    return res


def decToN(i,base):
    if i==0:
        return "0"
    ans = []
    flag = 0

    if i<0:
        flag = 1
        i = abs(i)

    while i>0:
        ans.append(str(i%base))
        i//=7

    if flag:
        ans.append('-')
    ans.reverse()

    return "".join(ans)

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