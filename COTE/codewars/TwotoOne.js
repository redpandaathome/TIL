// https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/javascript
// to combine arrays... arr1.concat(arr2)

function longest(s1, s2) {
   // your code
   let newArr = s1.split('').concat(s2.split(''))
   newArr=Array.from(new Set(newArr))
 
   return newArr.sort().join("")
 }


 //improved... Set(a+b)
 const longest = (s1, s2) => [...new Set(s1+s2)].sort().join('')