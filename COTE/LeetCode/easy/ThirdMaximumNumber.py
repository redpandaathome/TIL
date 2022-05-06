#✨✨✨ 
# arr=list(set(arr))
# and then, arr.sort()
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # print(nums)
        # print(set(nums))
        # print(list(set(nums)))
        
        #list.sort sorts the list in place, i.e. it doesn't return a new list. Just write
        # so you can't do below cos list(set(nums)) is not declared anywhere and sort() does not return but only changes input
        # nums = list(set(nums)).sort()
        nums = list(set(nums))
        nums.sort()
        return nums[len(nums)-3] if len(nums)>=3 else nums[len(nums)-1]