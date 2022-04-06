
# int ! not parseInt 

def persistence(n):
    # your code
    count=0
    while n>9:
        cur=1
        for i in str(n):
            cur=cur*int(i)
        count+=1
        n=cur;
    return count

#interesting - reduce - lambda
import functools
def persistence(n):
    # your code
    count=0
    nums=[int(x) for x in str(n)]
    while len(nums)>1:
        n=functools.reduce(lambda a,b: a*b, nums)
        nums=[int(x) for x in str(n)]
        count+=1
        print("n?",n, ", count?", count)
    return count