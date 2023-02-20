//https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3260/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var sortArrayByParity = function(nums) {
   return nums.sort((a,b)=>a%2-b%2)
};


//s1
var sortArrayByParity = function(nums) {
   let j=0;
   for(let i=0; i< nums.length; i++){
       if(nums[i]%2 === 0){
           [nums[i],nums[j]] = [nums[j],nums[i]]
           j++;
       }
   }
   return nums;
};