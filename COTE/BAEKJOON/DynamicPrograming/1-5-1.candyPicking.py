#https://www.acmicpc.net/problem/11048

#헐... 저번에 못풀었던 건데 기본 유형인가보넹
#✨✨✨✨✨ dp라고 생각하고 푸니 풀었지만 너무 오래걸렸다.
#다시 시간단축해서 풀어봐야 함 🐝

n, m = map(int, input().split())
# print(n,m)
arr=[]

for i in range(n):
  arr.append(list(map(int,input().split())))
  
dx = [1,0,1]
dy = [0,1,1]

graph= [[ 0 for i in range(m)] for j in range(n)]
# graph[0][0]=arr[0][0]
# print('graph:', graph)
for i in range(n):
  for j in range(m):
    # print("i:",i, ", j:",j)
    maxVal = 0
    #✨개선... 굳이 이렇게 안하고 더 간결하게 max(a,b,c)로 해도 됐을듯.
    for k in range(3):
      bx = i-dx[k]
      by = j-dy[k]
      # print("bx:",bx, "by:",by)
      # print("graph[bx][by]:", graph[bx][by])
      if bx<0 or by<0 or bx>n-1 or by>m-1:
        continue
      maxVal = max(maxVal, graph[bx][by])
      
    graph[i][j]= arr[i][j]+maxVal
    arr[i][j]= graph[i][j]
    # print("arr[",i,"][",j,"]:", arr[i][j], "+ maxVal:",maxVal, '=', arr[i][j]+maxVal)
    # print("new graph:", graph)

print(graph[n-1][m-1])