//https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/

/**
 * @param {number[]} arr
 * @return {boolean}
 */
 var validMountainArray = function(arr) {
   if(arr.length<3)return false
   //check strictly increasing till k then ->
   let curI=0
   while(arr.length-2>curI){
       if(arr[curI]<arr[curI+1]){
           curI+=1
       } else if(arr[curI]==arr[curI+1]){
           return false
       } else {
           break
       }
   }
   if(curI==0)return false
   while(arr.length-1>curI){
       if(arr[curI]>arr[curI+1]){
           curI+=1
       } else {
           return false
       }
   }
   return true
};

//
const validMountainArray = A => {
   let i = 0;
   while (A[i + 1] > A[i]) { i++; }
   if (i === 0 || i === A.length - 1) { return false; }
   while (A[i] > A[i + 1]) { i++; }
   return i === A.length - 1;
};