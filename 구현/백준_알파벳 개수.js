// console.log("a".charCodeAt() - 97);
const filePath = process.platform === "linux" ? "/dev/stdin" : "알파벳개수.txt";
const input = require("fs").readFileSync(filePath).toString().trim();

function cntAlpha(string) {
  const answer = new Array(26).fill(0);

  for (const str of string) {
    answer[str.charCodeAt() - 97] += 1;
  }

  return answer;
}

console.log(...cntAlpha(input));
