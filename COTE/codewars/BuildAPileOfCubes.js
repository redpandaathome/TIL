// https://www.codewars.com/kata/5592e3bd57b64d00f3000047/train/javascript

function findNb(m) {
   // your code
   let cur = 1;
   let sum =0;
   let temp=cur;
   while(sum<=m){
     let temp= cur**3
     sum+=temp;
     if(sum==m){
       return cur
     }
     cur+=1
   }
 return -1
}

// improved... using ('-') interesting...
function findNb(m) {
   var n = 0
   while (m > 0) m -= ++n**3
   return m ? -1 : n
 }

 // Math.pow(num,3)
 function findNb(m) {
   let n = 0;
   let sum = 0;
   while (sum < m) {
     n++;
     sum += Math.pow(n, 3);
   }
   return sum === m ? n : -1;
 }