import sys

input = sys.stdin.readline

n = int(input())
# https://www.acmicpc.net/problem/2644
# simple question but it was tricky -> need a lot more practice in dfs
# difficult points - count coherency in dfs
# return in dfs??? ->print? what if there is no value, how to print -1?

start, target = map(int, input().split())
m = int(input())
graph = [[]for i in range(n+1)]
for i in range(m):
  x, y = map(int, input().split())
  graph[y].append(x)
  graph[x].append(y)

visited = [False] * (n+1)
# print(graph)

result = []
def dfs(start, count):
  # print("DFS v:",start, ", count:", count)
  visited[start]=True
  if start == target:
    print(count)
    sys.exit()
  for i in graph[start]:
    if not visited[i]:
      dfs(i, count+1)

dfs(start, 0)
print(-1)