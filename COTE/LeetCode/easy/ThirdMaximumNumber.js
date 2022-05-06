//https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3231/

/**
 * @param {number[]} nums
 * @return {number}
 */
 var thirdMax = function(nums) {
   let arr= [...new Set(nums)].sort((a,b)=>a-b)
   let result = arr.length<3 ? arr[arr.length-1]:arr[arr.length-3]
   return result
};

//Interesting!
//Time and space complexity of Set()??
//https://www.reddit.com/r/learnjavascript/comments/n1j7ub/time_and_space_complexity_of_set/
// new set o(n), sort logN
/**
 * @param {number[]} nums
 * @return {number}
 */
 var thirdMax = function(nums) {
   let max = -Infinity;
   let mid = -Infinity;
   let min = -Infinity;
   
   for (x of nums) {
     if (x > max) {
       min = mid;
       mid = max;
       max = x;
     }  else if (x > mid  && x < max) {
       min = mid;  
       mid = x;
     } else if (x > min && x < mid) {
       min = x;
     }
   }
   
   return (min > -Infinity) ? min : max;
   
 };