#how to skip to next i in for range in python?
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        isDone=False
        for i in range(len(arr)):
            if not isDone and arr[i]==0:
                arr.insert(i,0)
                arr.pop()
                isDone=True
            elif isDone:
                isDone=False


#s1 this way - i chould be changed
class Solution:
	def duplicateZeros(self, arr: List[int]) -> None:
		i = 0
		n = len(arr)
		while(i<n):
			if arr[i]==0:
				arr.pop()
				arr.insert(i,0)
				i+=1
			i+=1


#s2 different way
def duplicateZeros(self, arr: List[int]) -> None:
        res = []
        for x in arr:
            res.append(x)
            if x == 0:
                res.append(x)
        for i in range(len(arr)):
            arr[i] = res[i]