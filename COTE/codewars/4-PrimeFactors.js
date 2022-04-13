// 🧐🧐🧐
// []
// https://www.codewars.com/kata/54d496788776e49e6b00052f/solutions/javascript

function sumOfDivided(lst) {
   //your code
   //find prime Number list under the biggest number
   //find factors -> sort -> {2:[12], 3:[15]}
   let allPrimes=[]
   lst.forEach((el)=>{
     let primeList = findPrime(el);
     allPrimes.push(...primeList)
   })
 
   allPrimes= Array.from(new Set(allPrimes))
   let result=[]
   allPrimes.forEach((p)=>{
     let sum=0
     lst.forEach(el=>{
       if(el%p==0){
         sum+=el
       }
     })
     result.push([p, sum])
   })
   return result.sort((a,b)=>a[0]-b[0])
 }
 
 function findPrime(n){
   n=Math.abs(n)
   const factors = []
   let divisor =2
   while(n>=2){
     if(n%divisor==0){
       factors.push(divisor)
       n=n/divisor;
     } else {
       divisor+=1
     }
   }
   return factors;
 }


//solution1
function sumOfDivided(lst) {
   var max = Math.max(...lst.map(x => Math.abs(x))),
       isPrime = x => {
         for(var i = 2; i*i<=x; i++) if (x%i === 0) return false;
         return true;
       };
   var sums = {};
   for (var i = 2; i<=max; i++) if (isPrime(i)) {
     lst.forEach(x => {
       if (x%i === 0) sums[i] = x + (sums[i]||0);
     });
   }
   return Object.keys(sums).map(i => [+i, sums[i]]);
 }

//my trial1
//✨ checking prime number - i*i<=x... "="
// let(i=2; i<=max...) "="
// Math.max(...arr)
// let func1 = x=> {}
// sum[i]=(sum[i]||0)+a
// Object.keys(obj)=>map(i=>...)
function sumOfDivided(lst) {
  let max = Math.max(...lst.map(x=>Math.abs(x))),
      isPrime = x=> {
        for(let i=2; i*i<=x; i++) if (x%i===0)return false;
        return true;
      };
  let sums={};
  for(let i=2; i<=max; i++) if(isPrime(i)){
    lst.forEach(x=>{
      if(x%i===0) sums[i] = (sums[i]||0)+x;
    })
  }
  return Object.keys(sums).map(i=>[+i, sums[i]])
}
 