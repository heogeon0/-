function solution(board, skill) {
  const N = board.length;
  const M = board[0].length;
  const newBoard = new Array(N + 1)
    .fill(0)
    .map((i) => new Array(M + 1).fill(0));

  skill.forEach(([type, r1, c1, r2, c2, p]) => {
    let power = type === 1 ? -p : p;

    newBoard[r1][c1] += power;
    newBoard[r1][c2 + 1] += -power;
    newBoard[r2 + 1][c1] += -power;
    newBoard[r2 + 1][c2 + 1] += power;
  });

  for (let i = 0; i < N + 1; i++) {
    for (let j = 1; j < M + 1; j++) {
      newBoard[i][j] += newBoard[i][j - 1];
    }
  }

  for (let j = 0; j < M + 1; j++) {
    for (let i = 1; i < N + 1; i++) {
      newBoard[i][j] += newBoard[i - 1][j];
    }
  }
  var answer = 0;

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      answer += board[i][j] + newBoard[i][j] > 0 ? 1 : 0;
    }
  }
  // console.log(newBoard)
  return answer;
}
