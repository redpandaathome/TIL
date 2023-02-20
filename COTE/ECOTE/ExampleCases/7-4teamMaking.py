import sys
# from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i


def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_find(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(m):
    o, a, b = map(int, input().split())
    if o == 0:
        union_find(parent, a, b)
    else:
        if find_parent(parent, a) != find_parent(parent, b):
            print('NO')
        else:
            print('YES')



7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1

#output
NO
NO
YES