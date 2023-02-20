n, m, start = map(int, input().split())

# [[],[2,3,4],[1,4],[1,4],[1,2,3]]
graph = [[]for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

#✨ sort needed...
for i in range(len(graph)):
  graph[i].sort()

visited = [False for i in range(n+1)]

dfs_ans = []
def dfs(graph, start, visited):
    visited[start] = True
    dfs_ans.append(start)
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)
dfs(graph,start,visited)
for i in dfs_ans:
  print(i, end=' ')
print()

bfs_ans = []
from collections import deque
visited2 = [False for i in range(n+1)]
def bfs(graph, v, visited):
    if visited[v]:
      return
    q = deque([v])
    visited[v] = True
    while q:
      node = q.popleft()
      bfs_ans.append(node)
      for i in graph[node]:
        if not visited[i]:
          q.append(i)
          visited[i]=True
bfs(graph, start, visited2)
for i in bfs_ans:
  print(i, end= ' ')