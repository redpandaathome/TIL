
# first trial - time out 💩🚽💩🚽💩🚽💩🚽
def sum_for_list(lst):
    sums=[]
    lst_abs=[abs(x) for x in lst]
    max_val=max(lst_abs)
    for i in range(2,max_val+1):
        if is_prime(i):
            temp_sum=0
            is_valid=False
            for x in lst:
                if x%i==0:
                    is_valid=True
                    temp_sum+=x
            if is_valid:
                sums.append([i, temp_sum])
    return sorted(sums)

    
def is_prime(n):
    possible_nums = (x for x in range(2,n+1) if x*x<n+1)
    for i in possible_nums:
        if n%i==0:
            return False
    return True


#solution1 ✨✨✨
# [ ]
def prime_factors(n):
    i = 2
    factors = []
    if n < 0:
        n *= -1
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def combine(arr1, arr2):
    for a in arr1:
        if not a in arr2:
            arr2.append(a)
    return arr2

def sum_for_list(lst):
    factors=[]
    sums=[]
    for i in range(len(lst)):
        combine(prime_factors(lst[i]), factors)
    for f in factors:
        temp_sum=0
        for l in lst:
            if l%f==0:
                temp_sum+=l
        sums.append([f, temp_sum])
    sums.sort(key=lambda x:x[0])
    return sums