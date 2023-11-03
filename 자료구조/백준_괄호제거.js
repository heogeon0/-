const fs = require('fs')
const { exit } = require('process')
const input = fs.readFileSync('백준_괄호제거.txt').toString()

const correctList = []
const stack = []
const checkCorrect = (item, idx) => {
  if (stack.length > 0 && item === ')' && stack[stack.length - 1][0] === '(') {
    correctList.push([stack.pop(), [item, idx]])
  } else {
    stack.push([item, idx])
  }
}

const combi = (arr, n) => {
  if (n===1) return arr.map(el => [el])
  
  const result = []
  arr.forEach((fixed, idx, origin) => {
    const rest = origin.slice(idx + 1)
    const combis = combi(rest, n-1)

    const attached = combis.map(combi => [fixed, ...combi])
    result.push(...attached)
  }) 

  return result
}



// 1. 올바른 괄호 위치 찾기
for (let idx = 0; idx < input.length; idx++) {
  if (input[idx] === '(' || input[idx] === ')') {
    checkCorrect(input[idx], idx)
  }
}

// 2. 괄호쌍 위치로 조합 만들기
const combiList = []
for (let i = 1; i <= correctList.length; i++) {
  combiList.push(...combi(correctList, i))
}

const answer = []

for (let i = 0; i < combiList.length; i++) {
  let str = Array.from(input)
  for (let temp of combiList[i]) {
    for (let [_, idx] of temp) {
      str[idx] = '_'
    }
  }
  answer.push(str)
}

const ra = new Set()
for (const a of answer) {
  const aa = []
  for (const str of a) {
    if (str !== '_') aa.push(str)
  }
  ra.add(aa.join(''))
}

const k = [...ra].sort().reduce((acc, cur) => acc+cur+'\n', '')
console.log(k)

