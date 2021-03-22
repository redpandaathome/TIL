n = int(input())
arr = []
# for i in range(20):
#   arr.append([])
#   for j in range(20):
#     arr[i].append(0)
# 위와 같이, 모두 0이 채워진 2차원 리스트를 만드는 코드를 아래와 같은 방법으로 짧게 만들 수도 있다.
# ... [0 for j in range(20)]  #20개의 0이 들어간 [0, 0, 0, ... , 0, 0, 0] 리스트 
# 아래처럼 작성하면 위와 같은 리스트가 20개가 들어간 리스트를 한 번에 만들어 준다.

# d = [[0 for j in range(20)] for i in range(20)]

# 이러한 리스트 생성 방식을 List Comprehensions 라고 한다.
arr = [[0 for j in range(20)] for i in range(20)]


for i in range(n):
  x, y = input().split()
  arr[int(x)][int(y)]=1

for i in range(1,20):
  for j in range(1,20):
    print(arr[i][j], end=' ')
  print()