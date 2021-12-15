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

### how to deal with count? as 🌏 global? or parameter
### parameter > can't get returned value like below
# def dfs(v, count):
#   visited[v]=True
#   print("dfs>>>v:",v, ", count:", count)
#   for i in graph[v]:
#     if not visited[i]:
#       count+=1
#       dfs(i, count)

# count = 0
# dfs(1, count)
# print(count) #0



# 👀 if you want to use parameters instead of global variables...
# you can use countMax variable like below...

# def dfs(v, count):
#   global countMax
#   visited[v]=True
#   count+=1
#   countMax = max(count, countMax)
#   print("dfs>>>v:",v, ", count:", count)
#   for i in graph[v]:
#     if not visited[i]:
#       dfs(i, count)

# count = 0
# countMax = count
# dfs(1, count)
# print(countMax) #4