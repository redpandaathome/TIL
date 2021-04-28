# itertools.combinations(iterable, r)
import itertools
arr = [0,1,2,3,3,5]
d=1
checkedList=[]
a = list(itertools.combinations(arr,2))
for i in a:
    if sum(i)//2 <=d:
        checkedList.append(i)
print(checkedList)
