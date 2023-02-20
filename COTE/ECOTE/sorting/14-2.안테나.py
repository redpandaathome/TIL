#  acmicpc.net/problem/18310
# 2021.03.11

# !!! : median value (모든 점들로 부터 거리 합의 최소)
n= int(input())

arr =list(map(int, input().split()))
arr.sort()

print(arr[(n-1)//2])

#input
4
5 1 7 9

#output
5