graph = [
   [],
   [2,3,8],
   [1,7],
   [1,4,5],
   [3,5],
   [3,4],
   [7],
   [2,6,8],
   [1,7]
]

from collections import deque

visited = [False]*len(graph)
ans = []
def bfs(graph, start, visited):
  q = deque([start])
  visited[start] = True
  ans.append(start)
  #✨
  while q:
    v = q.popleft()
    for i in graph[v]:
      #✨
      if not visited[i]:
        q.append(i)
        ans.append(i)
        visited[i]=True
bfs(graph,1,visited)
print(ans)

#bfs - while q...