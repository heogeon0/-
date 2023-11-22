const fs = require("fs");
const input = fs.readFileSync("바이러스.txt").toString().trim().split("\n");

const N = parseInt(input[0]);
const M = parseInt(input[1]);

const arr = new Array(N + 1).fill(0).map((i) => new Array(0));

for (let i = 2; i < 2 + M; i++) {
  const [a, b] = input[i].split(" ").map((i) => parseInt(i));

  arr[a].push(b);
  arr[b].push(a);
}

const v = new Array(N + 1).fill(0);
v[1] = 1;
const q = [1];
let answer = 0;

while (q.length) {
  const now = q.shift();

  for (let next of arr[now]) {
    if (v[next] === 0) {
      v[next] = 1;
      answer++;
      q.push(next);
    }
  }
}

console.log(answer);
