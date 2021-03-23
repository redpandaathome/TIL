# 먹이 | 더이상못움직 까지 우하향
# ✨✨✨✨✨1~10 * 1~10 인덱스를 사용하고 싶다면 아래처럼
arr= []
for i in range(11):
  arr.append([])
  for j in range(11):
    arr[i].append(1) #벽(막힌길)
for i in range(10):
  line = list(map(int, input().split()))
  for j in range(10):
    arr[i+1][j+1]=line[j]
# ✨✨✨✨✨

print(arr)
x,y = [2,2]

while x!=10 and y!=10:
  if arr[x][y]==2:
    arr[x][y]=9
    break
  elif arr[x][y]==0:
    arr[x][y]=9
    if arr[x][y+1]!=1:
      print("1: arr[" , x ,"][", y , "+1]=" , arr[x][y+1])
      y+=1
    elif arr[x+1][y]!=1:
      print("2: arr[",x,"+1][",y,"]=",arr[x+1][y])
      x+=1
    else:
      print("else...?")
      break

for i in range(1,11):
  for j in range(1,11):
    print(arr[i][j], end=' ')
  print()