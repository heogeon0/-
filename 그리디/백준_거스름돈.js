
const fs = require('fs')
const input = parseInt(fs.readFileSync('./백준_거스름돈.txt').toString().trim())

const dp = new Array(input + 1).fill(-1)
const money = [2, 5]

dp[0] = 1
dp[2] = 1
dp[5] = 1

for (let i = 1; i <= input; i++) {
  for (let m of money) {
    if (i - m > 0 && dp[i-m] != -1) {
      dp[i] = dp[i-m] + 1
    }
  }
}

console.log(dp[input])