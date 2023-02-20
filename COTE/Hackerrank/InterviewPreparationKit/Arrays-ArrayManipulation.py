# https://www.hackerrank.com/challenges/crush/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
# 2022.03.23

#Failed due to timeout 🧐🧐🧐
def arrayManipulation(n, queries):
    # Write your code here

    graph = [[0]*n for i in range(m)]
    
    for i in range(m):
        start = queries[i][0]
        end = queries[i][1]
        k = queries[i][2]
        # print("---i>",i)
        for x in range(m): #💜
            for j in range(start-1, end):
                graph[x][j]+=k
        # print("graph>>>:",graph)
    
    return findMaxVal(graph)
    
def findMaxVal(arr):
    length=len(arr)
    maxVal=0
    for i in range(length):
        maxVal = max(maxVal, max(arr[i]))
    return maxVal


#Improved version... https://youtu.be/6dbfeaqRBFU
#[ ]
def arrayManipulation(n, queries):
    # Write your code here
    graph = [0]*(n+1)
    
    for i in range(m):
        # print("i:",i)
        start = queries[i][0]
        end = queries[i][1]
        k = queries[i][2]

        graph[start-1]+=k
        graph[end]-=k
    # print("graph>>>:",graph)
    
    ans = 0
    cur = 0
    for i in graph:
        cur += i
        if cur > ans:
            ans=cur
    return ans