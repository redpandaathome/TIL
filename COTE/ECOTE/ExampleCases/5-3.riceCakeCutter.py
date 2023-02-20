# input
4 6
19 15 10 17

#output
15

n, t = map(int, input().split())
arr = list(map(int, input().split()))


def find(arr, t, start, end):
  if start > end:
    return None
  mid = (start+end)//2
  sum = 0
  for i in arr:
    cut = i-mid
    if cut >= 0:
      sum += cut
  
  if sum == t:
    return mid
  elif sum < t:
    end = mid - 1
    # 🐝 재귀로 풀거면 return 잊지...ㅁ..ㅏ..
    return find(arr, t, start, end)
  elif sum > t:
    start = mid + 1
    # 🐝 재귀로 풀거면 return 잊지...ㅁ..ㅏ..
    return find(arr, t, start, end)


print(find(arr, t, 0, max(arr)-1))