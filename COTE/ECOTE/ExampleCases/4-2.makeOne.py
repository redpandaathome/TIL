#input
26

#output
3

#5로 나눠지면 5로 나눈다/ 3~/ 2~/x-1

n = int(input())

result=0
while n!=1:
  if n%5==0:
    n=n/5
  elif n%3==0:
    n=n/3
  elif n%2==0:
    n=n/2
  else:
    n-=1
  result+=1
print(result)


#input:26
#output:5

#책에서 한 접근은...
n = int(input())

d=[0]*30001
for i in range(2, n+1):
  d[i]=d[i-1]+1
  if i%2==0:
    d[i]=min(d[i], d[i//2]+1)
  if i%3==0:
    d[i]=min(d[i], d[i//3]+1)
  if i%5==0:
    d[i]=min(d[i], d[i//5]+1)
print(d[n])
