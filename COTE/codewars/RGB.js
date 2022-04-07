//https://www.codewars.com/kata/513e08acc600c94f01000001/solutions/javascript

function rgb(r, g, b){
   // complete this function  
   r=changeTo16(checkRange(r))
   g=changeTo16(checkRange(g))
   b=changeTo16(checkRange(b))
   return (r+g+b).toUpperCase()
 }
 
 function changeTo16(n){
   let result = n.toString(16);
   result = result.length<2 ? '0'+result : result
   return result;
 }
 
 function checkRange(s){
   s= s<0? 0 : s
   s= s>255? 255:s
   return s
 }

 //IMPROVED... 1
 // arr.slice(-2) -> gets two last items!
 function rgb(r, g, b){
   return toHex(r)+toHex(g)+toHex(b);
 }
 
 function toHex(d) {
     if(d < 0 ) {return "00";}
     if(d > 255 ) {return "FF";}
     return  ("0"+(Number(d).toString(16))).slice(-2).toUpperCase()
 }

 //2 -> min max range ✨
 function rgb(r, g, b){
  return [r,g,b].map(function(x) {
   return ('0'+Math.max(0, Math.min(255, x)).toString(16)).slice(-2);
 }).join('').toUpperCase();
}

//cleanest
function rgb(r, g, b){
   function toHex(a) { 
     if (a <= 0) return '00';
     else if (a >= 255) return 'FF';
     else return a.toString(16).toUpperCase();
   }
   return toHex(r) + toHex(g) + toHex(b);
 }