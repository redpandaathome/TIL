#1. nested array
graph = [[]for _ in range(3)]
print(graph)
##[[],[]]

print([0]*3)
#[0,0,0]

print([[0]*3 for i in range(2)])
##[[0, 0, 0], [0, 0, 0]]


#2.
arr=[1,2,3]
print([x for x in arr if x>=2])
##[2,3]