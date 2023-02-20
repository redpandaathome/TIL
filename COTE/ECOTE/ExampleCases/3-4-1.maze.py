n, m = map(int,input().split())
graph = []
for i in range(n):
  graph.append(list(map(int,input())))
print(graph)

from collections import deque
  #상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

ans = 0
def bfs(x,y):
  q = deque()
  q.append((x,y))
  while q:
    x,y = q.popleft()
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if nx>=0 and ny>=0 and nx<n and ny<m and graph[nx][ny]==1:
        q.append((nx,ny))
        graph[nx][ny]=graph[x][y]+1
        print(graph)
        print('=========')
  return graph[n-1][m-1]
  
print(bfs(0,0))

5 6
101010
111111
000001
111111
111111

3 3
110
010
011