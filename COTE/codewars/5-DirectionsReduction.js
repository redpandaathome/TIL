//https://www.codewars.com/kata/550f22f4d758534c1100025a/solutions/javascript

function dirReduc(arr){
   while(true){
     let resetCheck=false;
     for(let i=1; i<arr.length;i++){
     let curIdx=i-1;
       if(isOp(arr[curIdx], arr[i])){
         arr=arr.slice(0,i-1).concat(arr.splice(i+1, arr.length))
         resetCheck=true;
         break
       }
     }
     if(!resetCheck){
       break
     }
   }
   return arr
 }
 
 function isOp(a,b){
   if((a=='SOUTH' && b=='NORTH') || (b=='SOUTH' && a=='NORTH') || (a=='WEST' && b=='EAST') || (a=='EAST' && b=='WEST')){
     return true
   }
   return false
 }

 
//s1
// use object & reduce from the back
function dirReduc(plan) {
   var opposite = {
     'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'};
   return plan.reduce(function(dirs, dir){
       if (dirs[dirs.length - 1] === opposite[dir])
         dirs.pop();
       else
         dirs.push(dir);
       return dirs;
     }, []);
 }

//trial1
function dirReduc(arr){
   const opposite = {
     "SOUTH":"NORTH", "EAST":"WEST", "NORTH":"SOUTH", "WEST":"EAST"
   }
   return arr.reduce((ac,cu)=>{
     if(opposite[cu]===ac[ac.length-1]){
       ac.pop();
     }else{
       ac.push(cu)
     }
     return ac;
   },[])
 }

//s2
// pattern.test(str), str.replace(pattern,''), str.match(/~/) ||[]
function dirReduc(arr) {
   var str = arr.join(''), pattern = /NORTHSOUTH|EASTWEST|SOUTHNORTH|WESTEAST/;
   while (pattern.test(str)) str = str.replace(pattern,'');
   return str.match(/(NORTH|SOUTH|EAST|WEST)/g)||[];
 }