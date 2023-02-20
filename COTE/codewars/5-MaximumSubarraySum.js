//https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/solutions/javascript

var maxSequence = function(arr){
   let maxSum=-Infinity;
   let n=0
   while(n<arr.length){
     n+=1
     for(let i=0; i<arr.length;i++){
     let sum=0
       for(let j=i; j<i+n; j++){
         if(j<arr.length){
           sum+=arr[j]
         } else {
           break
         }
       }
       maxSum=Math.max(maxSum, sum)
     }
   }
   return maxSum>0?maxSum:0
 }

//Kadane's algorithm(Dynamic Programming) ✨✨✨
//https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d
var maxSequence = function(arr){
   let localMax=0
   let globalMax=0
   for(let i=0; i<arr.length; i++){
     localMax=Math.max(arr[i], arr[i]+localMax)
     if(localMax>globalMax){
       globalMax=localMax
     }
   }
  return globalMax
 }


//1
var maxSequence = function(arr){
   var min = 0, ans = 0, i, sum = 0;
   for (i = 0; i < arr.length; ++i) {
     sum += arr[i];
     min = Math.min(sum, min);
     ans = Math.max(ans, sum - min);
   }
   return ans;
 }

//2
var maxSequence = function(arr){
   var currentSum = 0;
   return arr.reduce(function(maxSum, number){
       currentSum = Math.max(currentSum+number, 0);
       return Math.max(currentSum, maxSum);
   }, 0);
}

//3
var maxSequence = function(arr){
   var max = 0;
   var cur = 0;
   arr.forEach(function(i){
     cur = Math.max(0, cur + i);
     max = Math.max(max, cur);
   });
   return max;
 }