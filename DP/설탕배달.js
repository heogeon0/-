const fs = require("fs");
const N = fs.readFileSync("설탕배달.txt").toString().trim() * 1;

const dp = new Array(N + 1).fill(0);
const stand = [3, 5];

// console.log(dp);
dp[0] = 0;
dp[3] = 1;
dp[5] = 1;

for (let i = 3; i < N + 1; i++) {
  for (let j of stand) {
    if (i - j > 0 && dp[i - j] != 0) {
      dp[i] = dp[i - j] + 1;
    }
  }
}

console.log(dp[N] != 0 ? dp[N] : -1);
