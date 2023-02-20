#플로이드워셜 ㄱㄱ

INF = int(1e9)

n, m = map(int, input().split())
graph = [ [INF] * (n+1) for i in range(n+1)]
for a in range(1, m+1):
    a, b = map(int, input().split())
    # ✨양방향이란것!
    graph[a][b]=1
    graph[b][a]=1
    
for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b]=0
x, k = map(int, input().split())

for i in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b]=min(graph[a][b], graph[a][i]+graph[i][b])

distance = graph[1][k]+graph[k][x]
if distance >= INF:
    print(-1)
else:
    print(distance)
#input
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

#output
3

[[1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000], 
[1000000000, 0, 1, 1, 1, 2], 
[1000000000, 1000000000, 0, 1000000000, 1, 2], 
[1000000000, 1000000000, 1000000000, 0, 1, 1], 
[1000000000, 1000000000, 1000000000, 1000000000, 0, 1], 
[1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 0]]

#input2
4 2
1 3
2 4
3 4

#output2
-1