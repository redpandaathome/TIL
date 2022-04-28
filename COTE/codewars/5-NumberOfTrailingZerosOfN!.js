// https://www.codewars.com/kata/52f787eb172a8b4ae1000a34/train/javascript
//[ ] 🏃🏻‍♀️🏃🏻‍♀️🏃🏻‍♀️ recursive...
// figuring out the rule...5, 10(2*5), 15(3*5), 20(4*5), 25(5*5 !!!), 30(5*6), ...

function zeros (n) {
   let cnt=0
   if(n==0)return 0
   let div = countDivForFive(n);
   while(div>0){
     cnt+=div
     div=countDivForFive(div)
   }
   return cnt
 }
 
 function countDivForFive(n){
   return Math.floor(n/5)
 }


//s1
function zeros (n) {
   var zs = 0;
   while(n>0){
     n=Math.floor(n/5);
     zs+=n
   }
   return zs;
 }

//s2
function zeros(n) {
   return n/5 < 1 ? 0 : Math.floor(n/5) + zeros(n/5);
 }