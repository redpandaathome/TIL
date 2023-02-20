//
//[ ] again
//solution
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
 const revNums = (nums,start,end)=>{
   console.log("->revNums...",start,end)
   while(start<end){
       [nums[start],nums[end]]=[nums[end],nums[start]]
       start++
       end--
       console.log("swaped...", nums, start, end)
   }
}
var rotate = function(nums, k) {
   console.log("===old k...",k, nums)
   k=k%nums.length
   console.log("new k...",k)
   nums.reverse();
   console.log("reversed nums...", nums)
   revNums(nums, 0,k-1)
   revNums(nums, k,nums.length-1)
   
};

//s2✨
var rotate = function(nums, k) {
   for (let i = 0; i < k; i++) {
       nums.unshift(nums.pop());
   }
};