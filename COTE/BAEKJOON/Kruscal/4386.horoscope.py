#https://www.acmicpc.net/status?user_id=dbal0&problem_id=4386&from_mine=1

import sys
import math

input = sys.stdin.readline

n = int(input())
graph = []
# location = []

for i in range (n):
  x, y = map(float, input().split())
  graph.append((x,y))

# print(graph.popleft())
result = 0;

parent = [0]*(n+1)
for i in range(1,n+1):
  parent[i] = i

def find_parent(x):
  if parent[x] != x:
    parent[x]=find_parent(parent[x])
  return parent[x]

def union_parent(a,b):
  a = find_parent(a)
  b = find_parent(b)
  if a < b:
    parent[b]=a
  else:
    parent[a]=b

def calcDistance(a, b):
  return math.sqrt(math.pow(a,2)+math.pow(b,2))

newGraph = []

# ✨✨✨
for i in range(n):
  now = graph[i]
  for j in range(i+1,n):
    a, b = now
    a2,b2 = graph[j]
    cost = calcDistance(a-a2, b-b2)
    if i!=j:
      # print("i&j:", i, j, ", cost:", cost)
      newGraph.append((cost, i, j))

newGraph.sort()
for unit in newGraph:
  cost, d1, d2 = unit
  if find_parent(d1) != find_parent(d2):
    union_parent(d1,d2)
    result+=cost

print(round(result,2))