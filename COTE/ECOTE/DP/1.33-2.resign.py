n = int(input())
t = []
p = []
for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

# ✨✨✨✨✨ 뒤에서 접근. n=6~0 i번째에서 t[i]+i = 총걸릴시간 <=n(주어진시간), 뒤에서 부터 최적 dp[i] 업데이트!
max_v = 0
dp = [0 for i in range(n+1)]
for i in range(n-1, -1, -1): 
    time = t[i]+i
    if time<=n:
        dp[i] = max(max_v, p[i]+dp[time])
        max_v = dp[i]

    # else 부분은 없어도 되는 것 같은데 왜 에러가 날까? IDE에서 돌리면 맞는데...흠
    else:
        print('...else...?i:',i, ", n:",n)
        dp[i]=max_v
        print(dp[i])
print(max_v)
print(dp)
        
