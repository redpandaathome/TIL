# https://www.acmicpc.net/problem/2251
# 물통🌺🌺🌺💦

import sys
from collections import deque

input = sys.stdin.readline

def pour(x,y):
    print('pour...x,y:', x, y)
    if not visited[x][y]:
        visited[x][y] = True
        q.append((x,y))

def bfs():
    q.append((0,0))
    visited[0][0] = True
    while q:
        x, y = q.popleft()
        z = c-x-y
        if x == 0:
            ans.append(z)
        # a->b
        water = min(x, b-y)
        pour(x-water ,y+water)
        # a->c
        water = min(x, c-z)
        pour(x-water ,y)
        # b->a
        water = min(y, a-x)
        pour(x+water ,y-water)
        # b->c
        water = min(y, c-z)
        pour(x ,y-water)
        # c->a
        water = min(z, a-x)
        pour(x+water ,y)
        # c->b
        water = min(z, b-y)
        pour(x ,y+water)

        
        
    
a, b, c = map(int, input().split())
q = deque()
ans = []
visited = [[False] * (b+1)  for i in range(a+1)]
print("visited:", visited)

bfs()
ans.sort()
print(ans)
print(' '.join(map(str, ans)))

    
