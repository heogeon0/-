const filePath = process.platform === "linux" ? "/dev/stdin" : "최단거리.txt";
const [N, M] = require("fs")
  .readFileSync(filePath)
  .toString()
  .split(" ")
  .map((i) => parseInt(i));

const v = new Array(100001).fill(0);

const solve = (N, M) => {
  const q = [];
  q.push([N, 0]);
  v[N] = 1;

  while (q.length) {
    const [now, time] = q.shift();
    if (now === M) return time;

    for (let next of [now * 2, now - 1, now + 1]) {
      if (next >= 0 && next <= 100000 && v[next] === 0) {
        v[next] = 1;
        if (next === now * 2) {
          q.unshift([next, time]);
        } else {
          q.push([next, time + 1]);
        }
      }
    }
  }
};

console.log(solve(N, M));
