## 1. 🌺deque - 큐 자료구조시 사용 *** 🌺BFS
#append, popleft
#vscode 검색 ㄱㄱ
from collections import deque
q = deque([start])
while q:
   v = q.popleft()
   q.append(i)

#or
q.append((x,y))
x, y = q.popleft()


## 2. ✨heapq - 우선수위큐 자료구조시 사용 *** ✨Dijkstra
#heapq.heappush(q, (0,start)), heapq.heappop(q)
#vscode 검색 ㄱㄱ

import heapq
q= []
heapqq.heappush(q, (0,start))
while q:
   dist, now = heapq.heappop(q)