const filePath = process.platForm === "linux" ? "/dev/stdin" : "N과M(1).txt";
const [N, M] = require("fs")
  .readFileSync(filePath)
  .toString()
  .trim()
  .split(" ")
  .map((i) => parseInt(i));

const makePerm = (n, arr) => {
  if (n === 1) {
    return arr.map((el) => [el]);
  }

  const result = [];

  arr.forEach((fixed, idx, origin) => {
    const rest = [...origin.slice(0, idx), ...origin.slice(idx + 1)];
    const perms = makePerm(n - 1, rest);
    const attached = perms.map((perm) => [fixed, ...perm]);
    result.push(...attached);
  });
  return result;
};

const arr = new Array(N).fill(0).map((i, idx) => idx + 1);

const perms = makePerm(M, arr);
console.log(perms);
// perms.forEach((i) => {
//   console.log(i);
// });
