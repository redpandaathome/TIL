// https://www.codewars.com/kata/514a024011ea4fb54200004b/solutions/javascript/all/best_practice
// regex https://www.youtube.com/watch?v=t3M6toIflyQ

function domainName(url){
   //your code here
   const regex = /(?:https?:\/\/)?(?:www\.)?([a-zA-Z0-9-]+)(?:\.?)/;
   return url.match(regex)[1]
 }

//regex...✨
//https://github.com/dream-ellie/regex
//https://regexr.com/5mhou
// Improved1
function domainName(url){
   url = url.replace("https://", '');
   url = url.replace("http://", '');
   url = url.replace("www.", '');
   return url.split('.')[0];
 };

// Improved2
function domainName(url){
   return url.match(/(?:http(?:s)?:\/\/)?(?:w{3}\.)?([^\.]+)/i)[1];
 }