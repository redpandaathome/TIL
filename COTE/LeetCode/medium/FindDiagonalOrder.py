# way to flat... 
# result=[[1],[2,3]] [e for arr in result for e in arr ]
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m=len(mat)
        n=len(mat[0])
        result=[[] for i in range(m+n-1)]
        for i in range(0, m):
            for j in range(0, n):
                key=i+j
                if key%2==0:
                    result[key].insert(0,mat[i][j])
                else:
                    result[key].append(mat[i][j])
        return [e for arr in result for e in arr ]