// https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1167/
//✨✨✨
// careful with .fill -> push ->will have impact on all filled units
// new Array(m+n-1).fill(0).map(e=>[])
// change direction with key !
// arr.flat()
/**
 * @param {number[][]} mat
 * @return {number[]}
 */
 var findDiagonalOrder = function(mat) {
   let m=mat.length
   let n=mat[0].length
   let result = new Array(m+n-1).fill(0).map(e=>[])
   
   for(let i=0; i<m; i++){
       for(let j=0; j<n; j++){
           let key=i+j
           if(key%2===0){
               //upward
               result[key].unshift(mat[i][j])
           } else {
               //downward
               result[key].push(mat[i][j])
           }
       }
   }
   return result.flat();
};