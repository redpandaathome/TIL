# https://www.acmicpc.net/problem/10974
# 모든순열

import sys
import itertools
n = int(input())
seq = [int(x)+1 for x in range(n)]

list = list(itertools.permutations(seq, n))
for i in list:
    print(" ".join(map(str, i)))
