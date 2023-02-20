# check if key exists... not in...
# declare new key in dict
# var = val1 if cond else val2
# result[c]+=1 if c in result else 1
# You can't do result[c]+1 if c in result else reuslt[c]=1 
def scramble(s1, s2):
    obj1=count_char(s1)
    obj2=count_char(s2)
    for c in obj2:
        if c not in obj1 or obj2[c]>obj1[c]:
            return False
    return True
    

def count_char(s):
    result={}
    for c in s:
        if c in result:
            result[c]+=1
        else:
            result[c]=1
    return result


#try2
# you can't use -- or ++ in python. just redeclare the value.
def scramble(s1, s2):
    obj1=count_char(s1)
    for c in s2:
        if c not in obj1:
            return False
        obj1[c]=obj1[c]-1
        if obj1[c]<0:
            return False
    return True
    

def count_char(s):
    result={}
    for c in s:
        if c in result:
            result[c]+=1
        else:
            result[c]=1
    return result

#simple sol
# str.count(c)
def scramble(s1,s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True

#try
def scramble(s1, s2):
    for c in s2:
        if s1.count(c) <s2.count(c):
            return False
    return True

#s2
# import Counter
from collections import Counter
def scramble(s1,s2):
    # Counter basically creates a dictionary of counts and letters
    # Using set subtraction, we know that if anything is left over,
    # something exists in s2 that doesn't exist in s1
    return len(Counter(s2)- Counter(s1)) == 0