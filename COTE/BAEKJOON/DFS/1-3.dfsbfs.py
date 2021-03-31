# https://www.acmicpc.net/problem/1260
# 🤕

import sys
n, m, v = map(int, sys.stdin.readline().split())

graph = [[0]*(n+1) for i in range(n+1)]

for i in range(m):
  a,b = map(int, sys.stdin.readline().split())
  graph[a][b]=graph[b][a]=1
# print('graph:', graph)
visited = [False for i in range(n+1)]
dfsAns = []

def dfs(v):
  visited[v]=True
  dfsAns.append(v)
  # print(v)
  for i in range(1,n+1):
    if visited[i]==False and graph[v][i]==1:
      dfs(i)

from collections import deque

bfsVisited = [False for i in range(n+1)]


bfsAns=[]
def bfs(v):
  q = deque([v])
  bfsVisited[v] = True
  while q:
    v=q.popleft()
    # print('v: ',v)
    bfsAns.append(v)
    for i in range(1, n+1):
      if not bfsVisited[i] and graph[v][i]==1:
        q.append(i)
        bfsVisited[i]=True

dfs(v)
bfs(v)

for i in dfsAns:
  print(i, end=' ')
print()
for i in bfsAns:
  print(i, end=' ')