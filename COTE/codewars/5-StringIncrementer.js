//https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/javascript
//isNaN(string), strng.substring(dIdx), strng.substring(0,dIdx)
function incrementString (strng) {
   let dIdx=strng.length
   strng.split('').every((e,i)=>{
     if(isNaN(e)) {
       return true
     }
     dIdx=i
     return false
   })
 
   if(dIdx==strng.length){
     return strng+'1'
   }else {
     let tempS =strng.substring(dIdx)
     let newTempS = (parseInt(tempS)+1).toString()
 
     if(tempS.length>newTempS.length){
       newTempS='0'.repeat(tempS.length-newTempS.length)+newTempS
     }
     let result = strng.substring(0,dIdx)+ newTempS
     return result
   }
   
 }

//1
//✨str.replace(/regexp/, function(match, group1, group2,...){return blah})
function incrementString(input) {
   if(isNaN(parseInt(input[input.length - 1]))) return input + '1';
   return input.replace(/(0*)([0-9]+$)/, function(match, p1, p2) {
     var up = parseInt(p2) + 1;
     return up.toString().length > p2.length ? p1.slice(0, -1) + up : p1 + up;
   });
 }

// 2
// var str = strng.replace(/[0-9]/gi,'');
// var num = strng.replace(/[^0-9]/gi,'');
function incrementString (strng) {
   var str = strng.replace(/[0-9]/gi,'');
   var num = strng.replace(/[^0-9]/gi,'');
   num++;
   var t = str + num;
   if((strng.length - t.length) ==2)
     str +='00';
   if((strng.length - t.length) ==1)
     str +='0';
   return str+num;
 }


//3
function incrementString (strng) {
   return strng.replace(/(\d*)$/, m => ((+m + 1) + '').padStart(m.length, '0'))
 }


//try!
function incrementString (strng) {
   let original = strng;
   let str = strng.replace(/[0-9]/gi,'');
   let num = strng.replace(/[^0-9]/gi,'');
   num++
 
   let result=str+num;
   if(result.length>=original.length){
     return result;
   } else if(result.length<original.length){
     return str+ '0'.repeat(original.length-result.length) + num
   }
 }