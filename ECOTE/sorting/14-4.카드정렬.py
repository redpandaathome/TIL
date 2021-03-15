# https://www.acmicpc.net/problem/1715
# ✨

import heapq
n = int(input());
heap= []
for i in range(n):
  data= int(input())
  heapq.heappush(heap, data)

result=0
# print('heap',heap)

while len(heap) !=1:
  one = heapq.heappop(heap)
  two = heapq.heappop(heap)
  # print('one:',one, ' ,two:', two)
  # print('heapq.pop*2=>', heap)

  sum_value=one+two;
  result+=sum_value;
  heapq.heappush(heap, sum_value)
  # print('heapq.push=>', heap)

print (result)


###input
3
10
20
40

###output
100


#콘솔창
4
1
2
3
4
heap [1, 2, 3, 4]
one: 1  ,two: 2
heapq.pop*2=> [3, 4]
heapq.push=> [3, 4, 3]
one: 3  ,two: 3
heapq.pop*2=> [4]
heapq.push=> [4, 6]
one: 4  ,two: 6
heapq.pop*2=> []
heapq.push=> [10]
19