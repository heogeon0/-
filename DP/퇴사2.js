const fs = require("fs");
const input = fs.readFileSync("퇴사2.txt").toString().trim().split("\n");
const N = input[0] * 1;
const arr = input
  .slice(1, N + 1)
  .map((i) => i.split(" ").map((i) => parseInt(i)));

// console.log(arr);
arr.unshift([0, 0]);

const dp = new Array(N + 1).fill(0);

for (let i = 1; i <= N; i++) {
  dp[i] = Math.max(dp[i], dp[i - 1]);
  const [d, cash] = arr[i];

  if (i + d - 1 <= N) {
    dp[i + d - 1] = Math.max(dp[i - 1 + d], dp[i - 1] + cash);
  }
}
console.log(dp[N]);
