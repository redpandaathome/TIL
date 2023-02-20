#input
3
홍길동 95
이순신 77
흥부 100

#output
이순신 홍길동

n = int(input())
array = []
for i in range(n):
  input_data = input().split()
  # ✨
  array.append((input_data[0], int(input_data[1])))

# def setting(data):
#   return data[1]

# array = sorted(array, key=setting)
# ✨
array = sorted(array, key=lambda student: student[1])

for i in array:
  print(i[0], end=' ')