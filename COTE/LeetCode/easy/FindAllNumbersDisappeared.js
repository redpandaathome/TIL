//https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3270/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var findDisappearedNumbers = function(nums) {
   let refArr=[]
   for(let i=0; i<nums.length; i++){
       refArr.push(i+1)
   }
   
   let result=[]
   refArr.forEach(e=>{
       if(nums.indexOf(e)<0){
           result.push(e)
       }
   })
   return result;
};

// ✨✨✨ interesting! 
var findDisappearedNumbers = function(nums) {
   let res = [];
   for (let i = 0; i < nums.length; i++) {
       let num = Math.abs(nums[i]);
       let idx = num-1;
       nums[idx] = Math.abs(nums[idx]) * -1;
   }
   for (let i = 0; i < nums.length; i++) {
       if (nums[i] > 0) res.push(i+1);
   }
   return res;
   // Time Complexity: O(N)
   // Space Complexity: O(1)
};
/*
We will scan through the input array and for every number we will use its value as an index and
negate the number at the index. For example, if we encounter 4, we will negate the number at index 3.
The reason the index is not four is because the array is zero-indexed.
*/


/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var findDisappearedNumbers = function(nums) {
   let res = []
   nums.forEach((val, ind, arr) => {
       let tmp = Math.abs(arr[ind]) - 1;
       if (arr[tmp] > 0)
           arr[tmp] *= -1;
   })
   nums.forEach((val, ind) => {
       if (val > 0)
           res.push(ind + 1)
   })
   return res
};

//t1
/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var findDisappearedNumbers = function(nums) {
   let result=[]
   for(let i=0; i<nums.length; i++){
       let n =Math.abs(nums[i])
       let idx= n-1
       nums[idx]=Math.abs(nums[idx])*-1 //sholud keep the original value ->negative
   }
   
   nums.forEach((e,i)=>{
       if(e>0){
           result.push(i+1)
       }
   })
   return result;
};