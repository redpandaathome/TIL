// 💩 try again...
// https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

function minimumBribes(q) {
   // Write your code here
   let bribes = 0;
   let isChaotic = false
   
   for(let i = 0; i< q.length; i++){
       let currentVal = q[i];
       let originalVal = i+1
       if(currentVal - originalVal >2){
           isChaotic = true;
           break;
       } 
       //✨✨✨
       for(let j =Math.max(0, currentVal-2); j<i; j++){
           if(q[j]>q[i]){
               bribes++;
           }
       }
   }
   
   if(isChaotic){
       console.log("Too chaotic")
   } else {
       console.log(bribes)
   }
}
