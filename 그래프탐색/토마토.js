const fs = require("fs");
const input = fs.readFileSync("토마토.txt").toString().trim().split("\n");

const [M, N, H] = input
  .shift()
  .split(" ")
  .map((i) => parseInt(i));

const arr = Array.from(Array(H), () =>
  Array.from(Array(N), () => Array.from(Array(M).fill(0)))
);

for (let h = 0; h < H; h++) {
  for (let n = 0; n < N; n++) {
    arr[h][n] = input.shift().split(" ").map(Number);
  }
}

const q = [];
let tomatos = 0;
for (let h = 0; h < H; h++) {
  for (let n = 0; n < N; n++) {
    for (let m = 0; m < M; m++) {
      if (arr[h][n][m] === 1) {
        q.push([h, n, m, 0]);
      }
      if (arr[h][n][m] === 0) {
        tomatos++;
      }
    }
  }
}

const delta = [
  [0, 0, -1],
  [0, 0, 1],
  [0, 1, 0],
  [0, -1, 0],
  [1, 0, 0],
  [-1, 0, 0],
];

let day = -1;
let idx = 0;
while (q.length > idx) {
  const [nh, nr, nc, nday] = q[idx++];

  day = nday;
  for (let [h, x, y] of delta) {
    let [dh, dx, dy] = [nh + h, nr + x, nc + y];

    if (
      0 <= dh &&
      dh < H &&
      0 <= dx &&
      dx < N &&
      0 <= dy &&
      dy < M &&
      arr[dh][dx][dy] === 0
    ) {
      arr[dh][dx][dy] = nday + 1;
      q.push([dh, dx, dy, nday + 1]);
      tomatos--;
    }
  }
}

console.log(tomatos ? -1 : day);
