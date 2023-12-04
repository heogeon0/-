const filePatjh = process.platform === "linux" ? "/dev/stdin" : "입국심사.txt";
const Input = require("fs")
  .readFileSync(filePatjh)
  .toString()
  .trim()
  .split("\n");

const [N, M] = Input[0].split(" ").map((i) => parseInt(i));
const table = [];

for (let i = 1; i <= N; i++) {
  table.push(parseInt(Input[i]));
}

let s = 1;
let e = Math.max(...table) * M;
let answer;

while (s <= e) {
  let mid = Math.floor((s + e) / 2);
  // flag === 1 : 전부 다 심사가능 else : 전부 심사 불가능
  let cnt = table.reduce((prev, t) => prev + Math.floor(mid / t), 0);

  if (cnt >= M) {
    answer = mid;
    e = mid - 1;
  } else {
    s = mid + 1;
  }
}

console.log(answer);
