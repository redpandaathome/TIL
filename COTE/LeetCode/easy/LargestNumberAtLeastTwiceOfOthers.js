/**
 * @param {number[]} nums
 * @return {number}
 */
 var dominantIndex = function(nums) {
   let maxNum = nums.reduce((m,cu,i)=>Math.max(m, cu))
   let idx= -1;
   for(let i=0; i<nums.length;i++){
       if(nums[i]==maxNum){
           idx=i;
           continue   
       }
       if(nums[i]*2>maxNum)return -1
   }
   return idx;
};