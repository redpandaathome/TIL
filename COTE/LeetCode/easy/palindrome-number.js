/**
 * @param {number} x
 * @return {boolean}
 */
 var isPalindrome = function(x) {
   let strNum = x.toString()
   let strLeng = strNum.length
   let right;
   if(strNum.slice(0,1)=='-1')return false

   let midNum = Math.floor(strLeng/2)
   let left = strNum.slice(0,midNum)

   if(strLeng%2==0){
       right=strNum.slice(midNum, strLeng)
   } else {
       right=strNum.slice(midNum+1, strLeng)
   }

   let reversedRight = reverse(right)

   if(left==reversedRight){
       return true
   } else {
       return false
   }
}

function reverse(s){
console.log(s.split(""))
return s.split("").reverse().join("");
}