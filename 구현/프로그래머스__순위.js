function solution(n, results) {
  var table = new Array(n + 1).fill(0).map((i) => new Array(n + 1).fill(0));

  results.forEach(([w, l]) => {
    table[w][l] = 1;
    table[l][w] = -1;
  });

  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= n; j++) {
      for (let k = 1; k <= n; k++) {
        if (table[j][k] === 1 && table[i][j] === 1) {
          table[i][k] = 1;
          table[k][i] = -1;
        }
        if (table[j][k] === -1 && table[i][j] === -1) {
          table[i][k] = -1;
          table[k][i] = 1;
        }
      }
    }
  }
  console.log(table);
  var answer = 0;

  for (let i = 1; i <= n; i++) {
    let total = 0;
    for (let j = 1; j <= n; j++) {
      total += table[i][j] ? 1 : 0;
    }

    total === n - 1 ? answer++ : null;
  }
  return answer;
}
