# someone else's

import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n=int(input())
    rank=[0]*(n+1)
    last=[0]*(n+1)
    lst=list(map(int,input().split()))
    for i,x in enumerate(lst): rank[x]=i+1;last[x]=i+1
   #  print("rank:", rank)
   #  print("last:", last)
    m=int(input())
    for __ in range(m):
      a,b=map(int,input().split())
      if last[a]>last[b]: rank[a]-=1;rank[b]+=1
      else: rank[a]+=1;rank[b]-=1
      # print(">>>new rank:", rank)
    result=[0]*(n+1)
    ok=True
    for i in range(1,n+1):
        if result[rank[i]]==0:result[rank[i]]=i
        else:ok=False;break
    if ok: print(*result[1:])
    else: print("IMPOSSIBLE")