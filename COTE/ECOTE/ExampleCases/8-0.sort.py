
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
for i in range(1, len(array)):
  for j in range(i, 0, -1):
    if array[j]<array[j-1]:
      array[j], array[j-1] = array[j-1], array[j]
    else:
      break


### Quick Sort
