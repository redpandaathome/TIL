#https://www.acmicpc.net/problem/9095

n = int(input())

def sol(m):
  if m==1:
    return 1
  elif m==2:
    return 2
  elif m==3:
    return 4
  elif m>=4:
    return sol(m-1)+sol(m-2)+sol(m-3)

for i in range(n):
  k= int(input())
  print(sol(k))
  