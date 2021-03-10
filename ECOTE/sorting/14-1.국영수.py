#  https://www.acmicpc.net/problem/10825
# 2021.03.10

n = int(input())
print('n: ', n)
arr = [];
for i in range(n):
  arr.append(input().split());


# 1. sort냐 sorted냐... 
# https://www.programiz.com/python-programming/methods/list/sort
#list.sort(key=..., reverse=...)
#sorted(list, key=..., reverse=...)

# 2. sorted 사용시 유의
# arr = [1,5,3,2]
# print(sorted(arr)) ->None 
# => 아래처럼 해야 출력
# sorted(arr) 
# print(arr)

# 3. sort - Sort the list using key
# def takeFirst(el):
#   return el[0]
# random = [(2, 2), (3, 4), (4, 1), (1, 3)]
# random.sort(key=takeFirst)
# print(random)


arr.sort(key=lambda x: 
(-int(x[1]), #감소하는 형태
int(x[2]),  #증가
-int(x[3]), 
x[0]) #이름 사전순(단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)
)

for student in arr:
  print(student[0])


# Input 예시
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90

# Output 예시
Donghyuk
Sangkeun
Sunyoung
nsj
Wonseob
Sanghyun
Sei
Kangsoo
Haebin
Junkyu
Soong
Taewhan
