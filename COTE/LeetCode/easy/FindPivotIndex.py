class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_total=sum(nums)
        sum_left=0
        for i,e in enumerate(nums):
            sum_left+=e
            if(sum_left==sum_total-sum_left+e):
                return i
        return -1