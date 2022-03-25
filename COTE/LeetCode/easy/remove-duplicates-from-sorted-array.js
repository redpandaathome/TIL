// https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/

/**
 * @param {number[]} nums
 * @return {number}
 */
 var removeDuplicates = function(nums) {
   for(let i=0; i<nums.length; i++){
      let dupNum =0
      let cur = nums[i]
       for(let j=i+1; j<nums.length; j++){
           let compare = nums[j]
           if(cur==compare){
               dupNum+=1
           } else {
               break
           }
       }
       nums.splice(i+1,dupNum)
       // console.log("NEW ARR:",nums)
   }

};


// IMPROVED
var removeDuplicates = function(nums) {
   nums.splice(0,nums.length,...(new Set(nums)))
};