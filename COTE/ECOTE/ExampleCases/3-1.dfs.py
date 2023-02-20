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

#✨
visited = [False]*len(graph)
ans = []
def dfs(graph, start, visited):
  visited[start] = True
  ans.append(start)
  for i in graph[start]:
    if not visited[i]:
      dfs(graph, i, visited)
dfs(graph, 1, visited)
print(ans)

#dfs - recursive dfs...