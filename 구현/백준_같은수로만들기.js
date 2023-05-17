const filePath =
  process.platform === "linux" ? "/dev/stdin" : "같은수로만들기.txt";
const input = require("fs")
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");

const N = parseInt(input[0]);
const stack = [];

let answer = 0;
let maxv = 0;
for (let i = 1; i <= N; i++) {
  const now = parseInt(input[i]);
  maxv = Math.max(maxv, now);

  if (!stack.length) {
    stack.push(now);
  } else {
    if (stack[stack.length] < now) {
      answer += now - stack.pop();
      stack.push(now);
    } else if (stack[stack.length] > now) {
      stack.pop();
      stack.push(now);
    }
  }
}

while (stack.length) {
  answer += maxv - stack.pop();
}

console.log(answer);
