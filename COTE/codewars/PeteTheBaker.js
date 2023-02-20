
// object array
function cakes(recipe, available) {
   // TODO: insert code
   let countObj = {}
   let result = 0
   let recipeKeys = Object.keys(recipe);
   let availKeys = Object.keys(available)
   for(let i=0; i<recipeKeys.length; i++){
 
     if(!availKeys.includes(recipeKeys[i])){
 //       console.log("NOTENOUGH INGRE>>>RETURN!")
       return 0
     }
     let currentKey = recipeKeys[i];
     countObj[currentKey]=Math.floor(available[currentKey]/recipe[currentKey])
   }
 
 //   console.log(countObj)
 // ✨
   result=Infinity
   Object.keys(countObj).forEach(e=>{
     result=Math.min(result,countObj[e])
 //     console.log("countObj[e]", countObj[e], "result:",result)
   })
   return result;
 }

//Second trial 
function cakes(recipe, available) {
  let keys = Object.keys(recipe).sort()
  let availableKeys = Object.keys(available).sort()
  if(keys.length > availableKeys.length) return 0
  
  // ✨
  let minCnt = Math.max(...Object.values(available))
  let current;

  availableKeys.every(k=>{
    if(recipe[k] === undefined){
      return true
    }
    if(recipe[k] > available[k]){
      minCnt = 0
      return false
    } else {
      current = Math.floor(available[k]/recipe[k])
      minCnt = Math.min(minCnt, current)
    }

    return true
  })
  
  return minCnt
}


// IMPROVED ✨
// 1.reduce((val, ingredient)=>{}, Infinity(initialValue)) -> will start with first ingredient as a current
// 2. Math.floor(iffy ||0), if something goes wrong with NaN or undefined, it will take 0
function cakes(recipe, available) {
   return Object.keys(recipe).reduce(function(val, ingredient) {
     return Math.min(Math.floor(available[ingredient] / recipe[ingredient] || 0), val)
   }, Infinity)  
 }