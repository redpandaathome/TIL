// https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/javascript
// str.repeat(num)

function accum(s) {
	// your code
  let result=''
  for(let i=0; i<s.length; i++){
    let firstCap = s[i].toUpperCase();
    let rest = s[i].toLowerCase().repeat(i);
    result= result+firstCap+rest
    if(i!=s.length-1){
      result+='-'
    }
  }
  return result
}

//improved - arr.join('-'), arr->map->different arr, =>(a+b+c)
function accum(s) {
   return s.split('').map((c, i) => (c.toUpperCase() + c.toLowerCase().repeat(i))).join('-');
 }