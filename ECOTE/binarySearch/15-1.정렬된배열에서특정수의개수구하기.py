# 단순히 정렬된 배열에서 특정 뎅터를 찾을 경우 직접 이진탐색을 구현할 필요없ㅇ, 파이썬 bisect 모듈 사용

import bisect
n, target = map(int,input().split())
arr = list(map(int, input().split()))
# print(n,target, arr)
left = bisect.bisect_left(arr, target)
right = bisect.bisect_right(arr, target)

result = right-left
if result ==0:
  print(-1)
else:
  print(result)

  