
from collections import deque

q = deque()
p = deque()
r = deque()

q.append(1)
q.append(2)
print(q.popleft()) # expected 1

p.append((1,2))
p.append((3,4))
print(p.popleft()) # 1 2?
a, b = p.popleft()
print("(a,b)=>", a,b)

r.append([1,2])
r.append([3,4])
print(r.popleft()) # 1 2?
c, d = r.popleft()
print("[c,d]=>", c, d)

# 1
# (1, 2)
# (a,b)=> 3 4
# [1, 2]
# [c,d]=> 3 4