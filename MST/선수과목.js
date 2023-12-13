const filePath = process.platform === "linux" ? "/dev/stdin" : "선수과목.txt";

const Input = require("fs")
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");

const [N, M] = Input[0].split(" ").map((i) => parseInt(i));
const map = {};
const inDegree = new Array(N + 1).fill(0);
const answer = new Array(N + 1).fill(1);

for (let i = 1; i <= M; i++) {
  let [p, c] = Input[i].split(" ").map((i) => parseInt(i));

  map[p] = (map[p] || []).concat(c);
  inDegree[c] += 1;
}

const q = [];

for (let i = 1; i <= N; i++) {
  !inDegree[i] ? q.push(i) : null;
}

while (q.length) {
  now = q.shift();

  for (let node of map[now] || []) {
    inDegree[node] -= 1;

    if (inDegree[node] === 0) {
      q.push(node);
      answer[node] = answer[now] + 1;
    }
  }
}

console.log(answer.slice(1).join(" "));
