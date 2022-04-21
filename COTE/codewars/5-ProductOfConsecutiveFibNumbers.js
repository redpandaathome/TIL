//https://www.codewars.com/kata/5541f58a944b85ce6d00006a/train/javascript

function productFib(prod){
   let arr=[0,1]
   let a=arr[arr.length-2]
   let b=arr[arr.length-1]
   while(prod>=a*b){
     if(a*b==prod){
       return [a,b,true]
     }
     arr=findFib(arr)
     a=b
     b=arr[arr.length-1]
   }
   return [a, b, false]
 }
 
 function findFib(arr){
   let temp =arr[arr.length-2]+arr[arr.length-1]
   arr.push(temp)
   return arr;
 }

//1
function productFib(prod){
   var n = 0;
   var nPlus = 1;  
   while(n*nPlus < prod) {
     nPlus = n + nPlus;
     n = nPlus - n;
   }
   return [n, nPlus, n*nPlus===prod];
 }

//2
function productFib(prod){
   let [a, b] = [0, 1];
   while(a * b < prod) [a, b] = [b, a + b];
   return [a, b, a * b === prod];
 }