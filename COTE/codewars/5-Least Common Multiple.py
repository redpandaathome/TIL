import functools
def lcm(*args):
    arr=list(args)
    if len(arr)==0:
        return 1
    print(arr)
    result=functools.reduce(lambda a,b: a*b/gcd(a,b) if gcd(a,b) else 0, arr) 

    return result

def gcd(a,b):
    if b==0:
        return a
    return gcd(b, a%b)

#1
from math import gcd
from functools import reduce
from operator import mul

def lcm(*args):
    return 1 if not args else reduce(lambda a, b: mul(a, b) // gcd(a, b), args)

#2
from math import gcd
def lcm(*args):
    lcm=1
    for x in args:
        if x!=0:
            lcm=lcm*x//gcd(lcm,x)
        else:
            lcm=0
    return lcm

#3
def lcm(*args):
    gcd = lambda m,n: m if not n else gcd(n,m%n)
    return reduce( lambda x, y: x*y/gcd(x, y), args)