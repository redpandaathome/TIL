n = int(input())
coins = [500,100,50,10]
sum=0
for i in coins:
  sum+=n//i
  # n-=(n//i)*i
  n%=i
print(sum)