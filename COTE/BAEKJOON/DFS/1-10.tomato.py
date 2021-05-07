# https://www.acmicpc.net/problem/7576
# 토마토 🍅
# 쉬워보였는데 막상 어어어어엄청 헤맸다.

import sys
from collections import deque
input = sys.stdin.readline()

m, n = map(int, input.split())
# print(n, m)
arr = []
for i in range(n):
    temp = sys.stdin.readline().split()
    arr.append(list(map(int, temp)))
#print("arr", arr)

#또는 💜
# graph = [list(map(int, sys.stdin.readline().split())) for i in range (n)]


dx = [1,-1,0,0]
dy = [0,0,-1,1]


q = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i,j))


while q:
    x, y = q.popleft()
    for i in range(4):
        nx = dx[i]+x
        ny = dy[i]+y
        # if nx>=n or 0>nx or ny>=m or 0>ny:
            # continue
        if 0<=nx<n and 0<=ny<m and arr[nx][ny] == 0:
            arr[nx][ny] = arr[x][y]+1
            q.append((nx,ny))


#전부 0 -> -1, 전부 1이면? 0, 전부 -1이면? -1
unRipe = False
for i in arr:
    if 0 in i:
        unRipe = True
        break
        
#print("arr:", arr)

if unRipe:
    print(-1)
else:
    maxDay = 0
    #✨MaxDay카운팅에서 꾀쓴게 문제였다...(털썩) 근데 냉장고가 텅비었을때 리턴이 0인건...? 없어도되네 이조건은
    for i in range(n):
        for j in range(m):
            maxDay = max(maxDay, arr[i][j])
    if maxDay == -1:
        print(0)
    else:
        print(maxDay-1)

