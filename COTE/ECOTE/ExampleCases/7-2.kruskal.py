import sys
input = sys.stdin.readline
v, e = map(int, input().split())

parent = [0]*(v+1)

for i in range(1, v+1):
    parent[i] = i


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_find(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

# ✨🌺
edges = []
result = 0
for i in range(1, e+1):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()

# ✨🌺
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_find(parent, a, b)
        result += cost
print(result)

print(parent)


7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25