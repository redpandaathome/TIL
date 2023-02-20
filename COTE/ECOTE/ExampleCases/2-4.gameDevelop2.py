#n * m - land or sea(a - x, b - y)
#from current direction -> left (anti clock)
# left - new? rotate to the left -> go
# all 4 directions are old or sea -> go one block behind you (if it's sea -> DONE)
# check how many blocks it can move
# n, m
# a, b, direction
#north east south west
#0 1 2 3
#n lines to tell you if it's land or sea(0 land 1 sea)

n, m = map(int, input().split())
a, b, d = map(int, input().split())
givenMap = []
for i in range(n):
  temp = list(map(int, input().split()))
  givenMap.append(temp)

count = 1
print(givenMap[a][b])

#n, w, s, e
nx = [0,1,0,-1]
ny = [-1,0,1,0]

allChecked = False
moved = False
while not allChecked:
  print("While start! current...", a,b,d)
  moved = False
  for i in range(d,d+4):
    i = i%4
    print("for...i:", i)
    dx = a + nx[i]
    dy = b + ny[i]
    print("dx, dy:", dx, dy, "givenMap:", givenMap[dx][dy])
    if dx<0 or dy<0 or dx>=n or dy>=m:
      continue
    if givenMap[dx][dy] == 0:
      print("entering...", dx, dy, givenMap[dx][dy])
      count += 1
      givenMap[a][b]=2
      a, b = dx, dy
      givenMap[a][b]=2
      d = i
      print("enter->change..", givenMap, ", a,b:", a,b)
      moved = True
      break
  if moved:
    continue
  print("....allChecked...True")
  allChecked = True
  #check behind!
  dx = a +nx[(d+2)%4]
  dy = b + ny[(d+2)%4]
  if givenMap[dx][dy] != 1:
    a, b = dx, dy
    allChecked = False

print("count:",count)
