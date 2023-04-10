function solution(alp, cop, problems) {
  let [max_alp, max_cop] = problems.reduce(
    (acc, [areq, creq, ...a]) => {
      return [Math.max(acc[0], areq), Math.max(acc[1], creq)];
    },
    [0, 0]
  );

  if (alp > max_alp) alp = max_alp;
  if (cop > max_cop) cop = max_cop;

  var dp = new Array(max_alp + 2)
    .fill(0)
    .map((i) => new Array(max_cop + 2).fill(Infinity));
  dp[alp][cop] = 0;

  for (let i = alp; i <= max_alp; i++) {
    for (let j = cop; j <= max_cop; j++) {
      const [a, b] = [Math.min(i, max_alp), Math.min(j, max_cop)];
      dp[a][b + 1] = Math.min(dp[a][b + 1], dp[a][b] + 1);
      dp[a + 1][b] = Math.min(dp[a + 1][b], dp[a][b] + 1);

      problems.forEach(([alp_req, cop_req, alp_rwd, cop_rwd, cost]) => {
        if (i >= alp_req && j >= cop_req) {
          const [nalp, ncop] = [i + alp_rwd, j + cop_rwd];

          dp[Math.min(nalp, max_alp)][Math.min(ncop, max_cop)] = Math.min(
            dp[Math.min(nalp, max_alp)][Math.min(ncop, max_cop)],
            dp[i][j] + cost
          );
        }
      });
    }
  }

  return dp[max_alp][max_cop];
}
