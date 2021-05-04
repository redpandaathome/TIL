# https://www.acmicpc.net/problem/2178
# 미로탐색
# 이런 최단거리포인트(0,0 ->n-1,m-1) 문제는 bfs로 풀면 간단하구나

import sys
from collections import deque
input = sys.stdin.readline()

n, m = map(int, input.split())
# print(n, m)
arr = []
for i in range(n):
    temp = sys.stdin.readline().strip()
    arr.append(list(map(int, temp)))

#... 인덱스 n,m살려서 하려면 입력 어떻게 받아야 할까?

#0,0 -> n-1,m-1
# dfs? bfs?
visited = [[False]*m for i in range(n)]
# print(visited)

dx = [1,-1,0,0]
dy = [0,0,-1,1]


def bfs(x, y):
    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if 0>nx or nx>=n or 0>ny or ny>=m or visited[nx][ny]==True:
                continue
            if arr[nx][ny]==1:
                arr[nx][ny] = arr[x][y]+1
                q.append((nx,ny))


bfs(0,0)
# print(arr)
print(arr[n-1][m-1])
