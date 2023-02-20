//https://www.codewars.com/kata/545cedaa9943f7fe7b000048/solutions/javascript

function isPangram(string){
   let countObj = {}
   let count=0
   let arr = string.split("").filter(e=>e!==" ")
 
   arr.forEach(v=>{
 //     console.log("countObj[",v,"]", countObj[v])
     if(countObj[v]==null){
       countObj[v]=0
       count+=1
     }
   })
   return count>=26? true : false
 }

 //Improved...1 .every(x=>)
 //The every() method tests whether all elements in the array pass the test implemented by the provided function. It returns a Boolean value.
 //https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/every
 function isPangram(string){
   string = string.toLowerCase();
   return "abcdefghijklmnopqrstuvwxyz".split("").every(function(x){
     return string.indexOf(x) !== -1;
   });
 }

 // 1-2 my version
 function isPangram(string){
  return 'abcdefghijklmnopqrstuvwxyz'.split('').every(x=>string.toLowerCase().split('').includes(x))
}

 // Improved...2 every((x)=>~.includes(x))
 function isPangram(string){
  return 'abcdefghijklmnopqrstuvwxyz'
  .split('')
  .every((x) => string.toLowerCase().includes(x));
}

// [...'strinnnng]=> ['s','t',...,'g']
function isPangram(string) {
   const alphabetList = [...'abcdefghijklmnopqrstuvwxyz'];

   return alphabetList.every((letter) => string.toLowerCase().includes(letter));
 }

 //✨g modifier: global. All matches (don't return on first match)
 //✨i modifier: insensitive. Case insensitive match (ignores case of [a-zA-Z])
 //✨ size for set is not length! set.size
 //✨ declaring set with array new Set([...arr])
 function isPangram(string) {
   return new Set(string.toLocaleLowerCase().replace(/[^a-z]/gi, '').split('')).size === 26;
 }