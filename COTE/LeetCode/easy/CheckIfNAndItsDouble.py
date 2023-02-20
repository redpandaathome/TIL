class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        print(arr)
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                if arr[i]==arr[j]*2 or arr[j]==arr[i]*2:
                    return True
        return False


# In case of [0,0] -> print(i, arr.index(arr[i]*2)) -> 1,0✨
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        print(arr)
        for i in range(len(arr)):
            if arr[i]*2 in arr and arr.index(arr[i]*2)!=i:
                return True
        return False