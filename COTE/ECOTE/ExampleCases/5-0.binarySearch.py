#input
10 7
1 3 5 7 9 11 13 15 17 19

#output
4

#input2
10 7
1 3 5 6 9 11 13 15 17 19

#output2
'none matching'

# Binary search
# when data is sorted!
# When you need to search more than 20 million -> think about binary search...O(NlogN)
# Database has its data sorted by tree data structure -> support fast searching by using similar algorithm of binary search

# 1. recursive
def binary_search(array, target, start, end):
  #✨ in case of mid = (start:5, end:5)//2 = 5 -> start>=end!
  if start >= end:
    return None
  mid = (start+end)//2
  if array[mid]==target:
    return mid+1
  elif array[mid]>target:
     # ✨ don't miss to return...!
    return binary_search(array, target, start, mid-1)
  else:
     # ✨ don't miss to return...!
    return binary_search(array, target, mid+1, end)


n, target = map(int, input().split())
array = list(map(int, input().split()))
result = binary_search(array, target, 0, len(array)-1)

print(result)

# 2. repeatitive
# Binary search with recursive code

def binary_search(array, target, start, end):
  if start > end:
    return None
  # print("CALLED...", start, end)
  while start <= end:
    mid = (start+end)//2
    # print("start&end:", start, end, ",mid&v:", mid, array[mid])
    if array[mid]==target:
      return mid+1
    elif array[mid]<target:
      start = mid+1
    else:
      end = mid-1


n, target = map(int, input().split())
array = list(map(int, input().split()))
result = binary_search(array, target, 0, len(array)-1)

print(result)


# binary search tree
# left child < parent node < right child
