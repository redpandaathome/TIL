#https://www.acmicpc.net/problem/1932

#굳이 deepcopy 안했어도...ㅇㅋ

import sys
import copy
# # n, m, v = map(int, sys.stdin.readline().split())

t = int(input())
graph = []
for i in range(t):
    graph.append(list(map(int, sys.stdin.readline().split())))
# print(graph)

dp = copy.deepcopy(graph)

for i in range(1, t):
    for j in range(len(dp[i])):
        if j==0:
            left = 0
        else:
            left = dp[i-1][j-1]
        if j== len(dp[i])-1:
            right = 0
        else:
            right = dp[i-1][j]
        dp[i][j]= dp[i][j]+max(left, right)
    print('------------------------')
print(max(dp[t-1]))