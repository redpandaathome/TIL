#✨
#input
3

#output
5

n = int(input())

d=[0]*1001
d[1]=1
d[2]=3
for i in range(3,n+1):
 d[i]=(d[i-1]+d[i-2]*2)%796796
print(d)
print(d[n])
print(d[n]%796796)