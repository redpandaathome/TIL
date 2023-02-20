# https://www.acmicpc.net/problem/2309

from itertools import combinations
import sys
input = sys.stdin.readline

arr = []
for i in range(9):
    arr.append(int(input()))
# print(arr)

combi = combinations(arr, 7)
for i in combi:
    # print(i)
    if sum(i) == 100:
        ans = sorted(list(i))
        for i in ans:
            print(i)
        break