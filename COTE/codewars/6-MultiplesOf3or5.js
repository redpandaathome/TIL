//https://www.codewars.com/kata/514b92a657cdc65150000006/solutions/javascript/me/best_practice

function solution(number){
   let result = []
   result = check35(number);
   return result.reduce((ac,cu)=>ac+cu, 0)
 }
 
 function check35(n){
   let result=[]
   for(let i=1;i<n;i++){
     if(i%3==0 || i%5==0){
       result.push(i)
     }
   }
   return result
 }


// simpler
function solution(number){
   var sum = 0;
   
   for(var i = 1;i< number; i++){
     if(i % 3 == 0 || i % 5 == 0){
       sum += i
     }
   }
   return sum;
 }