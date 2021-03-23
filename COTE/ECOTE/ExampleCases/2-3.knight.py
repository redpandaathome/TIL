n = input()
x = n[0]
y = int(n[1])

arr = ['a','b','c','d','e','f','g','h']
x = arr.index(x)+1

# 좌상, 우상, 좌하, 우하, 가로로~
dx = [-2,-2, 2, 2, -1, 1, -1,1]
dy = [-1,1, -1, 1, -2, -2, 2, 2]

answer=0
for case in range(len(dx)):
  nx = x+dx[case]
  ny = y+dy[case]
  if nx<1 or ny<1 or nx>8 or ny>8:
    continue
  answer+=1
print(answer)
