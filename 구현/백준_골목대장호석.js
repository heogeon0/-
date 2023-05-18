const filePath =
  process.platform === "linux" ? "/dev/stdin" : "골목대장호석.txt";
const input = require("fs")
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");

const [N, _, A, B, c] = input[0].split(" ").map((i) => parseInt(i));
const map = new Array(N + 1).fill(0).map((i) => new Array(N + 1).fill(0));
const v = new Array(N + 1).fill(0);

for (let temp of input.slice(1)) {
  let [a, b, m] = temp.split(" ").map((i) => parseInt(i));
  map[a][b] = m;
  map[b][a] = m;
}

let answer = Infinity;
let C = c;
// console.log(map);

const solution = (nowIdx, maxMoney) => {
  // console.log(nowIdx, maxMoney);
  if (maxMoney >= answer) return;

  if (nowIdx === B) {
    answer = maxMoney;
    return;
  }

  for (let nextIdx = 1; nextIdx <= N; nextIdx++) {
    // console.log(nowIdx, nextIdx);
    if (map[nowIdx][nextIdx] === 0 || v[nextIdx] === 1) continue;
    if (C - map[nowIdx][nextIdx] >= 0) {
      // console.log(nextIdx);
      C -= map[nowIdx][nextIdx];
      v[nextIdx] = 1;
      solution(nextIdx, Math.max(maxMoney, map[nowIdx][nextIdx]));
      v[nextIdx] = 0;
      C += map[nowIdx][nextIdx];
    }
  }
};

v[A] = 1;
solution(A, 0);

console.log(answer);
