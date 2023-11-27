const filePath = process.platform === "linux" ? "/dev/stdin" : "A와B2.txt";
const fs = require("fs");
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const S = input[0];
const T = input[1];

let answer = 0;

dfs(T);

console.log(answer);

function dfs(t) {
  if (S === t) {
    answer = 1;

    return;
  }

  if (t.length === 0) return;

  if (t[t.length - 1] === "A") dfs(t.slice(0, t.length - 1));

  if (t[0] === "B") dfs([...t.slice(1)].reverse().join(""));
}