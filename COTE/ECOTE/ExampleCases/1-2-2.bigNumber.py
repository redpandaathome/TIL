n, m, k = map(int,input().split())
arr = list(map(int,input().split()))

# 5 8 3
# 2 4 5 4 6
ansArr=[]
arr.sort(reverse=True)
first = arr[0]
second = arr[1]

count = (int(m/(k+1))*k + m%(k+1))
result = 0
result+= count*first
result+= (m-count)*second
print(result)