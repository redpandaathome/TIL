#join(strArr), join(str(d) for d in arr)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_value=''.join(str(d) for d in digits)
        return list(str(int(str_value)+1))


#first for loop range should be >0 to take care of index 0 separately for a case like [9]
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lastIdx=len(digits)-1
        digits[lastIdx]+=1
        for i in range(lastIdx,0,-1):
            if digits[i]==10:
                digits[i]=0
                digits[i-1]+=1
            else:
                break
        if digits[0]==10:
            digits[0]=0
            digits.insert(0,1)
        return digits