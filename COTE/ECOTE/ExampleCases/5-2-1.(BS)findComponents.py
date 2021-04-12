n = int(input())
a = list(map(int, input().split()))

k = int(input())
b = list(map(int, input().split()))


def find(arr, target, start, end):
    if end < 0:
        return False
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            end = mid-1
        elif arr[mid] < target:
            start = mid+1
    return False


for i in b:
    if find(a, i, 0, len(a)-1) is True:
        print('yes')
    else:
        print('no')


