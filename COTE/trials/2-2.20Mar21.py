m,n = map(int, input().split())

graph = []
for i in range(n):
	graph.append(list(input()))
	#[['c', '.', 'x', 'c'], ['.', '.', '.', '.'], ['x', 'x', '.', '.'], ['.', '.', '.', 'x'], ['x', '.', '.', 'x']]
startPoints = []
for i in range(m):
	if graph[0][i]=='c':
		startPoints.append(i)
# print(startPoints) >>[0,3]

def dfs(x, y, result):
	if x<=-1 or x>=n or y<=-1 or y>=m:
		return False
	elif graph[x][y]=='x':
		return False
	elif x!=n-1 and y!=m-1:
		dfs(x+1,y, result)
		result+=1
		# print("bf2 result:", result)
		dfs(x, y+1, result)
  else:
		return result
	
answer=0

for i in startPoints:
	temp = dfs(0,i,0)
	print("temp: ", temp)
	if not temp:
		temp=1000
		
	answer = min(temp ,answer)
print(answer)



##input
4 5
c.xc
....
xx..
...x
x..x

##output
1


##??? 흠..뭐가 문제였을까? 다시 차근차근 🐛
## 진짜 진짜 재밌었다... 4시간이 그냥 훌쩍 가버림...
## dfs, bfs 공부가 더 필요하다!! 파이썬 아주 아주 훌륭하다 💘
## 2rd도 갈 수 있음 ㅜㅜ 좋을테지만 이번엔 무리인 것 같고
## 다음엔 더 잘 달릴 수 있도록 준비가 필요하다. 준비준비 🏃🏻‍♀️🏃🏻‍♀️🏃🏻‍♀️🏃🏻‍♀️🏃🏻‍♀️