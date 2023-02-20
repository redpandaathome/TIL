// https://www.codewars.com/kata/52c4dd683bfd3b434c000292/solutions/javascript
// Array.from(new Set(arr)) <- to make set to array
// 🔥🔥🔥🔥🔥

function isInteresting(number, awesomePhrases) {
   // Go to town!
   console.log("=========number:",number, awesomePhrases)
   for(let i=0; i<3; i++){
     let result = 0
     if(number>99){
       console.log("===i:",i, number)
       console.log("isAllZero(number):",isAllZero(number))
       
       if(isAllZero(number)||isIncrementing(number)||isDecrementing(number)||isPalindrome(number)||isAwesome(number, awesomePhrases)||isAllSame(number)){
         if(i==0) return 2
         return 1
       } 
     }
     number+=1
   }
   return 0
 }
 
 function isAllSame(number){
   let arr = Array.from(new Set(number.toString().split('')))
   if(arr.length===1){
     return true
   } 
   return false
 }
 function isAwesome(number, awesomePhrases){
   if(awesomePhrases.indexOf(number)!==-1){
     return true
   }
   return false
 }
 function isPalindrome(number){
   //even length-1, odd except floor(length/2)
   let arr=number.toString().split('')
   let firstEnd;
   let secondStart;
   if(number.length%2!==0){
     firstEnd = Math.floor(arr.length/2);
     secondStart = Math.floor(arr.length/2)+1;
   } else {
     firstEnd = arr.length/2;
     secondStart = arr.length/2; 
   }
   let first = arr.slice(0,firstEnd)
   let second = arr.slice(secondStart, arr.length)
   if(first.join('')===second.reverse().join('')){
      return true
   } 
   return false
 }
 
 function isDecrementing(number){
   let str = number.toString()
   if('9876543210'.indexOf(str)!==-1) return true
   return false
 }
 function isIncrementing(number){
   let str = number.toString()
   if('1234567890'.indexOf(str)!==-1) return true
   return false
 }
 function isAllZero(number){
   let arr =number.toString().split('')
   for(let i =1; i<arr.length; i++){
     if(arr[i]!=='0'){
       return false
     }
   }
   return true
 }



// Solution1
// arr.some() https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some
// The some() method tests whether at least one element in the array passes the tes
function isInteresting(number, awesomePhrases) {
   var tests = [
     function(n) { return /^\d00+$/.test(n); },
     function(n) { return /^(\d)\1+$/.test(n); },
     function(n) { return RegExp(n).test(1234567890); },
     function(n) { return RegExp(n).test(9876543210); },
     function(n) { return n + '' == (n + '').split('').reverse().join(''); },
     function(n) { return awesomePhrases.some(function(p) { return p == n; }); }
   ];
   
   var interesting = 0;
   tests.some(function(test) {
     if (number > 99 && test(number))
       return interesting = 2;
     else if ((number > 98 && test(number + 1)) || (number > 97 && test(number + 2)))
       interesting = 1;
   });
   return interesting;
 }


// trial1
// all same digit regex... /^(\d)\1+$/
// Regexp(var).test(n)
function isInteresting(number, awesomePhrases) {
   // Go to town!
   let tests = [
     //allZero
     (n)=>/^\d00+$/.test(n),
     //allSame
     (n)=>/^(\d)\1+$/.test(n),
     //incre
     (n)=>RegExp(n).test(1234567890),
     //decre
     (n)=>RegExp(n).test(9876543210),
     //palinddrome
     (n)=>n.toString()==n.toString().split('').reverse().join(''),
     //awesomePhrases
     (n)=>awesomePhrases.some(p=>p==n)
   ]
   
   let result=0
   tests.some(test=>{
     if(number>99&&test(number)) return result=2; //return ✨
     else if((number>98 && test(number+1)) || (number>97 && test(number+2)))result=1;
   })
   return result;
 }





// Solution2
const chars = n => n.toString().split('')
const match = s => n => new RegExp(n).test(s)
const regex = r => n => r.test(n)

const tests = [
  match('1234567890'),                  // incremental
  match('9876543210'),                  // decremental
  regex(/^\d0+$/),                      // all zeroes
  regex(/^(\d)\1+$/),                   // repeated
  n => n == chars(n).reverse().join('') // palindrome
]

const test = (n, xs) => n > 99 && 
  (xs.indexOf(n) > -1 || tests.map(t => t(n)).some(x => !!x))
  
const isInteresting = (n, xs) =>
  test(n, xs) ? 2 : +(test(n + 1, xs) || test(n + 2, xs))




