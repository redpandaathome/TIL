//https://www.codewars.com/kata/52774a314c2333f0a7000688/train/javascript

function validParentheses(parens) {
   let cnt=0
   for(let i=0;i<parens.length; i++) {
     if(parens[i]=='('){
       cnt+=1
     }else{
       cnt-=1
     }
     if(cnt<0){
       return false
     }
   }
   return cnt==0?true:false;
 }