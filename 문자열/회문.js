const filePath = process.platform === "linux" ? "/dev/stdin" : "회문.txt";
const input = require("fs")
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");
const N = input[0];

const checkPeli = (str) => {
  const stack = [];

  for (let char of str) {
    if (stack.length) {
      const lastChar = stack[stack.length - 1];

      if (lastChar === char) {
        stack.pop();
        continue;
      }
    }
    stack.push(char);
  }

  return [stack.length ? false : true, stack];
};

const check = (word, left, right) => {
  while (left < right) {
    if (word[left] === word[right]) {
      left++;
      right--;
    } else return false;
  }
  return true;
};

const solve = (word) => {
  let left = 0;
  let right = word.length - 1;

  while (left < right) {
    if (word[left] === word[right]) {
      left++;
      right--;
    } else {
      if (check(word, left + 1, right) || check(word, left, right - 1)) {
        return 1;
      } else return 2;
    }
  }
  return 0;
};

for (let i = 1; i <= N; i++) {
  console.log(solve(input[i]));
}
