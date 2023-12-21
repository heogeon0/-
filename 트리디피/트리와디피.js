const filePath = process.platform === "linux" ? "/dev/stdin" : "트리와디피.txt";
const input = require("fs")
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");

const [N, R, Q] = input[0].split(" ").map((i) => parseInt(i));

const dp = Array(N + 1).fill(1);
const v = Array(N + 1).fill(0);
const arr = Array.from(Array(N + 1), () => Array());

for (let i = 1; i <= N - 1; i++) {
  const [s, e] = input[i].split(" ").map((i) => i * 1);

  arr[s].push(e);
  arr[e].push(s);
}

const dfs = (now) => {
  if (v[now]) return dp[now];

  v[now] = 1;

  for (let next of arr[now]) {
    if (v[next] === 0) {
      dp[now] += dfs(next);
    }
  }

  return dp[now];
};

dfs(R);

for (let i = N; i < N + Q; i++) {
  console.log(dp[input[i] * 1]);
}
