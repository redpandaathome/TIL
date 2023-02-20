class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cnt=0
        cur=0
        for n in nums:
            cur=cur+n
            max_cnt=max(max_cnt, cur)
            if not n:
                cur=0
        return max_cnt