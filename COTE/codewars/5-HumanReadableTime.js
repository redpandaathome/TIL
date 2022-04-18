
//https://www.codewars.com/kata/52685f7382004e774f0001f7/solutions/javascript

function humanReadable (seconds) {
   let second = (seconds%60)<10? '0'+(seconds%60):(seconds%60);
   let temp = (seconds-second)/60
   let min = (temp%60)<10? '0'+(temp%60):(temp%60);
   temp=temp-min;
   let hour = (temp/60)<10? '0'+(temp/60):(temp/60);
   
   return hour+":"+min+":"+second;
 }

//
function humanReadable(seconds) {
   var pad = function(x) { return (x < 10) ? "0"+x : x; }
   return pad(parseInt(seconds / (60*60))) + ":" +
          pad(parseInt(seconds / 60 % 60)) + ":" +
          pad(seconds % 60)
 }