// https://www.codewars.com/kata/52597aa56021e91c93000cb0/solutions/javascript

function moveZeros(arr) {
   let count=0
   let newArr=[]
   arr.forEach((v,i)=>{
     if(v===0){
       count+=1
     }else{
       newArr.push(v)
     }
   })
   for(let i=0; i<count; i++){
     newArr.push(0)
   }
   return newArr
 }

 // improved 👀
 var moveZeros = function (arr) {
   return arr.filter(function(x) {return x !== 0}).concat(arr.filter(function(x) {return x === 0;}));
 }

 //same
 function moveZeros(arr) {
   return arr.filter(x=>x!==0).concat(arr.filter(x=>x===0))
 }

 // 2023.02.16
 function moveZeros(arr) {
  //count numbers of zeros
  let numsOfZero = arr.filter(e=>e===0).length;
  //filter zeros
  let tempArr = arr.filter(e=>e!==0)
  //add zeros ✨
  return tempArr.concat(Array(numsOfZero).fill(0))
}