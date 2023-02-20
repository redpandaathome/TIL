# arr2 = arr.sort() will be None cos .sort() does not return value
# use sorted(~)
# set(), list(), sorted(), ('').join

def longest(a1, a2):
    # your code
    newList = ('').join(sorted(list(set(a1+a2))))
    return newList