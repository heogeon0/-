function solution(n, s, a, b, fares) {
  var dik = new Array(n + 1)
    .fill(0)
    .map((i) => new Array(n + 1).fill(Infinity));

  for (let [a, b, m] of fares) {
    dik[a][b] = m;
    dik[b][a] = m;
  }

  for (let i = 1; i <= n; i++) {
    dik[i][i] = 0;
  }

  for (let k = 1; k <= n; k++) {
    for (let i = 1; i <= n; i++) {
      for (let j = 1; j <= n; j++) {
        if (dik[i][j] > dik[i][k] + dik[k][j])
          dik[i][j] = dik[i][k] + dik[k][j];
      }
    }
  }

  let answer = dik[s][a] + dik[s][b];
  // console.log(answer)
  for (let i = 1; i <= n; i++) {
    answer = Math.min(answer, dik[s][i] + dik[i][a] + dik[i][b]);
  }

  // console.log(dik)
  return answer;
}
