// https://www.codewars.com/kata/520446778469526ec0000001/solutions/javascript/me/best_practice

Array.prototype.sameStructureAs = function (other) {
   // Return 'true' if and only if 'other' has the same
   // nesting structure as 'this'.

   // Note: You are given a function isArray(o) that returns
   // whether its argument is an array.
 if(!isArray(this) || !isArray(other)){
   return false
 }
 if(this.length !== other.length){
   return false
 }
 for(let i=0; i<this.length; i++){
   // not an array
   if(isArray(this[i])!==isArray(other[i])) return false
   //array
   if(isArray(this[i])){
     return this[i].sameStructureAs(other[i])
   }
 }
 return true
};


// improved?
Array.prototype.sameStructureAs = function (other) {
   return (this.length === other.length) ? this.every(function(el, i){
     return Array.isArray(el) ? el.sameStructureAs(other[i]) : true;
   }) : false;
};