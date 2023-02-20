
#

# 2. repetitive
def binary_search(array, target, start, end):
  # print(">>>target:", target, ", start&end:", start, end)
  if start>end:
    # print("start>end...return 0!")
    return 0
  while start<=end:
    mid = (start+end)//2
    # print("mid:", mid, array[mid])
    if array[mid]==target:
      # print("matching!, array[",mid,"]",array[mid], "... returning 1")
      return 1
    elif array[mid]>target:
      end = mid-1
    else:
      start = mid+1
    # print('---New start&end', start, end)


n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
array2 = list(map(int, input().split()))
result = []
for target in array2:
  if binary_search(array, target, 0, len(array)-1) == None:
    print(0)
  else:
    print(1)

#✨✨✨
# return 0 -> return None?
# return '0\n'