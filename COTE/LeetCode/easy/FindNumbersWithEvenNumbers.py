class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt=0
        for n in nums:
            if len(str(n))%2==0:
                cnt+=1
        return cnt


# sum(n~ for n in arr)
# print(2%2==0) ...True
# arr=[True,True,False]
# print(sum(arr)) ...2
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(len(str(n))%2==0 for n in nums)