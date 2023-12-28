const filePath = process.platform === "linux" ? "/dev/stdin" : "후위표기식.txt";

const input = require("fs").readFileSync(filePath).toString().trim().split("");

const stack = [];
let answer = "";

input.forEach((str) => {
  if (str === "(") {
    stack.push(str);
  } else if (str === ")") {
    while (stack.length && stack[stack.length - 1] !== "(") {
      answer += stack.pop();
    }

    stack.pop();
  } else if (str === "*" || str === "/") {
    while (
      (stack.length && stack[stack.length - 1] === "*") ||
      stack[stack.length - 1] === "/"
    ) {
      answer += stack.pop();
    }

    stack.push(str);
  } else if (str === "+" || str === "-") {
    while (stack.length && stack[stack.length - 1] !== "(") {
      answer += stack.pop();
    }
    stack.push(str);
  } else {
    answer += str;
  }
});

while (stack.length) {
  answer += stack.pop();
}

console.log(answer);
