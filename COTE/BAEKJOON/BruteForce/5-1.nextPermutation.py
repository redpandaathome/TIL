# https://www.acmicpc.net/problem/10972
# 다음순열🌺🌺🌺

import sys
n = int(input())
seq = [int(x) for x in sys.stdin.readline().split()]

k = -1
# k의 최대값
for i in range(n-1):
    #print('i:', i, seq[i], seq[i+1])
    if seq[i] < seq[i+1]:
        k = i
#print('k:',k)
if k == -1:
    print(-1)
else:
    # m의 최댓값
    for j in range(k+1, n): #n!!! not n-1 (n은 포함 하지 않으니까.)
        #print('j:',j, seq[k], seq[j])
        if seq[k] < seq[j]:
            m = j
    # k <-> m
    seq[k], seq[m] = seq[m], seq[k]
    
    # sort
    temp = seq[k+1:]
    temp.sort()
    
    print('seq?',seq, ', temp?', temp )
    answer = seq[:k+1] + temp
    print(' '.join(map(str, answer)))
    # print(' '.join(map(str, seq)))