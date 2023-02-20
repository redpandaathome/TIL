# dict type {}
# to check if key exists... i in dict
# ternary operator True if a==b else False
import string

def is_pangram(s):
    standardArr = list('abcdefghijklmnopqrstuvwxyz')
    count=0
    countObj = {}
    for i in list(s.lower()):
        if i!=" " and i not in countObj and i in standardArr:
            count+=1
            countObj[i]=0
    return True if count==26 else False

#Improved1 
# string.ascii_lowercase
# set(str1) <= set(str2)
import string

def is_pangram(s):
    return set(string.ascii_lowercase) <= set(s.lower())

#Improved2
#
import string

def is_pangram(s):
    s= s.lower()
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if i not in s:
            return False
    # return out side of for loop!
    return True

#Improved3
# The all() function returns True if all items in an iterable are true
# all(letter in str1 for letter in str2)✨
import string

def is_pangram(s):
    s = s.lower()
    return all(letter in s for letter in string.lowercase)