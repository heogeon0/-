const fs = require('fs')
const input = fs.readFileSync('백준_나는야포켓몬마스터.txt').toString().trim().split('\n')
const [N, M] = input[0].split(' ').map(i => parseInt(i))

const checkNum = (str) => {
 if (str.charCodeAt(0) >= 65 ) {
  return false
 } else {
  return true
 }
}


const map = new Map()
for (let i = 1; i <= N; i++) {
  map.set(input[i] , i)
  map.set(i, input[i])
}

for (let i = N + 1; i <= N+M; i++) {
  if (checkNum(input[i])) console.log(map.get(parseInt(input[i])))
  else console.log(map.get(input[i]))
}

// console.log(map)