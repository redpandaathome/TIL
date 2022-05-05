//https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3247/

/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
 var removeElement = function(nums, val) {
   for(let i=0; i<nums.length; i++){
       if(nums[i]===val){
           nums.splice(i,1)
           i-=1
       }
   }
};