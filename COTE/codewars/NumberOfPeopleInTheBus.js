//https://www.codewars.com/kata/5648b12ce68d9daa6b000099/solutions/javascript

var number = function(busStops){
   // Good Luck! thankyou
   let onArr=[]
   let offArr=[]
   busStops.forEach((bus,i)=>{
     bus.forEach((stop,stopIdx)=>{
       if(stopIdx%2==0){
         onArr.push(stop) 
       } else{
         offArr.push(stop)
       }
     })
   })
   let onCnt = onArr.reduce((a,b)=>a+b);
   let offCnt = offArr.reduce((a,b)=>a+b);
   return onCnt-offCnt
 }

 //Improved - reduce initial value(third param!), [on,off]
 var number = function(busStops){
   //ex: [[10,0],[3,5],[5,8]]
   return busStops.reduce((sum,cur)=>{
     let [on, off]=cur;
     return sum+on-off
   },0)
 }

 //shorter
 const number = (busStops) => busStops.reduce((rem, [on, off]) => rem + on - off, 0);