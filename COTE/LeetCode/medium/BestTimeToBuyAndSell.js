//https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/
// What I thought... in case of [7,1,5,3,6,4]
//n[0]= -7+ max(7,1) =0 <-value[0]
//n[1]= -1+ max(1,5) =4
//...
//n[3]= -3+ max(3,6) =3
// answer = sum(values)
/**
 * @param {number[]} prices
 * @return {number}
 */
 var maxProfit = function(prices) {
   let values=[]
   for(let i=0; i<prices.length; i++){
       let temp=(-prices[i]+Math.max(prices[i], prices[i+1]?prices[i+1]:0))
       values.push(temp)
   }
   return values.reduce((ac,cu)=>ac+cu)
};


//solution1
var maxProfit = function(prices) {
    
   // It is impossible to sell stock on first day, set -infinity as initial value for curHold
   let [curHold, curNotHold] = [-Infinity, 0];
   
   for(const stockPrice of prices){
       
       let [prevHold, prevNotHold] = [curHold, curNotHold];
       
       // either keep hold, or buy in stock today at stock price
       curHold = Math.max(prevHold, prevNotHold - stockPrice );
       
       // either keep not-hold, or sell out stock today at stock price
       curNotHold = Math.max(prevNotHold, prevHold + stockPrice );
   }
   
   // Max profit must come from notHold state finally.
   return curNotHold; 
};

//Trial 1
var maxProfit = function(prices) {
   let [cH,cNH]=[-Infinity, 0]
   for (const price of prices){
       let [pH, pNH]= [cH, cNH];
       
       cH = Math.max(pH,pNH-price)
       cNH = Math.max(pNH, pH+price)
   } 
   return cNH
};