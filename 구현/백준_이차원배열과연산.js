const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let Input = [];

rl.on("line", function (line) {
  Input.push(line);
}).on("close", function () {
  console.log(solution(Input));
  process.exit();
});

function solution(Input) {
  const [R, C, K] = Input[0]
    .trim()
    .split(" ")
    .map((i) => parseInt(i));
  let arr = [];

  for (let i = 1; i < 4; i++) {
    arr.push(
      Input[i]
        .trim()
        .split(" ")
        .map((i) => parseInt(i))
    );
  }

  let time = 0;

  while (time <= 100) {
    if (
      arr.length >= R - 1 &&
      arr[0].length >= C - 1 &&
      arr[R - 1][C - 1] == K
    ) {
      break;
    }
    time += 1;

    if (arr.length >= arr[0].length) {
      arr = rCal(arr);
    } else {
      arr = cCal(arr);
    }
  }
  return time === 101 ? -1 : time;
}

function rCal(arr) {
  const newArr = [];
  let maxLen = 0;
  for (let i = 0; i < arr.length; i++) {
    const temp = new Map();
    const row = [];
    let target = arr[i];

    for (let j = 0; j < target.length; j++) {
      if (target[j] === 0) continue;

      temp.set(target[j], temp.get(target[j]) + 1 || 1);
    }

    Array.from(temp)
      .sort((a, b) => (a[1] === b[1] ? a[0] - b[0] : a[1] - b[1]))
      .forEach((i) => {
        row.push(...i);
        maxLen = Math.max(maxLen, row.length);
      });
    newArr.push(row);
  }

  newArr.forEach((i) => {
    while (i.length < maxLen) {
      i.push(0);
    }
  });

  return newArr;
}

function cCal(arr) {
  const tempArr = [];
  let maxLen = 0;
  for (let i = 0; i < arr[0].length; i++) {
    const temp = new Map();
    const col = [];
    let target = [];

    for (let k = 0; k < arr.length; k++) target.push(arr[k][i]);
    for (let j = 0; j < target.length; j++) {
      if (target[j] === 0) continue;
      temp.set(target[j], temp.get(target[j]) + 1 || 1);
    }
    Array.from(temp)
      .sort((a, b) => (a[1] === b[1] ? a[0] - b[0] : a[1] - b[1]))
      .forEach((i) => {
        col.push(...i);
        maxLen = Math.max(maxLen, col.length);
      });
    tempArr.push(col);
  }

  const newArr = new Array(maxLen)
    .fill(0)
    .map((i) => new Array(arr[0].length).fill(0));

  tempArr.forEach((arr, col) => {
    arr.forEach((i, row) => (newArr[row][col] = i));
  });

  return newArr;
}
