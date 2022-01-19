import sys
input = sys.stdin.readline
from collections import deque

dx = [0,0,-1,1, -1,1,-1,1]
dy = [-1,1,0,0, -1,1,1,-1]
# def bfs(i,j):
#   q = deque()
#   q.append((i,j))
#   graph[i][j]=2
#   while q:
#     x, y = q.popleft()
#     for t in range(8):
#       nx = dx[t]+x
#       ny = dy[t]+y
#       if nx>=0 and ny >=0 and nx<m and ny<n and graph[nx][ny]==1:
#         graph[nx][ny]=2
#         q.append((nx,ny))

def dfs(i,j):
  graph[i][j]=2
  for t in range(8):
    nx = dx[t]+i
    ny = dy[t]+j
    if nx>=0 and ny>=0 and nx<m and ny<n and graph[nx][ny]==1:
      dfs(nx,ny)

while(True):
  n, m = map(int, input().split())
  if n==0 and m==0:
    break
  graph = []

  for i in range(m):
    line = list(map(int, input().split()))
    graph.append(line)

  cnt = 0
  for i in range(m):
    for j in range(n):
      if graph[i][j]==1:
        dfs(i,j)
        cnt +=1
  print("cnt:",cnt)


