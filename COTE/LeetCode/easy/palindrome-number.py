class Solution:
    def isPalindrome(self, x: int) -> bool:
        strNum = str(x)
        right=''
        if strNum[0]=='-':
            return False
        
        midNum =len(strNum)//2
        left= strNum[0:midNum]
        if len(strNum)%2==0:
            right= strNum[midNum:len(strNum)]
        else:
            right= strNum[midNum+1:len(strNum)]
            
        reversedRight=reverseString(right)
        if left==reversedRight:
            return True
        else:
            return False
        
def reverseString(x):
        return x[::-1]