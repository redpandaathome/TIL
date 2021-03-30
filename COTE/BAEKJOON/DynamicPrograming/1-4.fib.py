#https://www.acmicpc.net/problem/1003

n = int(input())

arr=[[1,0],[0,1]]
def sol(m):
  currentMax = len(arr)
  for i in range(currentMax,m+1):
    # print('for...', currentMax, m)
    arr.append([arr[i-1][0]+arr[i-2][0],arr[i-1][1]+arr[i-2][1]])
  # print("updated...",arr)

for i in range(n):
  k= int(input())
  if len(arr)<=k:
    sol(k)
  print(arr[k][0], arr[k][1])