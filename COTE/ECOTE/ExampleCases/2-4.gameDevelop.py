n, m = map(int, input().split())

x, y, d = map(int, input().split())

graph=[]
for i in range(n):
  graph.append(list(map(int, input().split())))

#왼쪽으로 회전...0123 북동남서
dx = [-1,0,1,0]
dy = [0,-1,0,1]

result=1
dCount = 0
graph[x][y]=2
while True:
  #만약 현방향이 0이면...왼쪽은dx[1]
  if dCount==4:
    print('dCount==4!')
    nx = x-1
    ny = y
    if nx<0 or ny<0 or nx>n or ny>m:
      break
    elif graph[nx][ny]==1:
      break
    else:
      x, y = nx,ny
      dCount=0
      continue

  if d+1>3:
    d=0
  else:
    d+=1
  dCount+=1
  print("방향을 바꾸었다...d:",d," dCount:", dCount)

  nx = x + dx[d]
  ny = y + dy[d]

  if graph[nx][ny]==0:
    print('전진! nx:', nx, " ny:", ny)
    x=nx
    y=ny
    graph[nx][ny]=2
    result+=1
    dCount=0
    print("전진 후 그래프:",graph)
  else:
    print("전진못함")
    continue

print(result)
  
  


#input
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
#output
=>3