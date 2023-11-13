const fs = require("fs");
const input = fs.readFileSync("주지수.txt").toString().trim().split("\n");

const [N, M] = input[0].split(" ").map((i) => parseInt(i));
const arr = input
  .slice(1, N + 1)
  .map((i) => i.split(" ").map((i) => parseInt(i)));

const cnt = input[N + 1] * 1;
const question = [];
for (let i = N + 2; i <= N + 4; i++) {
  question.push(input[i].split(" ").map((i) => parseInt(i)));
}

const sumArr = new Array(N + 1).fill(0).map((i) => new Array(M + 1).fill(0));
for (let i = 1; i <= N; i++) {
  for (let j = 1; j <= M; j++) {
    sumArr[i][j] =
      arr[i - 1][j - 1] +
      sumArr[i - 1][j] +
      sumArr[i][j - 1] -
      sumArr[i - 1][j - 1];
  }
}

question.forEach(([sr, sc, er, ec]) => {
  // console.log(sumArr[er][ec]);
  console.log(
    sumArr[er][ec] -
      sumArr[sr - 1][ec] -
      sumArr[er][sc - 1] +
      sumArr[sr - 1][sc - 1]
  );
});

// console.log(question);
