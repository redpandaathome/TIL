#https://www.acmicpc.net/problem/11399

import sys
# n, m, v = map(int, sys.stdin.readline().split())

n = int(input())
arr =list(map(int, input().split()))
arr.sort()
# print(arr)
newArr= []
for i in range(n):
  newArr.append(arr[i]+newArr[i-1]) if i>=1 else newArr.append(arr[i])
# print(newArr)
print(sum(newArr))

