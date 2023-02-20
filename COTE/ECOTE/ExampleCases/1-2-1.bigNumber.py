n, m, k = map(int,input().split())
arr = list(map(int,input().split()))

# 5 8 3
# 2 4 5 4 6
ansArr=[]
arr.sort(reverse=True)

maxCount=0
while len(ansArr)<m:
  if maxCount<k:
    ansArr.append(arr[0])
    maxCount+=1
  else:
    ansArr.append(arr[1])
    maxCount=0

print(ansArr)
print(sum(ansArr))