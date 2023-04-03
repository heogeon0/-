function solution(n, m, x, y, r, c, k) {
  const arr = new Array(n + 1).fill(0).map((i) => new Array(m + 1).fill(0));
  const dir = ["u", "r", "l", "d"];
  const delta = [
    [-1, 0],
    [0, 1],
    [0, -1],
    [1, 0],
  ];

  const stack = [[x, y, ""]];

  while (stack.length) {
    const [nr, nc, now] = stack.pop();

    if (nr === r && nc === c && now.length === k) return now;
    let [remain, shorts] = [
      k - now.length,
      Math.abs(nr - r) + Math.abs(nc - c),
    ];

    if (remain < shorts || remain % 2 != shorts % 2) continue;

    for (let i = 0; i < 4; i++) {
      const [dx, dy] = [nr + delta[i][0], nc + delta[i][1]];
      if (0 < dx && dx <= n && 0 < dy && dy <= m && arr[dx][dy] === 0) {
        stack.push([dx, dy, now + dir[i]]);
      }
    }
  }
  return "impossible";
}
