
### Selection Sort
# Select the smallest data and swipe with the first item → repeat
# O(N2) : N+(N-1)+...+2 =>(n2 + n)/2
# Multiple for loop ->O2
# Data *10 => time complexity*100 💩
# To learn how to find the smallest data in a list👍

array = [7,5,9,0,3,1,6,2,4,8]

# 1
sortedArray = sorted(array)
for i in range(len(array)):
  targetIdx = array.index(sortedArray[i])
  array[i], array[targetIdx] = array[targetIdx], array[i]
  print("after swipe...", array)

print("ARR:", array)

# 2✨
for i in range(len(array)):
  min_index = i
  for j in range(i+1, len(array)):
    if array[min_index]> array[j]:
      min_index = j
  array[min_index], array[i] = array[i], array[min_index]
print(array)


### Insertion Sort
# time complexity - O(N2) - dual for loops
# if the list is almost sorted -> fast O(N)! if not->O(N2)💩
for i in range(1, len(array)):
  #given that ~i is sorted -> find right spot in sorted array and insert
  for j in range(i, 0, -1):
    if array[j]<array[j-1]:
      array[j], array[j-1] = array[j-1], array[j]
    else:
      break


### Quick Sort
# set the standard and swap smaller and bigger data based on it
# time complexity - O(NlogN) 
array = [5,7,9,0,3,1,6,2,4,8]
#1.
def quick_sort(array, start, end):
  if start>=end:
    return
  pivot = start #
  left = start+1
  right = end
  while left<=right:
    #repeat till finding bigger data than pivot
    while left <=end and array[left]<=array[pivot]:
      left+=1
    #repeat till finding smaller data than pivot
    while right>start and array[right]>=array[pivot]:
      right-=1
    if left>right:
      array[pivot], array[right] =array[right], array[pivot]
    else:
      array[left], array[right] = array[right], array[left]
  quick_sort(array, start, right-1)
  quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#2.
def quick_sort(array):
  # list contains only one element
  if len(array)<=1:
    return array
  
  pivot = array[0]
  tail = array[1:] #list not including pivot

  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x > pivot]

  return quick_sort(left_side)+[pivot]+quick_sort(right_side)

print(quick_sort(array))


### Count Sort
# time complexity: the number of data: N, biggest number:K ->O(N+K)
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
count = [0] * (max(array) +1)
for i in range(len(array)):
  count[array[i]] += 1

for i in range(len(count)):
  for j in range(count[i]):
    print(i, end=' ')
#0 0 1 1 2 2 3 4 5 5 6 7 8 9 9


### Python Basic sorting...O(NlogN)
array= [7,5,9,0,3,1,6,2,4,8]
# 1.
result = sorted(array)
print(result)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 2.
#sigle variable
array.sort()
print(array)

# 3.
array2 = [('banana',2),('apple',5),('cherry',3)]

def setting(data):
  return data[1]

result2 = sorted(array2, key=setting)
print(result2)
#[('banana', 2), ('cherry', 3), ('apple', 5)]

