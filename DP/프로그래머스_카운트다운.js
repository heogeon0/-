function solution(target) {
  var dp = new Array(target + 1)
    .fill(0)
    .map((i) => new Array(2).fill(Infinity));
  // 1. 싱글로 넣는 경우
  for (let i = 1; i <= 20; i++) dp[i] = [1, 1];
  dp[0] = [0, 0];

  for (let i = 1; i <= target; i++) {
    for (let j = 1; j <= 20; j++) {
      // 1. 싱글로 넣는 경우
      if (i - j >= 0) {
        k = i - j;
        if (dp[k][0] + 1 < dp[i][0]) dp[i] = [dp[k][0] + 1, dp[k][1] + 1];
        else if (dp[k][0] + 1 === dp[i][0] && dp[k][1] + 1 > dp[i][1])
          dp[i][1] = dp[k][1] + 1;
      }

      // 2. 더블로 넣는 경우
      if (i - 2 * j >= 0) {
        k = i - 2 * j;
        if (dp[k][0] + 1 < dp[i][0]) dp[i] = [dp[k][0] + 1, dp[k][1]];
        else if (dp[k][0] + 1 === dp[i][0] && dp[k][1] > dp[i][1])
          dp[i][1] = dp[k][1];
      }

      // 3. 트리플로 넣는 경우
      if (i - 3 * j >= 0) {
        k = i - 3 * j;
        if (dp[k][0] + 1 < dp[i][0]) dp[i] = [dp[k][0] + 1, dp[k][1]];
        else if (dp[k][0] + 1 === dp[i][0] && dp[k][1] > dp[i][1])
          dp[i][1] = dp[k][1];
      }
    }
    // 불로 넣는 경우
    if (i - 50 >= 0) {
      k = i - 50;
      if (dp[k][0] + 1 < dp[i][0]) dp[i] = [dp[k][0] + 1, dp[k][1] + 1];
      else if (dp[k][0] + 1 === dp[i][0] && dp[k][1] + 1 > dp[i][1])
        dp[i][1] = dp[k][1] + 1;
    }
  }

  // console.log(dp)

  var answer = [...dp[target]];
  return answer;
}
