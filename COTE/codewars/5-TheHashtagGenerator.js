//https://www.codewars.com/kata/52449b062fb80683ec000024/solutions/javascript

//Primitives in JavaScript: You Can’t Change Index[0] of a String 😮😮😮
//https://medium.com/@lainakarosic/primitives-in-javascript-you-cant-change-index-0-of-a-string-e6f340fb4f19
//trim() can't fix inside sentence like 'hi     stranger'
// slice https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice
// splice https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice
// .slice(1,arr[i].length) => .slice(1)
function generateHashtag (str) {
   if(str.trim().length<1){
     return false
   }
   let arr = str.trim().split(" ");
   let result='#';
   for(let i=0; i<arr.length; i++){
     if(arr[i].length<1)continue
     let temp = arr[i][0].toUpperCase()+arr[i].slice(1,arr[i].length)
     result+=temp
   }
   if(result.length>140){
     return false
   }
   return result
 }


// careful str.split("") => [' ', ' ',...], str.split(" ") => ['', '', ...]
// charAt
// using map for just forEach but making result on the side!
function generateHashtag (str) {
   var hash = '#';
   str.split(' ').map(a => {
     hash += a.charAt(0).toUpperCase() + a.slice(1);
   });
   return hash != '#' && hash.length <= 140 ? hash : false;
 }