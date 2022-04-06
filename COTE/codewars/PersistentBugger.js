//https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/javascript

function persistence(num) {
   //code me
  let arr=getArrFromNumb(num)
  let count=0;
  
  while(arr.length!=1){
    newVal = multiplyAll(arr)
    arr=getArrFromNumb(newVal)
    count+=1
  }
  return count
}

function getArrFromNumb(num){
  let result= num.toString().split('')
  return result
}
function multiplyAll(arr){
  let result= arr.reduce((pr,cu)=>{
    return parseInt(pr)*parseInt(cu)
  })
  return result
}

//IMPROVED1 - var! num>9 as condition in for loop, reduce!
function persistence(num) {
   //code me
  for(var i=0;num>9;i++){
    num=num.toString().split('').reduce((p,c)=>p*c);
  }
  return i
}

//IMPROVED2
function persistence(num) {
   //code me
  let count=0;
  while(num>9){
    num=num.toString().split('').reduce((p,c)=>p*c);
    count++;
  }

  return count
}