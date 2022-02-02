# https://www.acmicpc.net/problem/4963
# 꼭 다 ㅅ ㅣ.... 🐛
# 2nd time 02.Feb.2022 ✅
# 

# x, y? y, x? 🚨
# 3 2
# 1 1 1
# 1 1 1
# m, n -> m - y, n - x,
# ... dx<n, dy<m

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

def dfs(x,y):
  if x<0 or y<0 or x>=m or y>=n:
    return False
  # print(x, y)
  visited[x][y]=True
  if graph[x][y]==1:
    # print('beforeG:',graph, ' (x,y):',x,y)
    graph[x][y]=0
    # print('changedG:',graph)
    for i in range(8):
      # print('i:', i)
      nx = dx[i]+x
      ny = dy[i]+y
      dfs(nx, ny)
    return True
  return False
    

while True:
  n, m = map(int, sys.stdin.readline().split())
  if n==0 and m==0:
    break
  graph = []
  for i in range (m):
    graph.append(list(map(int, sys.stdin.readline().split())))
  # print('graph:', graph)
  count = 0
  # ✨ x&y, n&m 🤷🏻‍♀️ 
  # https://www.notion.so/redpandathome/TIL-Python-cote-b52090c21f154868b9f76e60a8aed36e
  visited=[[False]*n for j in range (m)]
  # print('visited:',visited)
  for i in range(m):
    for j in range(n):
      # print('i,j:', i, j)
      # ✨
      if visited[i][j]==False:  
        if dfs(i, j)== True:
          # print('true..?', i, j)
          count+=1
  print(count)

