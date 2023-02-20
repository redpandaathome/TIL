//https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/solutions/javascript

function firstNonRepeatingLetter(s) {
   let arr = s.split('')
   if(arr.length==1){
     return arr[0]
   }
   for(let i=0; i<arr.length; i++){
     let right = arr.slice(i+1);
     let left = arr.slice(0,i);
     let lowChar = arr[i].toLowerCase();
     let upperChar = arr[i].toUpperCase();
     if(right.indexOf(lowChar)<0 && right.indexOf(upperChar)<0
       && left.indexOf(lowChar)<0 && left.indexOf(upperChar)<0){
       return arr[i]
     }
   }
   return ""
 }

//regexp... str.match(new RegExp(char, "gi")).length
function firstNonRepeatingLetter(s) {
   for(var i in s) {
     if(s.match(new RegExp(s[i],"gi")).length === 1) {
       return s[i];
     }
   }
   return '';
 }

// ✨ lastIndexOf !!
function firstNonRepeatingLetter(s) {
   var t=s.toLowerCase();
   for (var x=0;x<t.length;x++)
     if(t.indexOf(t[x]) === t.lastIndexOf(t[x]))
       return s[x];
   return "";
 }