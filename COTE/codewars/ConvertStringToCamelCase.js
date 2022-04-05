//https://www.codewars.com/kata/517abf86da9663f1d2000003/solutions/javascript
// str.replace(regExp, function)

function toCamelCase(str){
   let arr = str.split("")
   if(arr.indexOf("-")!=-1 || arr.indexOf("_")!=-1){
     let changeNext=false;
     arr = arr.map((e,i)=>{
       if(e=='-'||e=='_'){
         changeNext=true;
         return
       } else if(changeNext){
         changeNext=false;
         return e=e.toUpperCase()
       } else {
         return e;
       }
     })
   }
    
    console.log(arr.join(""))
    return arr.join("")
  }


//IMPROVED
//NEED TO STUDY REGEX
function toCamelCase(str){
   var regExp=/[-_]\w/ig;
   return str.replace(regExp,function(match){
         return match.charAt(1).toUpperCase();
    });
}