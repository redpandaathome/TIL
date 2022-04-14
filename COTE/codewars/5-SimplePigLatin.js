// https://www.codewars.com/kata/520b9d2ad5c005041100000f/solutions/javascript
// /[.,:!?]/.test(detailArr[i])
// str.substring(0,3)

function pigIt(str){
   let result=''
   str.split(' ').forEach(c=>{
     let detailArr=c.split('')
     let temp=''
     let tail=''
     for(let i=0; i<detailArr.length; i++){
       if(/[.,:!?]/.test(detailArr[i])){
         temp+=detailArr[i]
       } else if(i==0){
         tail=detailArr[i]+'ay'
       } else {
         temp+=detailArr[i]    
       }
     }
     result+= (temp+tail+" ")
   })
   return result.substring(0, result.length-1)
 }

// Improved1
function pigIt(str){
   return str.replace(/(\w)(\w*)(\s|$)/g, "\$2\$1ay\$3")
 }

// Improved2
function pigIt(str) {
   return str.replace(/\w+/g, (w) => {
     return w.slice(1) + w[0] + 'ay';
   });
 }

 // tip... charAt(index)