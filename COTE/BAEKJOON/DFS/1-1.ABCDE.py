# https://www.acmicpc.net/problem/13023
# 다시해봐야 🌺 
# [31.Mar.21✅]
# [11.Jan.22✅]
# []
import sys
n, m = map(int, sys.stdin.readline().split())

graph = [[] for i in range(n+1)]
visited = [ False for i in range(n+1)]


for i in range(m):
  a, b = map(int, sys.stdin.readline().split())
  graph[a+1].append(b+1)
  graph[b+1].append(a+1)

def dfs(graph, i, myDepth):
  global ans
  visited[i]=True;

  if myDepth>=4:
    ans=True
    return  

  for j in graph[i]:
    if not visited[j]:
      #✨ depth tracking...
      dfs(graph, j, (myDepth+1))
      #✨ visit reset
      visited[j] = False

ans = False
for i in range(1, n+1, 1):
  ### NOOOO : ans = dfs(graph, i, 0), take ans as global variable 🦁
  dfs(graph, i, 0)
  #✨ visit reset
  visited[i]=False
  if ans:
    break

print(1 if ans else 0)