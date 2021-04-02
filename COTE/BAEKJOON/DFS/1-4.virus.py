# https://www.acmicpc.net/problem/2606

import sys
# n, m, v = map(int, sys.stdin.readline().split())

n = int(input())
m = int(input())
#m개의 간선
graph = [[] for i in range(n+1)]
# print(graph)
for i in range (m):
  a, b = map(int, input().split())
  # a,b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)
visited = [False for i in range(n+1)]
# print(graph)

def dfs(v):
  global count
  visited[v]=True;
  for i in graph[v]:
    if not visited[i]:
      count+=1
      dfs(i)

count = 0
dfs(1)

print(count)