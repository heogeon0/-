const cals = [
  (a, b) => a + b,
  (a, b) => a - b,
  (a, b) => (a / b) | 0,
  (a, b) => a * b,
];

function DP(i, dp, N) {
  const temp = new Set();
  temp.add(String(N).repeat(i) * 1);

  for (const cal of cals) {
    for (let j = 0; j < i; j++) {
      for (let a of dp[j]) {
        for (let b of dp[i - j]) {
          const re = cal(a, b);
          temp.add(re);
        }
      }
    }
  }

  return temp;
}

function solution(N, number) {
  if (N === number) return 1;
  const dp = [new Set()];
  dp.push(new Set().add(N));

  for (let i = 2; i < 10; i++) {
    dp.push(DP(i, dp, N));

    if (dp[i].has(number)) return i;
  }

  return -1;
}
