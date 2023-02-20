function arrayManipulation(n, queries) {
   // Write your code here
   // 💜💜💜
   let zeroArr = '0'.repeat(n+1).split('').map((e) => parseInt(e));
   for(let i=0; i<queries.length; i++){
       // console.log("q[",i,"]:",queries[i])
       let startIdx = queries[i][0]
       let endIdx = queries[i][1]
       let addAmount = queries[i][2]
       
       zeroArr[startIdx-1]+=addAmount
       zeroArr[endIdx]-=addAmount
   }
   // console.log(zeroArr)
   let ans = 0
   let cur=0
   for(let i=0; i<n; i++){
      // 💜
       cur += zeroArr[i]
       if (cur>ans){
           ans = cur
       }
   }
   return ans
}


//interesting but more complicated
//https://medium.com/@Kliative/array-manipulation-hacker-rank-javascript-5a702c1ff044