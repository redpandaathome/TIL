class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)-1, 0,-1):
            print(i)
            if nums[i]==nums[i-1]:
                nums.remove(nums[i])
        
# remove!

#[👾] 2nd 29.04.2022...
#[ ]