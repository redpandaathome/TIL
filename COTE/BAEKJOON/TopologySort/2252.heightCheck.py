#https://www.acmicpc.net/status?user_id=dbal0&problem_id=2252&from_mine=1

import sys
from collections import deque

input = sys.stdin.readline

v,e = map(int, input().split())
indegree = [0]*(v+1)
graph = [[]for i in range(v+1)]

for i in range(1,e+1):
  a, b = map(int, input().split())
  graph[a].append(b)
  indegree[b]+=1

result = []
def topology_sort():
  q = deque()
  for i in range(1,v+1):
    if indegree[i]==0:
      q.append(i)
  while q:
    now = q.popleft()

    result.append(now)
    for i in graph[now]:
      indegree[i]-=1
      if indegree[i]==0:
        q.append(i)

topology_sort()

#✨✨✨
print(' '.join(str(x)for x in result))