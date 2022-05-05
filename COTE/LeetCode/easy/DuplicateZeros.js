//https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3245/

/**
 * @param {number[]} arr
 * @return {void} Do not return anything, modify arr in-place instead.
 */
 var duplicateZeros = function(arr) {
   let num=arr.length;
   for(let i=0;i<num;i++){
       if(arr[i]===0){
           arr.splice(i,0,0)
           i++
       }
   }
   arr.splice(num)
};


//intersting - using pop
/**
 * @param {number[]} arr
 * @return {void} Do not return anything, modify arr in-place instead.
 */
 var duplicateZeros = function(arr) {
    for (i = 0; i < arr.length; i++) {
        if (arr[i] == 0) {
            arr.splice(i, 0, 0);
            arr.pop();
            i++;
        }
    }
};