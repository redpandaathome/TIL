# Dynamic algorithm
# 큰 문제는 작게 나누고, 작은 문제라면 한번씩만 풀어 문제를 효율적으로 해결하는 알고리즘 기법

# def fib(n):
#   if n<=2:
#     return 1
#   return fib(n-1)+fib(n-2)

# print(fib(5))

#memoization✨
arr = [0]*100
def fib(n):
  if n<=2:
    return 1
  if arr[n] != 0:
    return arr[n]
  arr[n] = fib(n-1)+fib(n-2)
  print(arr)
  return arr[n]
print(fib(10))

#위와 같이 재귀함수를 이용한 다이나믹 프로그래밍 소스코드 작성은,
# 큰 문제해결위해 작은 문제 호출한다하여 topdown

#반면에 단순한 반복문을 이용해여 작은문제부터 차근 차근 도출하면 bottomup
arr = [0]*100
def fib(n):
  if n<=2:
    return 1
  arr[1]=1
  arr[2]=1
  for i in range(3,n+1):
    arr[i]=arr[i-1]+arr[i-2]
  return arr[n]
print(fib(10))

# 완탐으로 시간이 너무 오래 걸리면
# 부분문제들의 중복 여부를 확인해 보자.
# bottomup을 권장 - stack size...