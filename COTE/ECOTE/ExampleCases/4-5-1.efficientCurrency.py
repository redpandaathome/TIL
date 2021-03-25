n, m = map(int,input().split())
coins=[]
for i in range(n):
  if i<=n:
    coins.append(int(input()))
coins.sort(reverse=True)
result =0

for i in coins:
  print('m//i',m, i, "=",m//i)
  if m%i==0:
    result+=m//i
    m = m-result * i

if m!=0 and result==0:
  print(-1)
else:
  print(result)

#input =>5
2 15
2
3

#input =>-1
3 4
3
5
7