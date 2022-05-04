https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3237/

/**
 * @param {number[]} nums
 * @return {number}
 */
 var findNumbers = function(nums) {
   let lengthList=nums.map(el=>el.toString().length)
   return lengthList.reduce((cnt,e)=>{
       if(parseInt(e)%2===0){
           return cnt+=1
       }
       return cnt
   }, 0)
};

//s1
var findNumbers = function(nums) {

   const isEvenNums = num => {
       return String(num).length % 2 === 0;  
   };
   
   return nums.filter(elem => isEvenNums(elem)).length;
   
};