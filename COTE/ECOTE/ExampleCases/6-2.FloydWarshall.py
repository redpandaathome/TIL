# Essential! : k-lo       op (aDb = min(aDb, aDk+kDb) )

INF = int(1e9)

n=int(input())
m=int(input())
graph = [[INF] * (n+1) for i in range (n+1)]

for a in range (1, n+1):
    for b in range (1, n+1):
        if a==b:
            graph[a][b]=0

            
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    
for k in range(n+1):
    for a in range(n+1):
        for b in range(n+1):
            graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])

#print!
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b]==INF:
            print('INF', end=' ')
        else:
            print(graph[a][b], end=' ')
    print()

#input
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2

#output
0 4 8 6 
3 0 7 9 
5 9 0 4 
7 11 2 0 