const fs = require("fs");
const input = fs.readFileSync("번데기.txt").toString().trim().split("\n");

const N = input[0] * 1;
const T = input[1] * 1;
const target = input[2] * 1;

let n = 0;
let cnt = 0;
let answer = 0;

while (true) {
  n += 1;

  const arr = [0, 1, 0, 1];
  for (let i = 1; i <= n + 1; i++) arr.push(0);
  for (let i = 1; i <= n + 1; i++) arr.push(1);

  for (const x of arr) {
    if (x === target) cnt++;
    if (cnt === T) {
      console.log(answer);
      return
    }

    answer += 1;
    answer %= N;
  }
}
