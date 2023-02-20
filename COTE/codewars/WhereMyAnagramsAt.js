// https://www.codewars.com/kata/523a86aa4230ebb5420001e1/solutions/javascript

// comparing object(shallow)... 
// trying to sort objects... -> nah...
function anagrams(word, words) {
   let standard = counter(word)
   console.log("===",standard)
   let result=[]
   for (let i=0; i<words.length; i++){
     console.log("CHECKING:", words[i])
     if(shallowEqual(standard, counter(words[i]))){
       console.log("pushing...", words[i])
       result.push(words[i])
     }
   }
   return result
 }
 function shallowEqual(o1, o2){
   let key1=Object.keys(o1)
   let key2=Object.keys(o2)
   if(key1.length!==key2.length){
     return false
   }
   for (let key of key1){
     if(o1[key]!== o2[key]){
       return false
     }
   }
   return true
   
 }
 function counter(word){
 
   let newObj = {}
   for(let i=0; i<word.length;i++){
     if(newObj[word[i]]==null){
       newObj[word[i]]=1
     } else {
       newObj[word[i]]+=1
     }
   }
   return newObj
 }


//Improved 
String.prototype.sort = function() {
   return this.split("").sort().join("");
 };
 
 function anagrams(word, words) {
   return words.filter(function(x) {
       return x.sort() === word.sort();
   });
 }

//same but shorter
function anagrams(word, words) {
   word = word.split('').sort().join('');
   return words.filter(function(v) {return word == v.split('').sort().join('');});
 }

 //my version
 function anagrams(word, words) {
   let standard = word.split('').sort().join('')
   return words.filter(w=>w.split('').sort().join('')===standard)
 }