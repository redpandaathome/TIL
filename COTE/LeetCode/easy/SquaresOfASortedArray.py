class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        temp = [pow(n,2) for n in nums]
        return sorted(temp)

#t2
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([pow(e,2) for e in nums])

#s1
#✨[None for _ in A]
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        result = [None for _ in A]
        left, right = 0, len(A) - 1
        for index in range(len(A)-1, -1, -1):
            if abs(A[left]) > abs(A[right]):
                result[index] = A[left] ** 2
                left += 1
            else:
                result[index] = A[right] ** 2
                right -= 1
        return result