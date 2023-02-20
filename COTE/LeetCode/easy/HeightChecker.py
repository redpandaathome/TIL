class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortedArr= sorted(heights)
        k=0
        for i in range(len(heights)):
            if heights[i]!=sortedArr[i]:
                k+=1
        return k