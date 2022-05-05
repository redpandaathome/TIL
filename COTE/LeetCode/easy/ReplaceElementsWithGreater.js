//https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3259/

/**
 * @param {number[]} arr
 * @return {number[]}
 */
 var replaceElements = function(arr) {
   for(let i=0; i<arr.length-1; i++){
       arr[i]=Math.max(...arr.slice(i+1))
   }
   arr[arr.length-1]= -1;
   return arr
   
};

// !
const replaceElements = arr => {
   const result = new Array(arr.length);
   result[arr.length - 1] = -1;
   
   for (let i = arr.length - 1; i > 0; i -= 1) {
       result[i - 1] = Math.max(arr[i], result[i]);
   }
   
   return result;
};