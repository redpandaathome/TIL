# https://www.acmicpc.net/problem/11724
# 연결 요소의 갯수

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

ans = 0
visited = [False] * (n+1)
def dfs(arr, start, visited):
    visited[start] = True
    for i in arr[start]:
        if not visited[i]:
            dfs(arr, i, visited)

for i in range(1, n+1):
    if not visited[i]:
        dfs(arr, i, visited)
        ans+=1

print(ans)