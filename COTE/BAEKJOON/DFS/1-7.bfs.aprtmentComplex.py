# https://www.acmicpc.net/problem/2667
# 단지번호붙이기

# 난점 인풋받아오기
# 카운트 세기 - global
# 출력시 오름차순 정렬 놓치지 말기

#  import sys
# input = sys.stdin.readline().rstrip()

n = int(input())

graph = []
for i in range(n):
   #🌺
    graph.append(list(map(int,input())))

#상,하,좌,우
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def dfs(x, y):
    # print('dfs...', x, y)
    #🌺
    global count
    count += 1
    graph[x][y] = 2
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 > nx or nx >= n or 0 > ny or ny >= n:
            continue
        if graph[nx][ny] == 1:
            dfs(nx, ny)
    return count


ans = []
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            count = 0
            ans.append(dfs(i, j))
#🌺
ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])
