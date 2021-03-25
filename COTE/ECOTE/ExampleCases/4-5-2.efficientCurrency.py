#✨ brilliant.......... 다음에 다시 시도해볼 것!
# dynamic ps 굉장히 약하구나...

n, m = map(int,input().split())
coins=[]
for i in range(n):
  if i<=n:
    coins.append(int(input()))
d =[10001] * (m+1)
d[0]= 0
for i in range(n):
  print("i:",i,"==========")
  for j in range(coins[i], m+i):
    print("j: ", j)
    print("j-coins[i]: ", j-coins[i])
    if d[j - coins[i]] != 10001:
      d[j]=min(d[j], d[j-coins[i]]+1)
  print("d...", d)

if d[m] == 10001:
  print(-1)
else:
  print(d[m])