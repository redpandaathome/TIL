# https://www.acmicpc.net/problem/2644
# QUESTION - how to keep counts???

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
start, target = map(int, input().split())
m = int(input())
graph = [[]for i in range(n+1)]
for i in range(m):
  x, y = map(int, input().split())
  graph[y].append(x)
  graph[x].append(y)

visited = [False] * (n+1)
# print(graph)
dist = [-1]*(n+1)
def bfs(start, count):
  q = deque()
  q.append((start,count))
  while q:
    # print("q:", q)
    now, nowCnt = q.popleft()
    # print("now:", now, "nowCnt", nowCnt)
    visited[now]=True
    if target == now:
      return count
    for i in graph[now]:
      if not visited[i]:
        q.append((i, nowCnt+1))
        dist[i]=nowCnt+1
        
bfs(start, 0)
print(dist[target])