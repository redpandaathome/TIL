import sys
input = sys.stdin.readline

def find_parent(x):
  if parent[x]!=x:
    parent[x]=find_parent(parent[x])
  return parent[x]

def union_parent(a,b):
  a = find_parent(a)
  b = find_parent(b)
  if a<b:
    parent[b] = a
  else:
    parent[a] = b

t = int(input())
for i in range(t):
  n, m = map(int, input().split())
  # print("n,m: ",n, m)

  count = 0
  parent = [0]*(n+1)
  for i in range(1, n+1):
    parent[i] = i

  for i in range(1,m+1):
      a, b = map(int, input().split())
      if find_parent(a)!=find_parent(b):
        union_parent(a,b)
        count+=1
  print(count)
        
