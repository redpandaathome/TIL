//https://www.codewars.com/kata/530e15517bc88ac656000716/train/javascript

function rot13(message){
   let result=''
   let alphabet='abcdefghijklmnopqrstuvwxyz'
   message.split('').forEach(e=>{
     if(e.match(/[a-zA-Z]/)){
       let isUpper= e.toUpperCase()===e ? true:false;
       if(isUpper){
         e=e.toLowerCase();
       }
       let idx= (alphabet.indexOf(e)+13)%26
       result+= isUpper? (alphabet[idx]).toUpperCase():alphabet[idx]  
     } else {
       result+=e
     }
     
   })
   return result
 }


//1
function rot13(message) {
   let a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
   let b = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
   return message.replace(/[a-zA-Z]/gi, c => b[a.indexOf(c)])
 }


//2
let alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
let cipher   = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM";

function rot13(message){
  return message.split('').map(function(c) {
    let i = alphabet.indexOf(c);
    if (i < 0) {
      // not in alphabet, return char
      return c;
    }
    
    return cipher[i];
  }).join('');
}