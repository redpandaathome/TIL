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
 * Complete the 'sockMerchant' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER_ARRAY ar
 */

function sockMerchant(n, ar) {
  // Write your code here
  let temp = {};
  ar.forEach((e) => {
    if (e in temp) {
      temp[e] += 1;
    } else {
      temp[e] = 1;
    }
  });
  console.log("temp:", temp);
  let count = 0;
  for (let i = 0; i < Object.keys(temp).length; i++) {
    let value = temp[Object.keys(temp)[i]];
    console.log("i:", i, ", value:", value);
    if (value == undefined) continue;
    count += Math.floor(value / 2);
    console.log("new count...", count);
  }
  console.log("count:", count);
  return count;
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const n = parseInt(readLine().trim(), 10);

  const ar = readLine()
    .replace(/\s+$/g, "")
    .split(" ")
    .map((arTemp) => parseInt(arTemp, 10));

  const result = sockMerchant(n, ar);

  ws.write(result + "\n");

  ws.end();
}
