// https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/

/**
 * @param {number[]} nums
 * @return {number}
 */
//splice(start,numbers)
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
//splice(start,end,...(new Set(nums)))
var removeDuplicates = function(nums) {
   nums.splice(0,nums.length,...(new Set(nums)))
};

//2nd try[💦] - importance of understanding requirements in details... 🤨
//[ ]
/**
 * @param {number[]} nums
 * @return {number}
 */
 var removeDuplicates = function(nums) {
    let cnt=0
    for(let i=0; i< nums.length; i++){
        if(nums[i]==nums[i+1]){
            continue
        }
        nums[cnt]=nums[i]
        cnt+=1
    }
    return cnt
};

//using ++i
var removeDuplicates = function(nums) {
    let i = 0;
    for (let j = 0; j < nums.length; j++) {
        if (nums[j] != nums[i]) 
            nums[++i] = nums[j];
    }
    return ++i;
};