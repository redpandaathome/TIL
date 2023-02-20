# https://www.acmicpc.net/problem/3665

import sys
from collections import deque

input = sys.stdin.readline
t = int(input())

for i in range (t):
  n= int(input())
  arr = list(map(int, input().split()))
  indegree = [0] * (n+1)
  graph = [[]for i in range(n+1)]

  for i in range(n):
    now = arr[i]
    for j in range(0, i):
      graph[now].append(arr[j])
  
  swapNum = int(input())

  for i in range (1, len(graph)):
    indegree[i]=len(graph[i])

  for i in range(swapNum):
    a, b = map(int, input().split())

    # ✨
    if a in graph[b]:
      graph[b].remove(a)
      indegree[b]-=1
      graph[a].append(b)
      indegree[a]+=1
      
    else:
      graph[a].remove(b)
      indegree[a]-=1
      graph[b].append(a)
      indegree[b]+=1

  result = []
  def topology_sort():
    q = deque()
    for i in range(1,n+1):
      if indegree[i]==0:
        q.append(i)
    while q:
      now = q.popleft()
      result.append(now)
      for i in range(1,len(graph)):
        if now in graph[i]:
          indegree[i]-=1
          graph[i].remove(now)
          if indegree[i]==0:
            q.append(i)  

  topology_sort()
  strResult = ''
  if len(result)==n:
    strResult = ' '.join([str(x) for x in result])
  else:
    strResult = 'IMPOSSIBLE'
  print(strResult)