//2023.02.16 💦💦💦
function isInteresting(number, awesomePhrases) {
  // Go to town!
  console.log("----------------------------------")
  console.log(number, awesomePhrases)
  if(number <98) return 0
  
  let arr = [number, (number+1), (number+2)]
  arr = arr.map((e,i)=>{
    if(e>99 && (isFollowedByAllZeros(e) || isEveryDigitSame(e) || isAwesomePhrases(e, awesomePhrases) || isIncrementing(e) || isDecrementing(e) || isPalindrome(e)) ){
      return true
    }
      
      return false
    
  })
  console.log(">>>:",arr)
  let result;
  if(arr[0]===true) result= 2
  else if(arr[1]===true || arr[2]===true) result= 1
  else result= 0
  console.log("result:",result)
  return result
}
function isFollowedByAllZeros(num){
  let arr = num.toString().split('').map(e=>parseInt(e));
  console.log(arr, ", length?", arr.length)
  for(let i=1; i<arr.length; i++){
    console.log("💛i:",i, ",arr[i]:", arr[i])
    console.log(typeof(arr[i]), arr[i])
    console.log(arr[i]!==0)
    if(arr[i]!==0){
      return false;
    }
  }
  console.log("1...returning true")
  return true;
}

function isEveryDigitSame(num){
  let arr = num.toString().split('').map(e=>parseInt(e));
  let theNum = arr[0];
  for(let i=1; i<arr.length; i++){
    if(arr[i]!==theNum)return false;
  }
  console.log("2...returning true, theNum:", theNum)
  
  return true;
}

function isIncrementing(num){
  let arr = num.toString().split('').map(e=>parseInt(e));
  
  let theNum = arr[0];
  for(let i=1; i<arr.length; i++){
    theNum+=1
    if(theNum===10) theNum=0;
    if(arr[i]!==theNum) return false;
  }
  console.log("3...returning true")
  
  return true;
}

function isDecrementing(num){
  let arr = num.toString().split('').map(e=>parseInt(e));
  
  let theNum = arr[0];
  for(let i=1; i<arr.length; i++){
    theNum-=1
    if(theNum===-1 && i!==arr.length-1) return false;
    if(arr[i]!==theNum) return false;
  }
  console.log("4...returning true")
  
  return true;
}

function isPalindrome(num){
  console.log("isPalindrome...", num)
  let firstPart;
  let lastPart;
  let arr = num.toString().split('');
  if(arr.length%2==0){
    //0..num/2
    firstPart = arr.slice(0,arr.length/2)
    //num/2+1..length-1
    lastPart = arr.slice(arr.length/2)
  } else {
    firstPart = arr.slice(0,Math.floor(arr.length/2))
    lastPart = arr.slice(Math.floor(arr.length/2)+1)
  } 
//   console.log(firstPart, lastPart)
  if(firstPart.join('') !== lastPart.reverse().join('')) return false
//   console.log("5...returning true")
  
  return true
}
function isAwesomePhrases(num, awesomePhrases){
  if(awesomePhrases.includes(num)) {
    console.log("6...returning true")
    return true
  }
  return false
}


//Interesting 3! 🔥
function isPalindrome(number){   
  return number.toString().length > 2 && 
          /^(.?)(.?)(.?)(.?)(.?).?\5\4\3\2\1$/.test(number);
}

function isSequentialAsc(number){    
  return number.toString().length > 2 &&
          '1234567890'.indexOf(number) >= 0;  
}

function isSequentialDesc(number){
  return number.toString().length > 2 && 
          '9876543210'.indexOf(number) >= 0;  
}

function isAwesomePhrase(number, awesomePhrases){
  return awesomePhrases.some( function(n){ return n==number; } );
}

function isFollowedByZero(number){ 
  return  number % 100 == 0 || 
          number % 1000 == 0 || 
          number % 10000 == 0;
}

function isSameDigits(number){
  return /^(\d)\1{2,4}$/.test(number);
}

function isInteresting(number, awesomePhrases) {
  
  var isInteresting = 0;  
  
  for(var i=0; i<3 && !isInteresting && number >= 98 ; ++i, number++){             
    isInteresting = isPalindrome(number) ||
                  isSequentialAsc(number) || 
                  isSequentialDesc(number) ||
                  isAwesomePhrase(number, awesomePhrases) ||
                  isFollowedByZero(number) ||
                  isSameDigits(number) ? (i==0?2:1) : 0;
  
  } 
  return isInteresting;  
}