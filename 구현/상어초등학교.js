const fs = require("fs");
const input = fs.readFileSync("상어초등학교.txt").toString().trim().split("\n");

const N = parseInt(input[0]);
const arr = [];

for (let i = 1; i <= N ** 2; i++) {
  arr.push(input[i].split(" ").map((i) => parseInt(i)));
}

const map = new Array(N).fill(0).map((i) => new Array(N).fill(0));
const delta = [
  [-1, 0],
  [1, 0],
  [0, -1],
  [0, 1],
];

const score = [0, 1, 10, 100, 1000];
const scope_likes = new Array(N ** 2);
let answer = 0;
for (let i = 0; i < N ** 2; i++) {
  const candi = [];
  const now = arr[i][0];
  const likes = new Set(arr[i].slice(1, 5));
  scope_likes[now] = likes;
  for (let row = 0; row < N; row++) {
    for (let col = 0; col < N; col++) {
      if (map[row][col] !== 0) continue;
      let cntZero = 0;
      let cntLike = 0;

      for (let [dx, dy] of delta) {
        const drow = row + dx;
        const dcol = col + dy;

        if (drow >= 0 && drow < N && dcol >= 0 && dcol < N) {
          if (map[drow][dcol] === 0) {
            cntZero++;
            continue;
          }
          if (likes.has(map[drow][dcol])) {
            cntLike++;
          }
        }
      }
      candi.push([cntLike, cntZero, row, col]);
    }
  }

  candi.sort((a, b) => {
    if (a[0] === b[0]) {
      if (a[1] === b[1]) {
        if (a[2] === b[2]) {
          return a[3] - b[3];
        } else {
          return a[2] - b[2];
        }
      } else {
        return b[1] - a[1];
      }
    } else {
      return b[0] - a[0];
    }
  });

  const [cnt, _, row, col] = candi[0];
  map[row][col] = now;
}

for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    let cntLike = 0;
    let now = map[i][j];
    for (let [dx, dy] of delta) {
      const drow = i + dx;
      const dcol = j + dy;

      if (drow >= 0 && drow < N && dcol >= 0 && dcol < N) {
        if (scope_likes[now].has(map[drow][dcol])) {
          cntLike++;
        }
      }
    }
    answer += score[cntLike];
  }
}

console.log(answer);
