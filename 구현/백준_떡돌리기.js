const { exit } = require("process");

function dik(start, map, routes) {
  const Q = [start];
  map[start] = 0;

  while (Q.length) {
    const now = Q.shift();

    for (const [next, weight] of routes[now]) {
      if (map[next] > weight + map[now]) {
        map[next] = weight + map[now];
        Q.push(next);
      }
    }
  }
}

const filePath = process.platform === "linux" ? "/dev/stdin" : "떡돌리기.txt";
const input = require("fs")
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");

// N : 집 갯수, M : 도로 갯수, X : 최대 이동량, Y : 성현이의 집
const [N, M, X, Y] = input[0]
  .trim()
  .split(" ")
  .map((i) => parseInt(i));

let map = new Array(N).fill(Infinity);
const routes = {};

for (let i = 1; i < M + 1; i++) {
  const [a, b, w] = input[i]
    .trim()
    .split(" ")
    .map((i) => parseInt(i));

  routes[a] = (routes[a] || []).concat([[b, w]]);
  routes[b] = (routes[b] || []).concat([[a, w]]);
}

dik(Y, map, routes);
map = map.sort((a, b) => a - b).map((i) => i * 2);
map.shift();
if (map[map.length - 1] > X) {
  console.log(-1);
  exit();
}

let day = 1;
let dayMax = X;
while (map.length) {
  const weight = map.shift();

  if (dayMax >= weight) dayMax -= weight;
  else {
    day += 1;
    dayMax = X - weight;
  }
}

console.log(day);
