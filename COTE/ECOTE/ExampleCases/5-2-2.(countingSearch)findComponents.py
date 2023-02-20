#input
5
8 3 7 9 2
3
5 7 9

#output 
no yes yes

# Count Sort
n = int(input())
arrA = [0] * (1000001)
# a = list(map(int, input().split()))
for i in input().split():
    arrA[int(i)] += 1


k = int(input())
b = list(map(int, input().split()))
for i in b:
    if arrA[i] > 0:
        print('yes')
    else:
        print('no')

