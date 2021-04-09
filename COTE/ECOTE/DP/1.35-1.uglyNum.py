n = int(input())
arr = [1,2,3,5]
ans = [1]
i=2
while len(ans)<n:
    if i%2 !=0 and i%3!=0 and i%5!=0:
        i+=1
        continue
    else:
        ans.append(i)
    print('ans:',ans, ', i:',i)
    i+=1
# print(len(ans), n)
print(ans[n-1])
        