# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import math
n, k = map(int, input().split())
arr = list(map(int,input().split()))

print(math.ceil((n-1)/(k-1)))

##모두다른 구슬 n개중에 k개씩 골라서 같은 구슬로 만들 수 있다. 총 몇 번 골라야 모두 한가지 구슬이 될까?

##n k
##구슬배열
##input1
# 4 3
# 2 3 1 4
##output1
# 2

##input2
# 8 3
# 7 3 1 8 4 6 2 5
##output2
# 4

##input3
# 37 4
# 31 36 20 30 1 9 6 13 3 29 11 25 7 8 2 24 34 18 26 15 23 28 37 19 21 4 32 14 16 10 12 27 22 35 5 17 33
##output3
# 12