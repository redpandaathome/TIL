#✨✨✨✨✨
# if amount >= coin then
# comb[amount] += comb[amount-coin]

n = int(input())

arr = [3,5]
ans=[987654321]*(n+1)
ans[3]=1
if n>=5:
  ans[5]=1
for i in range(2):
  for j in range(3,n+1):
    if j>=arr[i]:
      # print(j, arr[i])
      ans[j]=min(ans[j], ans[j-arr[i]]+1)
      # print('ans[',j,']: ',ans[j])
  # print(ans)
  # print('----------------')
if ans[n]==987654321:
  print(-1)
else:
  print(ans[n])