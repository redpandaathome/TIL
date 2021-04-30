# https://www.acmicpc.net/problem/10972
# 다음순열 -> 메모리초과로 실패(256mb) 다른 방법으로 시도해야.

import itertools

n = int(input())
target = tuple(list(map(int, input().split())))
arr = [ i for i in range(1,n+1)]

cases = list(itertools.permutations(arr, n))

# A if 조건 else B
caseLen = len(cases)
index = -1 if cases.index(target)+1 == caseLen else cases.index(target)+1

if index == -1:
    print(-1)
else:
    print(' '.join(map(str, cases[index])))