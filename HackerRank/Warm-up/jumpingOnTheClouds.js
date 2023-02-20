"use strict";

const fs = require("fs");

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", function (inputStdin) {
  inputString += inputStdin;
});

process.stdin.on("end", function () {
  inputString = inputString.split("\n");

  main();
});

function readLine() {
  return inputString[currentLine++];
}

/*
 * Complete the 'jumpingOnClouds' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY c as parameter.
 */

function jumpingOnClouds(c) {
  // Write your code here

  let count = 0;
  let bigJump = false;
  for (let i = 0; i < c.length - 1; i++) {
    if (bigJump && c[bigJump] !== null) i += 1;
    // console.log('new i...', i)
    if (c[i + 2] == 0) {
      bigJump = true;
      count += 1;
    } else if (c[i + 1] == 0) {
      bigJump = false;
      count += 1;
    }
  }
  return count;
}

//✨ better solution
// function jumpingOnClouds(c) {
//    var n = 0;
//    for (var i = 0; i < c.length - 1;) {
//✨✨✨
//      i += (c[i+2] ? 1 : 2);
//      n++;
//    }
//    return n;
//  }

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const n = parseInt(readLine().trim(), 10);

  const c = readLine()
    .replace(/\s+$/g, "")
    .split(" ")
    .map((cTemp) => parseInt(cTemp, 10));

  const result = jumpingOnClouds(c);

  ws.write(result + "\n");

  ws.end();
}
