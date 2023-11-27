const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "인구이동.txt";
const Input = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, L, R] = Input[0].split(" ").map((i) => parseInt(i));

const arr = new Array(N);
for (let i = 1; i <= N; i++) {
  arr[i - 1] = Input[i].split(" ").map((i) => parseInt(i));
}

const bfs = (r, c, v, union) => {
  const q = [[r, c]];
  const unions = [[r, c]];
  v[r][c] = union;

  while (q.length) {
    const [r, c] = q.shift();

    for (let [dx, dy] of [
      [-1, 0],
      [1, 0],
      [0, -1],
      [0, 1],
    ]) {
      const [nr, nc] = [r + dx, c + dy];

      if (
        0 <= nr &&
        nr < N &&
        0 <= nc &&
        nc < N &&
        v[nr][nc] === 0 &&
        L <= Math.abs(arr[nr][nc] - arr[r][c]) &&
        R >= Math.abs(arr[nr][nc] - arr[r][c])
      ) {
        q.push([nr, nc]);
        v[nr][nc] = union;
        unions.push([nr, nc]);
      }
    }
  }
  return unions;
};

let answer = 0;
while (true) {
  const v = new Array(N).fill(0).map((i) => new Array(N).fill(0));
  let union = 1;
  let unions = [];

  for (let r = 0; r < N; r++) {
    for (let c = 0; c < N; c++) {
      if (v[r][c] === 0) {
        unions.push(bfs(r, c, v, union));
        union++;
      }
    }
  }

  let moves = unions.filter((i) => i.length > 1);
  if (!moves.length) break;

  for (let i = 0; i < moves.length; i++) {
    let total = Math.floor(
      moves[i].reduce((acc, [r, c]) => acc + arr[r][c], 0) / moves[i].length
    );
    moves[i].forEach(([r, c]) => (arr[r][c] = total));
  }
  answer++;
  // break;
}

console.log(answer);
