# https://www.acmicpc.net/problem/1707
# 이분그래프

from collections import deque
# import sys
# input = sys.stdin.readline()


n = int(input())

while n:
    n-=1
    v, e = map(int, input().split())
    nodes = [[] for i in range(v+1)]
    visited = [False] * (v+1)
    colored = [0] * (v+1)
    isTrue = True
    for i in range(e):
        a, b = map(int, input().split())
        nodes[a].append(b)
        nodes[b].append(a)
     

    def bfs(v):
        print('bfs...v:', v)
        global isTrue
        q = deque()
        q.append(v)
        colored[v]=1
        visited[v]=True
        while q and isTrue:
            v = q.popleft()
            #🌺
            visited[v]=True
            color = colored[v]
            print('#####nodes[',v,']:', nodes[v], ' colored[',v,']:', colored[v])
            for i in nodes[v]:
                if visited[i]:
                    print('??? visited[',i,']=', visited[i])
                    continue
                # 💩 visited[i] = True
                if colored[i] == color:
                    isTrue = False
                    print("f....a...l..s..e!")
                    break
                else:
                    print('else...colored[',i,']:', colored[i], '<->color:',color)
                    colored[i] = -color;
                    print(colored[i])
                    q.append(i)
    
    for i in range(1, v+1):
        if not isTrue:
            break
        else:
            bfs(i)
    
    if isTrue:
        print("YES")
    else:
        print("NO")
    

