class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        temp = [pow(n,2) for n in nums]
        return sorted(temp)