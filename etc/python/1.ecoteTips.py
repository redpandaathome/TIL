# from collections import deque
# import sys
# input = sys.stdin.readline()
from sys import stdin

# n, m = map(int, input().split())
#히히히히히히 재미땨!
a = [i for i in range(20) if i%2 == 1]
print(a)

#1~9제곱
b = [i*i for i in range(1,10)]
print(b)

c = [1,2,3,4,5,5,5,5,5,5]
# #3,5를 뺀 나머지를 제거하자?
remove_set = {3, 5}

d = [i for i in c if i not in remove_set]
print(d)

arr = ['']
arr = arr[0] + 'a'
print(arr)
