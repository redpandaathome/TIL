# 직접구현하고싶다면?
#INPUT1 => output:-1 (4가없음)
7 4
1 1 2 2 2 2 3

#INPUT2 => output:4 (2는 4개)
7 2
1 1 2 2 2 2 3


def count_by_value(arr, target):
  a = first(arr, target, 0, n-1)
  
  if a==None:
    return 0
  b = last(arr, target, 0, n-1)

  return b-a+1

def first(arr, target, start, end):
  if start>end: #✨
    return None

  mid = (start+end)//2
  if (mid==0 or target>arr[mid-1]) and arr[mid] ==target:
    return mid
  elif arr[mid] >= target: #왼쪽으로 이동 ✨ mid값이 타겟과 "같거나" 크면 왼쪽으로 가야함
    return first(arr, target, start, mid-1)
  else:
    return first(arr, target, mid+1, end) #mid값이 목표보다 작다면 오른쪽으로

def last(arr, target, start, end):
  if start>end:
    return None
  mid = (start+end)//2
  if (mid==n-1 or target<arr[mid+1]) and arr[mid] == target:
    return mid
  elif arr[mid] > target: #왼쪽으로 이동 ✨ mid값이 목표보다 크다면 왼쪽으로 가야함
    return last(arr, target, start, mid-1)
  else: #오른쪽으로 ✨ mid값이 목표보다 작거나 "같으면" 오른쪽으로 이동
    return last(arr, target, mid+1, end)




#####
n, target = map(int, input().split())
arr = list(map(int, input().split()))

result = count_by_value(arr, target);
if result==0:
  print(-1)
else:
  print(result)