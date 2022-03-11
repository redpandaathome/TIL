import sys
input = sys.stdin.readline

dx = [-1,-1,-1,1,1,1,0,0]
dy = [-1,0,1,-1,0,1,1,-1]

def dfs(i,j):
    graph[i][j]=2
    for k in range(len(dx)):
      nx = dx[k]+i
      ny = dy[k]+j
      if nx>=0 and nx<h and ny>=0 and ny<w and graph[nx][ny]==1:
        dfs(nx,ny)
    
  
while(True):
  w,h = map(int, input().split())
  print("* * * * * W&H", w, h)
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
        dfs(i,j)
        count+=1

  print("COUNT=",count)