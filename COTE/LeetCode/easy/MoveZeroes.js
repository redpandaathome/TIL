//https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3157/

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
 var moveZeroes = function(nums) {
   let zArr=[]
   let nArr=[]
   for(let i=0; i<nums.length; i++){
       if(nums[i]===0)zArr.push(i)
       if(nums[i]!==0)nArr.push(i)
   }
   
   for(let i=0; i<zArr.length; i++){
       let temp= nums.splice(zArr[i]-i,1)
       nums.push(...temp)
   }
};

// better solution ✨✨✨
var moveZeroes = function(nums) {
   let idxForNonZero = 0;
   for (let i = 0; i < nums.length; i++) {
       if (nums[i] !== 0) {
           [nums[idxForNonZero], nums[i]] = [nums[i], nums[idxForNonZero]];
           idxForNonZero++;
           // no need to check the swapped number because we are scanning through the array from the left so it is guaranteed that 
           // the element at the idxForNonZero is zero (not non-zero).
       }
   }
   return nums;  
   // Time Complexity: O(n)
   // Space Complexity: O(1)
};