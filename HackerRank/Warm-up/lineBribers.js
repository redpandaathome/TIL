// couldn't pass time limit 💩💩💩

'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'minimumBribes' function below.
 *
 * The function accepts INTEGER_ARRAY q as parameter.
 */

function minimumBribes(q) {
    // Write your code here
    let original = Array.from({length: q.length}, (_, i) => i + 1)
    let result = 0
    let isChaotic = false;
    for(let i=0; i<q.length; i++){
        // console.log("i:",i, "original:", original)
        if(original[i] < q[i]){
            let cheater = q[i]
            let cheaterOriginalIdx = original.indexOf(cheater)
            let gap = cheaterOriginalIdx-i;
            if (gap >=3){
                isChaotic = true
                break;
            }
            
            result += gap
            // console.log("changing original...",i, gap)
            original = changeArr(original, cheaterOriginalIdx, gap)
        }
    }
    if(isChaotic){
        console.log("Too chaotic")
    }else {
        console.log(result)
    }
    // console.log("==================")
}

function changeArr(arr, cheaterIdx,bribes){
  let targetIdx = cheaterIdx-bribes
  let front = arr.slice(0,targetIdx)
  let back =arr.slice(targetIdx,cheaterIdx)
  let tail = arr.slice(cheaterIdx+1, arr.length)
  let newArr= []
  newArr.push(...front,arr[cheaterIdx],...back,...tail)
//   console.log("---arr:", arr)
//   console.log("---targetIdx:", targetIdx)
//   console.log("---bribes:", bribes)
//   console.log("---front:", front)
//   console.log("---arr[cheaterIdx]:", arr[cheaterIdx])  
//   console.log("---back:", back)
//   console.log("---tail:", front)
  
  
  return newArr;
}

function main() {
    const t = parseInt(readLine().trim(), 10);

    for (let tItr = 0; tItr < t; tItr++) {
        const n = parseInt(readLine().trim(), 10);

        const q = readLine().replace(/\s+$/g, '').split(' ').map(qTemp => parseInt(qTemp, 10));

        minimumBribes(q);
    }
}
