#[x for x in arr if x>0]
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i,e in enumerate(nums):
            idx=abs(e)-1
            nums[idx]=abs(nums[idx])*-1
        result=[i+1 for i,x in enumerate(nums) if x>0]
        return result