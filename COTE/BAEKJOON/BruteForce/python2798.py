#✨ 조합사용하기
#https://www.acmicpc.net/problem/2798

from itertools import combinations

n, m = map(int,input().split())
arr = list(map(int, input().split()))

ans = 0
for i in range(n):
  combi = list(combinations(arr,3))
for i in combi:
  temp = sum(i)
  if m-temp < m-ans and m>=temp:
    ans=temp

print(ans)