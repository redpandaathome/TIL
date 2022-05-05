#✨
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3: return False
        i=0
        while(i<len(arr)-1):
            if arr[i+1]>arr[i]:i+=1
            else: break
        if i==0 or i==(len(arr)-1): return False
        while(i<len(arr)-1):
            if arr[i+1]<arr[i]:i+=1
            else:
                break
        if i==len(arr)-1:
            return True
        else:
            return False