import sys
from collections import deque

dx = [-1,1,0,0,-1,1,-1,1]
dy = [0,0,-1,1,1,-1,-1,1]

def bfs(tempGraph, i,j,count):
  q = deque()
  q.append((i,j))
  tempGraph[i][j]=2
  while q:
    # print("q??????????",q)
    x, y = q.popleft()
    # print("BF FOR>>>",x, y)
    for i in range(8):
      nx = x+dx[i]
      ny = y+dy[i]
      
      # 💜 m, n!!! alert
      if nx<0 or ny<0 or nx>=m or ny>=n:
        continue
      if tempGraph[nx][ny]!=1:
        continue

      tempGraph[nx][ny]=2
      q.append((nx,ny))
      # print("q.appending++++",nx,ny)
        

input = sys.stdin.readline
import copy

while(True):
  n,m = map(int, input().split())
  if n==0 and m==0:
    break
  graph = []
  for i in range(m):
    tempList = list(map(int, input().split()))
    graph.append(tempList)
  # print("GRAPH:", graph)
  count = 0

# 💜 m, n!!! alert
  for i in range(m):
    for j in range(n):
      if graph[i][j]==1:
        tempGraph = copy.copy(graph)
        bfs(tempGraph, i, j, count)
        count += 1
  print(count)