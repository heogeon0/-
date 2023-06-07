const filePath = process.platform === "linux" ? "/dev/stdin" : "백준_조합.txt";
const [N, M] = require("fs")
  .readFileSync(filePath)
  .toString()
  .trim()
  .split(" ")
  .map((i) => parseInt(i));

const combi = (arr, n) => {
  if (n === 1) return arr.map((el) => [el]);

  const result = [];

  arr.forEach((f, idx, origin) => {
    const rest = origin.slice(idx + 1);
    const combis = combi(rest, n - 1);
    const attached = combis.map((combi) => [f, ...rest]);

    result.push(...attached);
  });

  return result;
};

const fac = (n) => {
  let prod = 1;
  for (let i = 1; i <= n; i++) {
    prod *= i;
  }
  return prod;
};

console.log(Math.floor(fac(N) / (fac(N - M) * fac(M))));
