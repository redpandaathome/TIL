#2. stack
stack = []

stack.append(1)
stack.append(2)
stack.pop()

#queue
from collections import deque
q = deque()
q.append(1)
q.append(2)
q.popleft()
q.reverse()

#Adjacency Matrix
INF = 999999999

graph1 = [
   [0,7,5],
   [7,0,INF],
   [5, INF, 0]
]

#graph1...
#[[0,7,5],[7,0,INF],[5,INF,0]]



#Adjacency list
graph2 = [[] for _ in range(3)]

#node 0 info
graph2[0].append((1,7))
graph2[0].append((2,5))

#node 1
graph2[1].append(0,7)

#node 2
graph2[2].append(0,5)

#graph2...
#[[(1,7), (2,5)], [(0,7)], [(0,5)]]