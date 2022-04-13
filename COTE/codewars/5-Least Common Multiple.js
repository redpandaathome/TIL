// https://www.codewars.com/kata/5259acb16021e9d8a60010af/solutions/javascript
// [ ]

var lcm = function () {
   // TODO: Program me
   let arr =Array.from(arguments);
   let result = {}
   arr.forEach(e=>{
     let temp = primeCounter(e)
     console.log(e,temp)
     Object.keys(temp).forEach(o=>{
       o in result? result[o]=Math.max(result[o],temp[o]):result[o]=temp[o]
     })
   })
   return Object.keys(result).reduce((ac,cu)=>{
     return ac*Math.pow(cu,result[cu])},1)
 };
 
 function primeCounter(e){
   //6->{2:1, 3:1}
   let i=2;
   let factors={}
   while(i*i<=e){
     if(e%i!==0){
       i+=1
     }else{
       e=e/i
       i in factors? factors[i]+=1:factors[i]=1
     }
   }
   if(i>1){
       e in factors? factors[e]+=1:factors[e]=1
   }
   return factors;
 }

//...there is a rule for Greatest Common Divisor and Least Common Multiple
//apply...
var lcm = function () {
   function gcd(a,b) {
     if (a == 0) return b;
     return gcd(b%a, a);
   }
   return Array.prototype.slice.apply(arguments).reduce(function(a,b) {return a*b / gcd(a,b);}, 1);
 };


//
function lcm(...numbers) {
   return numbers.reduce((a, b) => Math.abs(a * b) / gcd(a, b));
 };
 
 function gcd(...numbers) {
   return numbers.reduce((a, b) => b === 0 ? a : gcd(b, a % b));
 }
