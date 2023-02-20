# 다른 사람 코드=> 훨씬 간결하다!

import sys
input = sys.stdin.readline
y, x = map(int, input().split())
graph = []
[graph.append(list(map(int, input().split()))) for _ in range(y)]
dp = [[0 for _ in range(x+1)] for _ in range(y+1)]

for i in range(1, y+1):
    for j in range(1, x+1):
        dp[i][j] = graph[i-1][j-1] + max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

print(dp[y][x])