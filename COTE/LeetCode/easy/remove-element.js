/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
 var removeElement = function(nums, val) {
   let s = nums.filter(e=>
       e!=val
   )
   nums.splice(0,nums.length,...s)
   // console.log(nums)
   return nums.length
};