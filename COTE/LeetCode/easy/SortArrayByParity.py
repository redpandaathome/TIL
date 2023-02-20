class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x: x%2)


#s1
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[i] % 2 :
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1 
                
            else:
                i += 1
                left += 1

        return nums