const filePath =
  process.platform === "linux" ? "/dev/stdin" : "최소스패닝트리.txt";

const Input = require("fs")
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");

const [N, M] = Input[0].split(" ").map(Number);

const arr = [];
for (let i = 1; i <= M; i++) {
  const [p, c, t] = Input[i].split(" ").map(Number);
  arr.push([p, c, t]);
}

arr.sort((a, b) => a[2] - b[2]);

const parents = new Array(N + 1).fill(0).map((_, i) => i);
let edge = N - 1;

const find = (now) => {
  if (now === parents[now]) return now;
  return (parents[now] = find(parents[now]));
};

const union = (a, b) => {
  let [roota, rootb] = [find(a), find(b)];
  let flag = roota === rootb;
  if (flag) return { flag: false };

  parents[rootb] = roota;
  return { flag: true };
};

let answer = 0;
for (let i = 0; i < M; i++) {
  const [a, b, c] = arr[i];

  let { flag } = union(a, b);

  if (flag) {
    answer += c;
    edge -= 1;
  }

  if (!edge) break;
}

console.log(answer);
