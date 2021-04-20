# https://www.acmicpc.net/problem/11726
# 2×n 타일링

import sys
input = sys.stdin.readline

n = int(input())

d = [0]*1001
d[1] = 1
d[2] = 2
for i in range(3, n+1):
    d[i] = (d[i-2]+d[i-1]) % 10007

print(d[n])
    

    
