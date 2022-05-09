/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var sortedSquares = function(nums) {
   return nums.map(e=>Math.pow(e,2)).sort((a,b)=>a-b)
};

//✨✨✨algorithm
// num**2
// tail--, head++
var sortedSquares = function(A) {
  const result = [];
  let head = 0;
  let tail = A.length - 1;

  while (head <= tail) {
    console.log("head&tail:",head,tail)
    if (A[head] ** 2 > A[tail] ** 2) result.push(A[head++] ** 2);
    else result.push(A[tail--] ** 2);
    console.log("result:", result)
  }

  return result.reverse();
};


// Your input
// [-4,-1,0,3,10]
// Your stdout
// head&tail: 0 4
// result: [ 100 ]
// head&tail: 0 3
// result: [ 100, 16 ]
// head&tail: 1 3
// result: [ 100, 16, 9 ]
// head&tail: 1 2
// result: [ 100, 16, 9, 1 ]
// head&tail: 2 2
// result: [ 100, 16, 9, 1, 0 ]

// Your answer
// [0,1,9,16,100]

//t1
var sortedSquares = function(A) {
  const result = [];
  let head = 0;
  let tail = A.length - 1;

  while (head<=tail){
      if(Math.pow(A[head],2)<Math.pow(A[tail],2))result.push(Math.pow(A[tail--],2))
      else result.push(Math.pow(A[head++],2))
  }
    return result.reverse()
};