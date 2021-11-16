n,m = map(int,input().split())
coins = []
d= [10001]*(m+1)
for i in range(n):
  temp = int(input())
  coins.append(temp)

for i in coins:
  if i<=m:
    d[i]=1

# print(coins)
# print(d)
coins.sort()

for i in range(coins[0],m+1):
  print("i...", i)
  temp = d[i]
  for c in coins:
    print("coin:", c)
    print(i-c, d[i-c])
    if d[i-c]>0:
      print("-temp:", temp)
      print("d[i-c]+1", d[i-c]+1)
      temp = min(temp, d[i-c]+1)
      d[i]=temp
print("d...", d)

if d[m]==10001:
  print(-1)
else:
  print(d[m])