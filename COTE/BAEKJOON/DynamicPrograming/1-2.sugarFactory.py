N = int(input())
a = N//5
while a>=0:
    if (N-a*5)%3 == 0:
        print(a+(N-a*5)//3)
        exit()
    a -= 1
print(-1)