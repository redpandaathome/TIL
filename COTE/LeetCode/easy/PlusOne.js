//big number doesn't keep it's precise value... hmmm
   // let str= digits.reduce((ac,cu)=>ac+cu,'')
   // console.log("str:",str,BigInt(str))
   // return (BigInt(str)+1).toString().split('')

//s1 !
//for loop range ;i>0 && digits[i]===10;
/**
 * @param {number[]} digits
 * @return {number[]}
 */
 var plusOne = function(digits) {
   const last = digits.length-1;
   digits[last]++;
   for(let i=last; i>0 && digits[i]===10; i--){
       digits[i]=0
       digits[i-1]++;
   }
   if(digits[0]===10){
       digits[0]=0
       digits.unshift(1)
   }
   return digits;
};