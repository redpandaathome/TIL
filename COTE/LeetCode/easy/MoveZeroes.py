class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroIdx=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i], nums[zeroIdx]= nums[zeroIdx], nums[i]
                zeroIdx+=1
        return nums