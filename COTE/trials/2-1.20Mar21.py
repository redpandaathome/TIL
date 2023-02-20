m,n = map(int, input().split())

graph = []
answers= []
for i in range(n):
	graph.append(list(map(int, input().split())))

def dfs(x,y,result):
	if x<=-1 or x>=n or y<=-1 or y>=m:
		return False
	if graph[x][y]>=0:
		# print("x", x, "y", y)
		result+=graph[x][y]
		# print('result so far:', result)
		dfs(x, y+1, result)
		dfs(x+1, y, result)
	if x == n-1 and y==m-1:
		answers.append(result)
	
temp = dfs(0, 0, 0)
print(answers)
print(max(answers))

starts = [0,3]
for i in starts:
  print(i)


#문제의 케이스는 무엇이었을까?
# 출발->목적지 간 최대로 수확하는 문제...