# https://www.acmicpc.net/problem/15989
# 1,2,3 더하기 4

# import sys
# input = sys.stdin.readline().rstrip()

n = int(input())
#🌺.
d = [[0,0,0,0] for i in range(10001)]
d[1][1] = 1

d[2][1] = 1
d[2][2] = 1

d[3][1] = 1
d[3][2] = 1
d[3][3] = 1


def solve(m):
#🌺.
    if m>3:
        for i in range(4, m+1):
            d[i][1] = d[i-1][1]
            d[i][2] = d[i-2][1] + d[i-2][2]
            d[i][3] = d[i-3][1] + d[i-3][2] + d[i-3][3]
    return d[m][1]+d[m][2]+d[m][3]


for i in range(n):
    m = int(input())
    print(solve(m))


#🌺 또는
# while n:
#    n-=1
#    print(sum(dp[int(input)]))