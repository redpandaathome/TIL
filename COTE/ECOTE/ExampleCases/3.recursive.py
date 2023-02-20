#팩토리얼 반복함수로
def fact(n):
  k = 1
  ans= 1
  while k<=n:
    ans*=k
    k+=1
  print(ans)

fact(4)
fact(1)
fact(2)

def fact2(n):
  ans=1
  for i in range(1,n+1):
    ans*=i
  print(ans)

fact2(4)
fact2(1)
fact2(2)

#재귀적으로 
def fact3(n):
  if n<2:
    return n
  return n*fact3(n-1)
print(fact3(4))
print(fact3(1))
print(fact3(2))


