#https://www.acmicpc.net/problem/1463

#arr[8]= 3인데 4라고 생각해서 헤매였다.

n= int(input())
arr=[0,0,1,1]
for i in range(4,n+1):
  arr.append(arr[i-1]+1)
  if i%3==0:
    arr[i]=min(arr[i], arr[i//3]+1)
  if i%2==0:
    arr[i]=min(arr[i], arr[i//2]+1)
print(arr[n])