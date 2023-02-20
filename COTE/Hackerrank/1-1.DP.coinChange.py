#https://www.hackerrank.com/challenges/coin-change/problem

n =4
c = [1,2,3]

def getWays(n, c):
  # Write your code here
  ans = [0]*(n+1)
  ans[0] = 1
  #✨✨✨✨✨
  for i in range(len(c)):
    for j in range(n+1):  
      if j>=c[i]:
        ans[j]+=ans[j-c[i]]
  return ans[n]
  #✨✨✨✨✨
   
result = getWays(n,c)
print(result)