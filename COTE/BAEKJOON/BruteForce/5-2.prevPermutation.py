import sys
n = int(input())
seq = [int(x) for x in sys.stdin.readline().split()]

k = n-1
for i in range(n-2, -1, -1):
    #i (3,2,1,0)
    #print('i:', i, "...", seq[i], ", i+1:", i+1, "...", seq[i+1])
    if seq[i] > seq[i+1]:
        k = i
        break
#print('k:', k)

if k == n-1:
    print(-1)
else:
    for i in range(k+1, n):
        #print('i:', i, "...", seq[i], ", i-1:", i-1, "...", seq[i-1])
        if seq[k] > seq[i]:
            m = i
            #break 🌺 여기는 넣으면 안되지 최대값 구해야 하는데 앞에서 부터 접근하니까. 쭉 타고올라가야!
    #print('m:', m)
    seq[k], seq[m] = seq[m], seq[k]

    temp = seq[k+1:]
    temp.sort(reverse=True)
    answer = seq[:k+1]+temp
    print(' '.join(map(str, answer)))



####🌺아래처럼 하던지
import sys
n = int(input())
seq = [int(x) for x in sys.stdin.readline().split()]

k = n-1
for i in range(n-2, -1, -1):
    #i (3,2,1,0)
    #print('i:', i, "...", seq[i], ", i+1:", i+1, "...", seq[i+1])
    if seq[i] > seq[i+1]:
        k = i
        break
#print('k:', k)

if k == n-1:
    print(-1)
else:
    #🌺 k+1 ~ n-1까지 커버하되 뒤에서 부터 하고싶다?
    for i in range(n-1, k, -1):
        #print('i:', i, "...", seq[i], ", i-1:", i-1, "...", seq[i-1])
        if seq[k] > seq[i]:
            m = i
            break
    #print('m:', m)
    seq[k], seq[m] = seq[m], seq[k]

    temp = seq[k+1:]
    temp.sort(reverse=True)
    answer = seq[:k+1]+temp
    print(' '.join(map(str, answer)))