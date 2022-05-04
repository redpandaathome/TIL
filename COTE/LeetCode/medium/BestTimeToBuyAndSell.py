#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        values=[]
        for i,p in enumerate(prices):
            print(i,p)
            next=0
            if len(prices)>i+1:
                next=prices[i+1]
            temp= max(next, p)
            values.append(-p+temp)
        return sum(values)


#s1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
		# It is impossible to sell stock on first day, set -infinity as initial value for cur_hold
        cur_hold, cur_not_hold = -float('inf'), 0
        
        for stock_price in prices:
            
            prev_hold, prev_not_hold = cur_hold, cur_not_hold
            
			# either keep hold, or buy in stock today at stock price
            cur_hold = max( prev_hold, prev_not_hold - stock_price )
			
			# either keep not-hold, or sell out stock today at stock price
            cur_not_hold = max( prev_not_hold, prev_hold + stock_price )
            
        # maximum profit must be in not-hold state
        return cur_not_hold if prices else 0

#t1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cH, cNH = float('-inf'),0
        for p in prices:
            pH, pNH = cH, cNH
            cH=max(pH, pNH-p)
            cNH=max(pNH, pH+p)
        return cNH