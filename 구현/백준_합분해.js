const filepath = process.platform === "linux" ? "/dev/stdin" : "합분해.txt";
const [N, M] = require("fs")
  .readFileSync(filepath)
  .toString()
  .trim()
  .split(" ")
  .map((i) => parseInt(i));

const dp = new Array(M + 1).fill(0).map((i) => new Array(N + 1).fill(0));

for (let i = 0; i <= N; i++) {
  dp[1][i] = 1;
}

// for (let j = 1; j <= M; j++) {
//   dp[j][0] =
// }

for (let i = 2; i <= M; i++) {
  for (let j = 0; j <= N; j++) {
    if (j === 0) dp[i][j] = 1;
    else dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1_000_000_000;
  }
}

console.log(dp[M][N]);
