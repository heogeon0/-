const fs = require('fs')
const input = fs.readFileSync('백준_요세푸스문제.txt').toString().split(' ')
const [a, b] = input.map(i => parseInt(i))

const arr = new Array(a).fill(0).map((_,idx) => idx + 1)
const answer = []
let cnt = 0

while (arr.length) {
  cnt += 1
  const frontNum = arr.shift()

  if (cnt === b) {
    answer.push(frontNum)
    cnt = 0
  } else {
    arr.push(frontNum)
  }
}

console.log(`<${answer.join(', ')}>`)