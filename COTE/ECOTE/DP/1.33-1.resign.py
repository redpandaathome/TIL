#https://www.acmicpc.net/problem/14501

import sys
import copy
# # n, m, v = map(int, sys.stdin.readline().split())

n = int(input())
t = []
p = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    t.append(a)
    p.append(b)
# print(graph)

max_v = 0
dp = [0 for i in range(n)]
for i in range(n-1, -1, -1): #6,5,4,3,2,1,0
    time = t[i]+i
    if time<=n:
        print('p[',i,']:',p[i], i-t[i], dp[i-t[i]])
        dp[i] = max(max_v, p[i]+dp[time])
        max_v = dp[i]
print(max_v)
print(dp)
        
