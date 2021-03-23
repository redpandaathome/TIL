n = int(input())
count=0
for i in range(n+1):
  for j in range(60):
    for k in range(60):
      result = str(i)+str(j)+str(k)
      # print(result)
      if '3' in result:
        count+=1
      else:
        continue
        
print(count)