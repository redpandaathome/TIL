n, m = map(int,input().split())
graph = []
for i in range(n):
  graph.append(list(map(int,input())))
print(graph)

    #좌우상하
dx = [0,0,-1,1]
dy = [-1,1,0,0]

count=0
def dfs(graph, i, j):
  graph[i][j] = 2
  x, y = i, j
  
  for w in range(4):
    nx = x+dx[w]
    ny = y+dy[w]
    if nx<0 or ny<0 or nx>=n or ny>=m:
      continue
    elif graph[nx][ny]==0:
      graph[nx][ny]=2
      dfs(graph, nx,ny)


for i in range(n):
  for j in range(m):
    if graph[i][j]==0:
      dfs(graph, i, j)
      print(graph)
      count+=1
print(count)


#input
4 5
00110
00011
11111
00000

#output
3