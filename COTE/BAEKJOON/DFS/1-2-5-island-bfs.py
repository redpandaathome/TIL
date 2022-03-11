import sys
input = sys.stdin.readline
from collections import deque

nx = [-1,-1,-1,1,1,1,0,0]
ny = [-1,0,1,-1,0,1,1,-1]

def bfs(i,j):
  q=deque()
  q.append([i,j])
  graph[i][j]=2
  while q:
    x,y = q.popleft()
    graph[x][y]=2
    for k in range(len(nx)):
      dx = nx[k]+x
      dy = ny[k]+y
      if dx<0 or dx>=h or dy<0 or dy>=w:
        continue
      if graph[dx][dy]==1:
        q.append([dx,dy])
    
while(True):
  # 💖 w, h - helpful!
  w,h = map(int, input().split())
  if w==0 and h==0:
    break
  graph = []
  for i in range(h):
    temp = list(map(int, input().split()))
    graph.append(temp)

  count=0  
  for i in range(h):
    for j in range(w):
      if graph[i][j]==1:
        bfs(i,j)
        count+=1

  print(count)