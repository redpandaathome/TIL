# to split char by char... [x for x in string]
# sorted with two conditions... sorted(arr, key=lambda x: (x[0], x[1]))

def order_weight(string):
    arr=string.split()
    arr2=[]
    for el in arr:
        tempSum= sum([int(x) for x in el])
        arr2.append([el, tempSum])
    arr2=sorted(arr2, key=lambda x: (x[1], x[0]))
    return ' '.join([x[0] for x in arr2])

#1
def order_weight(_str):
    return ' '.join(sorted(sorted(_str.split(' ')), key=lambda x: sum(int(c) for c in x)))