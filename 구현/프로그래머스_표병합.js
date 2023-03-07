function updateRocate(table, r, c, value) {
  table[r][c][0] = value;
  for (const [mr, mc] of table[r][c][1]) {
    if (table[mr][mc][0] !== value) updateRocate(table, mr, mc, value);
  }
}

function updateValue(table, v1, v2) {
  for (let i = 1; i <= 50; i++) {
    for (let j = 1; j <= 50; j++) {
      if (table[i][j][0] === v1) table[i][j][0] = v2;
    }
  }
}

function Merge(table, r, c, value) {
  for (const [mr, mc] of table[r][c][1]) {
    if (table[mr][mc][0] !== value) {
      table[mr][mc][0] = value;
      Merge(table, mr, mc, value);
    }
  }
}

function unMerge(table, r, c) {
  while (table[r][c][1].length) {
    const [mr, mc] = table[r][c][1].pop();
    table[mr][mc][0] = "EMPTY";
    unMerge(table, mr, mc);
  }
}

function solution(commands) {
  var table = new Array(51)
    .fill(0)
    .map((i) => new Array(51).fill(0).map((j) => ["EMPTY", []]));
  var answer = [];

  commands.forEach((command) => {
    const com = command.split(" ")[0];

    if (com === "MERGE") {
      const [com, r1, c1, r2, c2] = command.split(" ");
      if (r1 !== r2 || c1 !== c2) {
        const value =
          table[r1][c1][0] === "EMPTY" ? table[r2][c2][0] : table[r1][c1][0];
        table[r1][c1][1].push([r2, c2]);
        table[r2][c2][1].push([r1, c1]);
        updateRocate(table, r1, c1, value);
      }
    }

    if (com === "UNMERGE") {
      const [com, r, c] = command.split(" ");
      const temp = table[r][c][0];

      unMerge(table, r, c);
      updateRocate(table, r, c, temp);
    }

    if (com === "UPDATE") {
      const temp = [...command.split(" ")];

      if (temp.length === 4) {
        updateRocate(table, ...temp.slice(1));
      } else {
        updateValue(table, ...temp.slice(1));
      }
    }

    if (com === "PRINT") {
      const [com, r, c] = command.split(" ");
      answer.push(table[r][c][0]);
    }
  });

  console.log(table);
  // console.log(table[1][2][1])

  return answer;
}
