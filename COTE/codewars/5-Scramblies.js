//https://www.codewars.com/kata/55c04b4cc56a697bb0000048/train/javascript

//key does not exist..? obj1[key]==undefined
function scramble(str1, str2) {
   let obj1= countChar(str1)
   let obj2= countChar(str2)
   for (let c in obj2){
     if(obj1[c]==undefined || obj2[c]>obj1[c]){
       return false
     }
   }
    return true
  }
  
  function countChar(str){
    let obj={}
    str.split('').forEach(e=>{
     if(e in obj){
       obj[e]+=1
     }else {
       obj[e]=1
     }
   })
    return obj;
  }
  

//1
//reduce((obj,cu)=>{...blah blah return obj},{})
//return arr.every(...)
// --undefined>=0 false... 
function scramble(str1, str2) {
   let frequency = str1.split('').reduce((ac,cu)=>{
     ac[cu]?ac[cu]++ : ac[cu]=1;
     return ac
   },{})
  
   return str2.split('').every(c=>{
     console.log(c,frequency[c] )
     return --frequency[c]>=0
   })
  }
  