const filePath =
  process.platform === "linux" ? "/dev/stdin" : "백준_컨베이어벨트위로봇.txt";
const Input = require("fs")
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");

const [N, M] = Input[0]
  .trim()
  .split(" ")
  .map((i) => parseInt(i));
const arr = Input[1]
  .trim()
  .split(" ")
  .map((i) => parseInt(i));

console.log(arr);
