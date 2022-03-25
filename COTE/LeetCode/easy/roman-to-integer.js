//https://leetcode.com/problems/roman-to-integer/submissions/
//Did not know Roman number system in details took lot of time 20 = XX not IIX

/**
 * @param {string} s
 * @return {number}
 */

 var romanToInt = function(s) {
   const sym= {
       "I":1,
       "V":5,
       "X":10,
       "L":50,
       "C":100,
       "D":500,
       "M":1000,
   }
   let ans=0
   for(let i=0; i<s.length; i++){
       let cur = s[i]
       
       if(i==s.length-1){
           ans+=sym[cur]
           break
       }
       
       let next = s[i+1]
       if (sym[cur]>=sym[next]){
           ans+=(sym[cur])
           // console.log("+ans:", ans)
       } else {
           temp = sym[next]-sym[cur]
           ans+=temp
           i++;
           // console.log("-ans:", ans)
           
       }
   }
   return ans
}

//Improved https://dev.to/urfan/leetcode-roman-to-integer-with-javascript-1g3n