const fs = require("fs");
const input = fs.readFileSync("동전.txt").toString().trim().split("\n");

const T = input.shift() * 1;

for (let t = 0; t < T; t++) {
  const N = input.shift() * 1;
  const coins = input
    .shift()
    .split(" ")
    .map((i) => parseInt(i));

  const M = input.shift() * 1;
  const dp = new Array(M + 1).fill(0);

  dp[0] = 1;
  for (let coin of coins) {
    for (let i = 0; i < M + 1; i++) {
      if (i >= coin) {
        dp[i] += dp[i - coin];
      }
    }
  }

  console.log(dp[M]);
}
