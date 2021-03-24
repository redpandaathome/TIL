n, m = map(int,input().split())
graph = []
for i in range(n):
  graph.append(list(map(int,input())))
print(graph)

#     #좌우상하
# dx = [0,0,-1,1]
# dy = [-1,1,0,0]

count=0
def dfs(x,y):
  if x<0 or y<0 or x>=n or y>=m:
    return False
  if graph[x][y] == 0:
    graph[x][y]=1
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    return True



for i in range(n):
  for j in range(m):
    if graph[i][j]==0:
      if dfs(i, j)==True:
        print(graph)
        count+=1
print(count)
