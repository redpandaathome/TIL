# input
5
8 3 7 9 2
3
5 7 9

# output
no yes yes

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()

def binary_search(arr, target, start, end):
  if start > end:
    return None
  mid = (start+end)//2
  # print("mid&val:", mid, arr[mid],", start&end:", start, end)
  if arr[mid]==target:
    # print("matched!", arr[mid])
    return mid
  elif arr[mid] > target:
    return binary_search(arr, target, start, mid-1)
  else:
    return binary_search(arr, target, mid+1, end)

for i in arr2:
  # print()
  # print("target:",i)
  if binary_search(arr1, i, 0, len(arr1)-1) == None:
    print('no', end=' ')
  else:
    print('yes', end=' ')
