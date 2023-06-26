const filePath =
  process.platform === "linux" ? "/dev/stdin" : "백준_아기상어.txt";
const Input = require("fs")
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");

const N = parseInt(Input[0]);
const map = [];

for (let i = 1; i <= N; i++) {
  map.push(
    Input[i]
      .trim()
      .split(" ")
      .map((i) => parseInt(i))
  );
}

// 현재 위치 찾기
let [nr, nc] = [0, 0];
for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    if (map[i][j] === 9) {
      [nr, nc] = [i, j];
      map[i][j] = 0;
    }
  }
}

let now = 2;
let cnt = 0;
let time = 0;
while (true) {
  // 1. 현재 위치에서 BFS로 후보자들 찾기
  let candis = [];
  candis = bfs(map, nr, nc, now);
  if (candis.length === 0) {
    console.log(time);
    return;
  }

  // console.log(candis);
  // 2. candis 를 통해서 다음 위치 정하기 (1.가장 가깝고, 2. 행이 작고, 3. 열이작고)
  candis.sort((a, b) =>
    a[2] === b[2] ? (a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]) : a[2] - b[2]
  );
  [nr, nc] = [candis[0][0], candis[0][1]];
  time += candis[0][2];

  cnt += 1;
  map[nr][nc] = 0;
  if (cnt === now) {
    now += 1;
    cnt = 0;
  }

  // console.log(time, nr, nc, candis[0][2]);
  // break;
}

// 2-2. 있다면 그 위치로 이동 및 크기 커지기

function bfs(map, nr, nc, size) {
  const delta = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];
  const N = map.length;
  const Q = [[nr, nc, 0]];
  const v = new Array(map.length)
    .fill(0)
    .map((i) => new Array(map.length).fill(0));

  const candis = [];
  while (Q.length) {
    const [nowr, nowc, nt] = Q.shift();

    for (let [dx, dy] of delta) {
      let [nxr, nxc] = [nowr + dx, nowc + dy];

      if (
        0 <= nxr &&
        nxr < N &&
        0 <= nxc &&
        nxc < N &&
        map[nxr][nxc] <= size &&
        v[nxr][nxc] === 0
      ) {
        if (v[nxr][nxc] === 0) {
          v[nxr][nxc] = 1;

          if (map[nxr][nxc] > 0 && map[nxr][nxc] < size) {
            candis.push([nxr, nxc, nt + 1]);
          }
          Q.push([nxr, nxc, nt + 1]);
        }
      }
    }
  }
  return candis;
}
