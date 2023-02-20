'use strict';

const fs = require('fs');

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
 * Complete the 'hourglassSum' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY arr as parameter.
 */

function hourglassSum(arr) {
    // Write your code here
    console.log("arr:",arr)
    let directions = [[0,0],[0,1],[0,2],[1,1],[2,0],[2,1],[2,2]]
    let newArr = []
    for(let i=0; i<4;i++){
        let lineSum = []
        for(let j=0;j<4;j++){
            let sum = 0
            for (const d of directions){
                let nx = parseInt(d[0])+ parseInt(i)
                let ny = parseInt(d[1])+parseInt(j)
                sum+=arr[nx][ny]
            }
            lineSum.push(sum)
        }
        newArr.push(lineSum)
    }
    console.log("newArr...", newArr)
    let max = newArr[0][0];

    for(let i=0; i<newArr.length;i++){
        for(let j=0; j<newArr[i].length; j++){
            max = Math.max(max, newArr[i][j])
            console.log('max...', max)
        }
    }
    return max
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    let arr = Array(6);

    for (let i = 0; i < 6; i++) {
        arr[i] = readLine().replace(/\s+$/g, '').split(' ').map(arrTemp => parseInt(arrTemp, 10));
    }

    const result = hourglassSum(arr);

    ws.write(result + '\n');

    ws.end();
}
