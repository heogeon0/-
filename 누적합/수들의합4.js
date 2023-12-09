const filePath = process.platform === "linux" ? "/dev/stdin" : "수들의합4.txt";
const Input = require("fs")
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");

const [N, K] = Input[0].split(" ").map((i) => parseInt(i));
const arr = Input[1].split(" ").map((i) => parseInt(i));
const sumArr = new Array(N).fill(0);

for (let i = 0; i < N; i++) {
  if (i - 1 > -1) sumArr[i] = sumArr[i - 1] + arr[i];
  else sumArr[i] = arr[i];
}

const map = {};
let answer = 0;
for (let i = 0; i < N; i++) {
  if (sumArr[i] === K) answer++;

  answer += map.hasOwnProperty(sumArr[i] - K) ? map[sumArr[i] - K] : 0;
  map[sumArr[i]] = map.hasOwnProperty(sumArr[i]) ? map[sumArr[i]] + 1 : 1;
}

console.log(answer);
