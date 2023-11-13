const fs = require("fs");
const input = fs.readFileSync("완전이진트리.txt").toString().trim().split("\n");

const N = parseInt(input[0]);
const arr = input[1].split(" ").map((i) => parseInt(i));

const answer = new Array(N).fill(0).map((i) => []);

const sol = (level, arr) => {
  if (arr.length === 1) {
    answer[level].push(arr[0]);
    return;
  } else {
    const mid = Math.floor(arr.length / 2);

    sol(level + 1, arr.slice(0, mid));
    sol(level + 1, arr.slice(mid + 1, arr.length));
    answer[level].push(arr[mid]);
  }
};

sol(0, arr);

for (const a of answer) {
  console.log(a.join(" "));
}
