const { exit } = require("process");

const filepath =
  process.platform === "linux" ? "/dev/stdin" : "유닛이동시키기.txt";
const input = require("fs")
  .readFileSync(filepath)
  .toString()
  .trim()
  .split("\n");

const [N, M, A, B, K] = input[0]
  .trim()
  .split(" ")
  .map((i) => parseInt(i));
const table = new Array(N).fill(0).map((i) => new Array(M).fill(0));

function checkBlock(a, b) {
  const block = [];
  for (let i = 0; i < A; i++) {
    for (let j = 0; j < B; j++) {
      block.push([a + i, b + j]);
    }
  }
  return block;
}

for (let i = 1; i <= K; i++) {
  const [a, b] = input[i].split(" ").map((i) => parseInt(i) - 1);
  table[a][b] = 3;
}

let starts = input[K + 1]
  .trim()
  .split(" ")
  .map((i) => parseInt(i) - 1);
let ends = input[K + 2]
  .trim()
  .split(" ")
  .map((i) => parseInt(i) - 1);

let Q = [[...starts, 0]];

table[starts[0]][starts[1]] = 1;
const delta = [
  [1, 0],
  [0, 1],
  [-1, 0],
  [0, -1],
];

// console.log(Q);
// console.log(table);
while (Q.length) {
  // console.log(Q);
  let [r, c, cnt] = Q.shift();
  // console.log(r, c, cnt);
  if (r === ends[0] && c === ends[1]) {
    console.log(cnt);
    exit();
  }

  for (let [dr, dc] of delta) {
    let [nr, nc] = [r + dr, c + dc];

    if (
      0 <= nr &&
      nr <= N - A &&
      0 <= nc &&
      nc <= M - B &&
      table[nr][nc] === 0
    ) {
      // console.log(nr, nc);
      // 2. 장애물 체크
      let blocks = checkBlock(nr, nc);
      // console.log(blocks);
      let flag = true;
      for (let [br, bc] of blocks) {
        if (table[br][bc] === 3) {
          flag = false;
          break;
        }
      }

      if (flag) {
        table[nr][nc] = 1;
        Q.push([nr, nc, cnt + 1]);
      }
    }
  }
}

// console.log(table);
console.log(-1);
