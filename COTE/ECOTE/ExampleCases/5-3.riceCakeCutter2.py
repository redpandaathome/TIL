# input
4 6
19 15 10 17

#output
15

n, m = map(int,input().split())
array = list(map(int, input().split()))

#✨ think about why sorting is not necessary here...
#array.sort() 
print(array)
def binary_search(array, target, start, end):
  if start > end:
    return None
  while start <=end:
    mid = (start+end)//2
    sum = 0
    for i in array:
      cut = i-mid
      if cut >0:
        sum += cut
    if sum == target:
      return mid
    elif sum<target:
      end = mid-1
    else:
      start = mid+1

  

#✨ 0~max(array)-1
result = binary_search(array, m, 0, max(array)-1)

print(result)