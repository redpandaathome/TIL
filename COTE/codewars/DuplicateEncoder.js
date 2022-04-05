// map(el,index,arr✨)
// arr.lastIndexOf(el)

//https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/solutions

//mine
function duplicateEncode(word){
   // ...
   word=word.toLowerCase();
   let arr = word.split('')
   let dupArr = arr.filter((e,i)=>arr.indexOf(e)!=i)

   let newArr = []
   let dup=")"
   let sing="("
   arr.forEach((e)=>{
     if(dupArr.indexOf(e)!= -1){
       newArr.push(dup)
     } else {
       newArr.push(sing);
     }
   })

 return newArr.join("")
}


//better
function duplicateEncode(word){
   return word
     .toLowerCase()
     .split('')
     .map( function (a, i, w) {
       return w.indexOf(a) == w.lastIndexOf(a) ? '(' : ')'
     })
     .join('');
 }