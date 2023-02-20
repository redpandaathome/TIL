
# 크루스칼 알고리즘(Kruskal) - greedy
# Topology Algorithms (위상정렬) - queue or stack

# Dijkstra Algorithms - Priority Queue(<-Min or Max Heap : 🌲 tree DS)

#🌲 tree DS
1) 부모->자식 계층적 모델
2) 루트 노드 존재
3) 비순환
4) 방향 그래프

# Graph
1) 네트워크 모델
2) 루트노드X
3) 순환Or비순환
4) 방향Or무방향

트리는 그래프의 일종, 부모-자식, 방향성이 존재.

그래프의 구현방법 - 인접행렬(Adjacency Matrix), 인접리스트(Adjacency List)

#node num:v, edge num:e
메모리공간, a->b 간선비용 찾기
인접행렬=>O(v2), O(1)
인접리스트=>O(e), O(v)

다익스트라 최단 경로 알고리즘 - 인접 리스트로 풀어봄
플로이드 워셜 알고리즘 - 인접 행렬로...

최단경로Q -> 노드 수가 적다(FW), 많다(Dijkstra)


다음으로 서로소 집합(Disjoint Sets), Kruskal, Topology ...