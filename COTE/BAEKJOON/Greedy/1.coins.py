# https://www.acmicpc.net/problem/11047

import sys
# n, m, v = map(int, sys.stdin.readline().split())

n,k = map(int, sys.stdin.readline().split())

coins = []
for i in range (n):
  coins.append(int(input()))

while k!=0:
  count=0
#   ✨범위...! -1까지
  for i in range(n-1, -1, -1):
    if coins[i]>k:
      continue
    n=k//coins[i]
    count+=n
    # print('n:',n, ' ,count:', count, ' ,k:',k)
    k -= coins[i]*n
    # print('k: ',k)
    if k==0:
      break
  break
print(count)
    