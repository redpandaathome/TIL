n = int(input())
plan = list(input().split())

x,y=1,1
for move in plan:
  if move=='L' and y-1>0:
    y-=1
  elif move=='R' and y+1<n+1:
    y+=1
  elif move=='U' and x-1>0:
    x-=1
  elif move=='D' and x+1<n+1:
    x+=1
print(x, y)