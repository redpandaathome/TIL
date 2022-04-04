// 😱
// [ ]
//https://leetcode.com/problems/implement-strstr/

/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
 var strStr = function(haystack, needle) {
   if(needle.length>haystack.length){
       return -1;
   }
   let haystackArr = haystack.split('')
   let needleArr = needle.split('')
   
   //one by one in haystack
   //find first matching one
   //if not matching before all matching in needle... -1
   for(let i=0; i<haystackArr.length; i++){
       let cur = haystackArr[i];
       let targetLength = needleArr.length;
       let startingI = i;
       for(let j=0; j<needleArr.length; j++){
           let el = needleArr[j];
           if(cur==el){
               console.log("i&j:",i,j)
               targetLength-=1;
               i+=1;
               cur = haystackArr[i];
               if(targetLength==0){
                   return startingI;
               }
           } else {
               i=startingI;
               break;
           }
       }
   }
   return -1;
// "babbb bbab b"
//       "bbab"
};

//IMPROVED VERSION 🎃
var strStr = function(haystack, needle) {
    
   const haySplit = haystack.split(needle)
   
   if(needle === '') return 0
   if(haySplit.length === 1) return -1
   
   return haySplit[0].length 
   
};