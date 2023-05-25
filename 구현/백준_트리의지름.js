const filePath = process.platform === "linux" ? "/dev/stdin" : "트리의지름.txt";
const input = require("fs")
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");

const N = parseInt(input[0]);
const tree = {};

for (let i = 1; i < N; i++) {
  const [a, b, m] = input[i]
    .trim()
    .split(" ")
    .map((i) => parseInt(i));
  tree[a] = (tree[a] || []).concat([[b, m]]);
  tree[b] = (tree[b] || []).concat([[a, m]]);
}

const bfs = (s) => {
  const v = new Array(N + 1).fill(0);
  v[s] = -1;
  const Q = [[s, 0]];

  while (Q.length) {
    const [now, cnt] = Q.shift();

    for (let i = 0; i < tree[now]?.length; i++) {
      const [next, weight] = tree[now][i];

      if (!v[next] && next != s) {
        v[next] = cnt + weight;
        Q.push([next, cnt + weight]);
      }
    }
  }
  return v.reduce((acc, now, idx) => (now > acc[0] ? [now, idx] : acc), [0, 0]);
};

const [value, nexts] = bfs(1);

answer = bfs(nexts)[0];

console.log(answer);
