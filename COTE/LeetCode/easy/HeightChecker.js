// ✨ array deep copy! [...arr]
// ✨ careful btw .sort(), .sort((a,b)=>a-b) 
/**
 * @param {number[]} heights
 * @return {number}
 */
 var heightChecker = function(heights) {
   let sortedArr= [...heights].sort((a,b)=>a-b)
   let k=0
   for(let i=0; i<heights.length; i++){
       if(sortedArr[i]!==heights[i]){
           k++;
       }
   }
   return k
};


//✨✨✨ reduce(ac,cu,idx)!? return...
//~~ double not bitwise operator https://stackoverflow.com/questions/5971645/what-is-the-double-tilde-operator-in-javascript
// a + (heights[i] !== b) works too... a+ true = a+1
var heightChecker = function(heights) {
   return [...heights].sort((a,b) => a-b).reduce((a,b,i) => a + (~~heights[i] !== b), 0);
};


//t1 
/**
 * @param {number[]} heights
 * @return {number}
 */
 var heightChecker = function(heights) {
   return [...heights].sort((a,b)=>a-b).reduce((ac,cu, i)=>{    console.log(ac, cu, i)
       if(heights[i]!==cu){
           ac+=1
       }
       return ac
   },0)
};