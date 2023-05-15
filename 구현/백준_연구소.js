const { exit } = require("process");
const filePath = process.platform === "linux" ? "/dev/stdin" : "연구소.txt";
const input = require("fs")
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");

function virus(map) {
  const delta = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];
  const lsts = [];

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (map[i][j] === 2) {
        let Q = [[i, j]];

        while (Q.length) {
          let [nr, nc] = Q.shift();

          for (let [xr, xc] of delta) {
            let [dr, dc] = [nr + xr, nc + xc];

            if (0 <= dr && dr < N && 0 <= dc && dc < M && map[dr][dc] === 0) {
              lsts.push([dr, dc]);
              Q.push([dr, dc]);
              map[dr][dc] = 3;
            }
          }
        }
      }
    }
  }
  // console.log(map);
  // 0 갯수 세기
  let zeroCnt = 0;
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (map[i][j] === 0) zeroCnt++;
    }
  }

  while (lsts.length) {
    const [r, c] = lsts.shift();
    map[r][c] = 0;
  }

  // console.log(map);
  return zeroCnt;
}

const [N, M] = input[0].split(" ").map((i) => parseInt(i));
const map = [];

for (let i = 1; i <= N; i++) {
  map.push(
    input[i]
      .trim()
      .split(" ")
      .map((i) => parseInt(i))
  );
}

const walls = [];
for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    if (map[i][j] === 0) walls.push([i, j]);
  }
}

// 1. 벽 위치 정하기

let answer = 0;
for (let i = 0; i < walls.length - 2; i++) {
  for (let j = i + 1; j < walls.length - 1; j++) {
    for (let k = j + 1; k < walls.length; k++) {
      map[walls[i][0]][walls[i][1]] = 1;
      map[walls[j][0]][walls[j][1]] = 1;
      map[walls[k][0]][walls[k][1]] = 1;

      // console.log(virus(map));
      answer = Math.max(answer, virus(map));
      map[walls[i][0]][walls[i][1]] = 0;
      map[walls[j][0]][walls[j][1]] = 0;
      map[walls[k][0]][walls[k][1]] = 0;
      // console.log(map);
      // exit();
    }
  }
}

// console.log(walls);
console.log(answer);
// console.log(N, M);
