import sys

input = sys.stdin.readline
n, m = map(int, input().split())

parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i


def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_find(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


result = 0
last = 0
edges = []
for i in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 🌺
edges.sort()
print('sorted-----', edges)
# graph.popleft()
for edge in edges:
    cost, a, b = edge
    print("cost, a, b:", cost, a, b)
   # 🌺
    if find_parent(a) != find_parent(b):
        print('connecting...', cost, a, b)
        union_find(a, b)
        result += cost
        last = cost

print(parent)
print(result)
print(result-last)



7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4