# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())
arr=[]
for i in range(n):
	arr.append(list(map(int, input().split())))
# [[12, 0], [10, 14], [4, 20], [5, 2147483648]]

def check(n, m):
	cup=0
	# nCup = n//5
	# ntCup = n//12;
	# mCup = m//7;
	while n>=5 and n+m>=12:
		nCup = n//5
		ntCup = n//12;
		mCup = m//7;
		if nCup >=1 and mCup>=1:
			extra = min(nCup, mCup)
			n-=5*extra
			m-=7*extra
			cup+=extra
		elif nCup>=1 and 0<m: ###
			nNeed=12-m;
			n-=nNeed;
			m=0;
			cup+=1
		elif ntCup>=1:
			n-=12*ntCup;
			cup+=ntCup
		else:
			return cup
	return cup
		

for i in range(n):
	a = arr[i][0];
	b = arr[i][1];
	print(check(a,b))



###note : Special coins at least 5 + normal coins = 12 (one present).
###How many presents can you get?
###input example:
#4
# 12 0
# 10 14
# 4 20
# 5 2147483648
###output example:
#1
# 2
# 0
# 1