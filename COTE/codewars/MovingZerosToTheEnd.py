def move_zeros(array):
    return list(filter(checkZero, array))+list(filter(checkNoneZero, array))

def checkZero(x):
    if x!=0:
        return True
    else:
        return False
    
def checkNoneZero(x):
    if x==0:
        return True
    else:
        return False


#improved
def move_zeros(array):
    temp = [x for x in array if x!=0]
    return temp+[0]*(len(array)-len(temp))

#
def move_zeros(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)

# why key? https://stackoverflow.com/questions/3766633/how-to-sort-with-lambda-in-python
def move_zeros(array):
    return sorted(array, key=lambda x: x==0)