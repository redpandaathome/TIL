# 🌺 LIS: Longest Increasing Subsequence 🌺
#input
6
10 20 10 30 20 50
#output
# 1 2 1 3 2 4

# 🔥 dp[i] = max(dp[i], dp[j]+1) if arr[j] < arr[i] ... ✨when 0<=j<i

n = int(input())
arr = list(map(int, input().split()))

dp = [1 for i in range(n)]

for i in range(1, n):
    for j in range(0, i):
        if arr[i]>arr[j]:
            dp[i] = max(dp[j]+1, dp[i])
    print(dp)
print('=============')
print(dp)