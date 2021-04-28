board = [[1,1,0,0,0,1],
         [0,0,0,0,0,1],
         [0,0,1,1,0,1],
         [1,0,1,1,0,1],
         [1,0,0,0,0,0],
         [1,1,0,0,0,0]
        ]
blocks = [[1,1,0,0,0,0],
          [1,1,0,0,0,0],
          [0,0,0,1,1,0],
          [0,0,0,0,1,1],
          [0,0,1,0,0,0],
          [1,1,1,0,0,0],
         ]
# dfs... blocks에서 데리고 와야하는 값 [[(0,0),(0,1),(1,0),(1,1)],...]

n = len(board)

def dfs(x,y, tempList):
    print('dfs x,y...', x,y, ', tempList:', tempList)
    boardVisited[x][y]=True
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        if board[nx][ny] == 1 and boardVisited[nx][ny] == False:
            print('calling dfs nx,ny...',nx,ny)
            tempList.append([nx,ny])
            dfs(nx,ny, tempList)
    return tempList


boardList = []
blockList = []
boardVisited = [[False] * n for i in range(n)]
blockVisited = [[False] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if boardVisited[i][j] == False and board[i][j] ==1:
            tempList = [[i,j]]
            boardList.append(dfs(i,j, tempList))
        if blockVisited[i][j] == False and blocks[i][j] ==1:
            tempList = [[i,j]]
            blockList.append(dfs(i,j, tempList))

print(boardList)
#[[[0, 0], [0, 1]], [[0, 5], [1, 5], [2, 5], [3, 5]], [[2, 2], [3, 2], [3, 3], [2, 3]], [[3, 0], [4, 0], [5, 0], [5, 1]]]

print(blockList)
# [[[0, 0]], [[0, 1]], [[1, 0]], [[1, 1]], [[2, 3]], [[2, 4]], [[3, 4]], [[3, 5]], [[4, 2]], [[5, 0]], [[5, 1]], [[5, 2]]]

#block 회전값 포함하여 초기화가 필요하다.
for i in range(len(blockList)):
    for j

