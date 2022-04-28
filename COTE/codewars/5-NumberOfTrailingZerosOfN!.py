import math

def zeros(n):
    zs = 0
    while n > 0:
        n = math.floor(n / 5)
        zs += n
    return zs


#s1 -> does not work haha
def zeros(n):
  x = n/5
  return x+zeros(x) if x else 0

#s2
def zeros(n):
    """
    No factorial is going to have fewer zeros than the factorial of a smaller
    number.

    Each multiple of 5 adds a 0, so first we count how many multiples of 5 are
    smaller than `n` (`n // 5`).

    Each multiple of 25 adds two 0's, so next we add another 0 for each multiple
    of 25 smaller than n.

    We continue on for all powers of 5 smaller than (or equal to) n.
    """
    pow_of_5 = 5
    zeros = 0
    
    while n >= pow_of_5:
        zeros += n // pow_of_5
        pow_of_5 *= 5
        
    return zeros