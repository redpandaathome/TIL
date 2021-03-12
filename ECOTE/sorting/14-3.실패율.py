#https://programmers.co.kr/learn/courses/30/lessons/42889?language=python3

def solution(N, stages):
    answer = []
    stages.sort(); #[1,2,2,2,3,3,4,6]
    ratio = []
    for k in range(1,N+1):
      # i 단계에서 실패율: 
      failRate = stages.count(k) / sum(i>=k for i in stages) if stages.count(k)>0 else 0
      if k<N+1:
          ratio.append([k,failRate])
    ratio.sort(key=lambda x: (-x[1],x[0]))
    answer = list(map(lambda x: x[0], ratio))
    return answer

#개선할 점? sum대신 length를 감소해가며 한다면 더 간결/빠른 코드가 될 수 있겠다.
#✨ 개선해 보기.[ ]


#input(N, stages) / output(result) 예시
N	stages	result
5	[2, 1, 2, 6, 2, 4, 3, 3]	[3,4,2,1,5]
4	[4,4,4,4,4]	[4,1,2,3]