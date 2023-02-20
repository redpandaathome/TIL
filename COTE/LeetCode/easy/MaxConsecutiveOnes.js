//https://leetcode.com/explore/featured/card/fun-with-arrays/521/introduction/3238/

/**
 * @param {number[]} nums
 * @return {number}
 */
 var findMaxConsecutiveOnes = function(nums) {
   let cnt=0
   let maxCnt=0
   let isOn=false
   for(let i=0;i<nums.length;i++){
       if(isOn && nums[i]===1){
           cnt++
       } 
       if(!isOn && nums[i]===1){
           isOn=true
           cnt++
       }
       if(isOn && nums[i]!==1){
          isOn=false
           maxCnt=Math.max(maxCnt,cnt)
           cnt=0
       }
       continue
   }
   maxCnt=Math.max(maxCnt, cnt)
   return maxCnt
};


// s1 The standard traversal:
// ✨ for (let el of arr){}
var findMaxConsecutiveOnes = function(nums) {
    let max = 0, curr = 0;
    for (let k of nums) {
        max = Math.max(max, curr += k);
        if (!k) curr = 0;
    }
    return max;
};


//Some one-liners:
var findMaxConsecutiveOnes = function(nums) {
    return nums.join('').split('0').reduce((max, ones) => Math.max(max, ones.length), 0);
};
var findMaxConsecutiveOnes = function(nums) {
    return Math.max(...nums.join('').split('0').map(ones => ones.length));
};
