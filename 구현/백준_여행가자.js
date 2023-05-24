const filePath = process.platform === "linux" ? "/dev/stdin" : "여행가자.txt";
const input = require("fs")
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");

const N = parseInt(input[0]);
const M = parseInt(input[1]);

const course = input[input.length - 1].split(" ").map((i) => parseInt(i));
// console.log(course);
///
function bfs(s, e) {
  const v = new Array(N).fill(0);
  const Q = [s];
  v[s] = 1;
  // console.log(s, e);
  while (Q.length) {
    const now = Q.shift();

    if (now === e) return true;

    for (let i = 0; i < N; i++) {
      if (map[now][i] && v[i] === 0) {
        v[i] = 1;
        Q.push(i);
      }
    }
  }
  return false;
}

const map = [];
for (let i = 2; i < N + 2; i++) {
  map.push(
    input[i]
      .trim()
      .split(" ")
      .map((i) => parseInt(i))
  );
}

let flag = true;
for (let i = 0; i < M - 1; i++) {
  if (!flag) break;

  flag = bfs(course[i] - 1, course[i + 1] - 1);
}

console.log(flag ? "YES" : "NO");
