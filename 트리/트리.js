const fs = require("fs");
const input = fs.readFileSync("트리.txt").toString().trim().split("\n");

const N = input[0];
const arr = input[1].split(" ").map((i) => parseInt(i));

const dfs = (num, arr) => {
  arr[num] = -2;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] == num) {
      dfs(i, arr);
    }
  }
};

dfs(parseInt(input[2]), arr);

let count = 0;
for (let i = 0; i < arr.length; i++) {
  if (arr[i] != -2 && arr.findIndex((v) => v === i) === -1) {
    count++;
  }
}

console.log(count);
