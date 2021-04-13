import heapq
INF = int(1e9)
#✨
import sys
input = sys.stdin.readline

n, m, c = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)
print('graph:', graph)
print(distance)
for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append([z, y])

print('updatedGraph:', graph)
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    # ✨
    distance[start]=0
    while q:
        dist, v = heapq.heappop(q)
        print('v:', v, ', dist:', dist)
        if distance[v] < dist:
            continue
        # ✨distance[v] = dist
        for i in graph[v]:
            print('i:', i)
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))

                    
dijkstra(c)
print(distance)
maxD=0
count=0
for d in distance:
    if d != INF:
        count+=1
        maxD = max(maxD, d)
print(count-1, maxD)

3 2 1
1 2 4
1 3 2