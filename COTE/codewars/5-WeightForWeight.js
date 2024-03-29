//https://www.codewars.com/kata/55c6126177c9441a570000cc/solutions/javascript

//sort localeCompare
function orderWeight(string) {
   if(string.length<1){
     return ''
   }
   let arr =string.split(" ");
   let arr2=[]
   arr.forEach((e,i)=>{
     let temp = e.split("").reduce((ac,cu)=>parseInt(ac)+parseInt(cu))
     arr2.push([e,temp])
   })
   
   arr2.sort((a,b)=>{
     let a1=parseInt(a[1])
     let b1=parseInt(b[1])
     return a1===b1?a[0].localeCompare(b[0]):a1-b1
   })
   let resultArr=[]
   arr2.forEach(e=>resultArr.push(e[0]))
   return resultArr.join(" ")
 }

//1
function orderWeight(strng) {
   const sum = (str)=>str.split('').reduce((sum,el)=>(sum+(+el)),0);
    function comp(a,b){
      let sumA = sum(a);
      let sumB = sum(b);
      return sumA === sumB ? a.localeCompare(b) : sumA - sumB;
     };
   return strng.split(' ').sort(comp).join(' ');
  }


//2023.02.20
//✨ string sort... return str1.localeCompare(str2)
// num sort return a-b
function orderWeight(string) {
  let arr = string.trim().split(" ").map(e=>e.trim())
  let newArr = []
  arr.map(e=>{
    let sum = e.split("").reduce((acc,cur)=>
      parseInt(acc)+parseInt(cur)
    , 0)
    newArr.push([e, sum])
    return sum
  })

newArr.sort((a,b)=>{
  if(a[1]===b[1]){
    return (''+a[0]).localeCompare(''+b[0])
  }
  return a[1]-b[1]
})
let result = newArr.map(e=>e[0])

return result.join(' ')
}