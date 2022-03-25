// https://leetcode.com/problems/longest-common-prefix/submissions/

/**
 * @param {string[]} strs
 * @return {string}
 */
 var longestCommonPrefix = function(strs) {
   let prefix = ""
   let sortedArr = strs.sort((a,b)=> a.length-b.length);
   let standardStr = sortedArr[0]
   let index=0
   for(let i=0; i< standardStr.length; i++){
       let cur = standardStr[i]
       // console.log("standardStr:",standardStr, "cur:",cur)
       for(let j=1; j<sortedArr.length; j++){
           let compareStr = sortedArr[j]
           // console.log("compareStr[",i,"]:", compareStr[i], ", cur:", cur)
           if(cur != compareStr[i]){
               return standardStr.slice(0,index)
           }
       }
       index=i+1
       // console.log("IDX:",index)
   }
   return standardStr.slice(0,index)
};