# 🌺🌺🌺🌺🌺

import sys
from collections import deque
import copy
input = sys.stdin.readline

n = int(input())
graph = [[] for i in range(n+1)]
indegree = [0] * (n+1)
time = [0] * (n+1)

for i in range(1,n+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for j in data[1:-1]:
        indegree[i] += 1
        # ✨✨✨✨✨
        graph[j].append(i)

print(time)
print(graph)

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()
    for i in range(1, n+1):
        if indegree[i]==0:
            q.append(i)
    while q:
        now = q.popleft()
        for i in graph[now]:
           # 🌺
            result[i] = max(result[i], result[now]+time[i])
            indegree[i] -= 1
            if indegree[i]== 0:
                q.append(i)
    # ✨✨✨
    for i in range(1, n+1):
        print(result[i])
topology_sort()
    



#input
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1

#output
10
20
14
18
17