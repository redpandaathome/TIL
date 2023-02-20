# https://wikidocs.net/16038
import copy

# CONCLUSION - PREFER TO USE DEEPCOPY!
# 1.if arr is like [1,2,3], using deepcopy or shallow copy doesn't matter
arr = [1,2,3]
arrA = arr
arrB = copy.deepcopy(arr)
arrC = copy.copy(arr)
arr[0]=10
print("AFTER CHANGING arr[0] to 10...")
print(arr)
print(arrA)
print("deepcopy:",arrB)
print("shallowcopy:",arrC)


arrB[0]=100
print("AFTER CHANGING arrB[0] to 100...")
print(arr)
print(arrA)
print("deepcopy:",arrB)
print("shallowcopy:",arrC)

arrC[0]=99999
print("AFTER CHANGING arrB[0] to 100...")
print(arr)
print(arrA)
print("deepcopy:",arrB)
print("shallowcopy:",arrC)

# AFTER CHANGING arr[0] to 10...
# [10, 2, 3]
# [10, 2, 3]
# deepcopy: [1, 2, 3]
# shallowcopy: [1, 2, 3]
# AFTER CHANGING arrB[0] to 100...
# [10, 2, 3]
# [10, 2, 3]
# deepcopy: [100, 2, 3]
# shallowcopy: [1, 2, 3]
# AFTER CHANGING arrC[0] to 99999...
# [10, 2, 3]
# [10, 2, 3]
# deepcopy: [100, 2, 3]
# shallowcopy: [99999, 2, 3]



# 2. but if arr is compound object... it matters
arr = [[1,2],[3,4]]

arrA = arr

#deepcopy
arrB = copy.deepcopy(arr) # will make  a independant, and new "compound"
#shallowcopy
arrC = copy.copy(arr)

#changing original array...
arr[0][0]=10
print("AFTER CHANGING arr[0][0] to 10...")
print(arr) #[[10, 2], [3, 4]]
print(arrA) #[[10, 2], [3, 4]]
print("deepcopy:",arrB) #[[1, 2], [3, 4]]
print("shallowcopy:",arrC) #[[10, 2], [3, 4]]


#changin deep copied array...
arrB[0][0]=100
print("AFTER CHANGING arrB[0][0] to 100...")
print(arr) #[[10, 2], [3, 4]]
print(arrA) #[[10, 2], [3, 4]]
print("deepcopy:",arrB) #[[100, 2], [3, 4]]
print("shallowcopy:",arrC) #[[10, 2], [3, 4]]

#changing shallo copied array...
arrC[0][0]=99999
print("AFTER CHANGING arrC[0][0] to 100...")
print(arr) #[[99999, 2], [3, 4]]
print(arrA) #[[99999, 2], [3, 4]]
print("deepcopy:",arrB) #[[100, 2], [3, 4]]
print("shallowcopy:",arrC) #[[99999, 2], [3, 4]]