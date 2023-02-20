#https://www.acmicpc.net/problem/1197

#2nd[✅] Mar 14 2022

import sys
input = sys.stdin.readline

v, e = map(int, input().split())

parent = [0]*(v+1)
edges = []

for i in range(1, v+1):
  parent[i]=i

def find_parent(x):
  if parent[x] != x:
    parent[x]= find_parent(parent[x])
  return parent[x]

def union_parent(a,b):
  a = find_parent(a)
  b = find_parent(b)
  if a<b:
    parent[b]=a
  else:
    parent[a]=b


for i in range(e):
  a, b, c = map(int, input().split())
  edges.append((c, a, b))

edges.sort()

result = 0

for edge in edges:
  cost, a, b = edge
  if find_parent(a) != find_parent(b):
    union_parent(a,b)
    result+=cost

print(result)