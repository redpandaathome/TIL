# 어려웠다... 간단한 개념인거같은데
# 다시 풀어보기 🌺[ ]
# https://www.acmicpc.net/problem/14500
# 테트로미노
# 핵심 ✨[[0,0],[0,1],[0,2],[0,3]] 에 0,0 을 각각 더해주면 0,0 위치에서 가로스틱
# 위에서 1,1 좌표를 더해주면 1,1위치에서 가로스틱...!

# from collections import deque
# import sys
# input = sys.stdin.readline()
from sys import stdin

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

tetrominos =[[[0,0],[0,1],[0,2],[0,3]],
    [[0,0],[1,0],[2,0],[3,0]],
    #squre
    [[0,0],[0,1],[1,0],[1,1]],
    #L
    [[0,0],[1,0],[2,0],[2,1]],
    [[1,0],[1,1],[1,2],[0,2]],
    [[0,0],[0,1],[1,1],[2,1]],
    [[0,0],[0,1],[0,2],[1,0]],
    #
    [[2,0],[0,1],[1,1],[2,1]],
    [[0,0],[1,0],[1,1],[1,2]],
    [[0,1],[0,0],[1,0],[2,0]],
    [[0,0],[0,1],[0,2],[1,2]],
    #lightening
    [[0,0],[1,0],[1,1],[2,1]],
    [[0,1],[1,0],[1,1],[0,2]],
    [[1,0],[2,0],[0,1],[1,1]],
    [[0,0],[0,1],[1,1],[1,2]],
    #ㅗ
    [[0,0],[0,1],[0,2],[1,1]],
    [[0,1],[1,0],[1,1],[1,2]],
    [[1,0],[0,1],[1,1],[2,1]],
    [[0,0],[1,0],[1,1],[2,0]]
]



def cal_sum(r, c, t):
    print('CAL_SUM', r, c, t)
    temp_sum = 0
    global n, m
    #0,0, t = [[0,0],[0,1],[0,2],[0,3]]
    for i in range(len(t)):
        dx, dy = t[i]
        nx = r + dx
        ny = c + dy
        if 0 <= nx < n and 0 <= ny < m:
            print('graph[',nx,'][', ny,']:',graph[nx][ny])
            temp_sum += graph[nx][ny]
        else:
            return -1
        print('...temp_sum:',temp_sum)
    return temp_sum


ans = 0
max_sum = 0
for i in range(n):
    for j in range(m):
        for tetromino in tetrominos:
            #[[0,0],[0,1],[0,2],[0,3]]
            max_sum = max(max_sum, cal_sum(i, j, tetromino))
            print(max_sum)
print(max_sum)

# # l = [[1,1],[2],[3],[4]]
# # t = [([11,11],[22],[33],[44])]
# # for i in l:
# #     print(i)
# # for i in t:
# #     print(i)

# # [1, 1]
# # [2]
# # [3]
# # [4]
# # ([11, 11], [22], [33], [44])

# list1 = ([1,1],[2,2])
# list2 = [[1,1],[2,2]]
# for a, b in list1:
#     print(a, b)
# for a, b in list2:
#     print(a, b)