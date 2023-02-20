# [ ] 🌺

import sys
# # n, m, v = map(int, sys.stdin.readline().split())

t = int(input())
for tc in range(t):
    n, m = map(int, sys.stdin.readline().split())

    # graph = [[[] for i in range(n+1)] for j in range(m+1)]

    #✨✨✨input 받기... 한줄로 들어오는걸 array index로 끊어서 받기!
    array = list(map(int, sys.stdin.readline().split()))
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m])
        index+=m
    # print(dp)
    # [[1, 3, 3, 2], [2, 1, 4, 1], [0, 6, 4, 7]]

    for j in range(1,m):
        for i in range(n):
            #왼쪽위에서 오는 경우
            if i ==0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            #왼쪽아래에서
            if i==(n-1):
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            #left...
            left=dp[i][j-1]

            dp[i][j] = dp[i][j]+max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)