//https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1144/

/**
 * @param {number[]} nums
 * @return {number}
 */
 var pivotIndex = function(nums) {
   let pivot=0
   while(pivot<nums.length){
       let leftSum=sumArray(nums.slice(0,pivot))
       let rightSum=sumArray(nums.slice(pivot+1,nums.length))
       
       if(leftSum===rightSum){
           return pivot;
       }
       pivot++;
   }
   return -1;
};
   
function sumArray(arr){
   if(arr.length<1)return 0
   return arr.reduce((ac,cu)=>ac+cu)
}

//simpler version, calc total sum and deduct with every new num[i]
/**
 * @param {number[]} nums
 * @return {number}
 */
 var pivotIndex = function(nums) {
   let leftSum=0
   let sum = nums.reduce((ac,cu)=>ac+cu,0)
   for(let i=0; i<nums.length;i++){
       leftSum+=nums[i]
       if(leftSum===sum-leftSum+nums[i])return i;
   }
   return -1;
};