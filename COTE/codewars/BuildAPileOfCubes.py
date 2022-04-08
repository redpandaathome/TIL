# pow(num, nth) == num**nth

def find_nb(m):
    # your code
    cur=1
    sum=0
    while sum<m:
        sum+=pow(cur,3)
        if sum==m:
            return cur
        cur+=1
    return -1