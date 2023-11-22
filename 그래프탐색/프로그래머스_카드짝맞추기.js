function getPerm(arr, n) {
  if (n === 1) return arr.map((el) => [el]);
  const result = [];

  arr.forEach((fixed, idx, _this) => {
    const rest = [..._this.slice(0, idx), ..._this.slice(idx + 1)];
    const perms = getPerm(rest, n - 1);
    const attached = perms.map((perm) => [fixed, ...perm]);
    result.push(...attached);
  });

  return result;
}

const isMovable = (y, x) => {
  if (-1 < y && y < 4 && -1 < x && x < 4) return true;
  else return false;
};

const ctrl_move = (y, x, dy, dx, board) => {
  let ny = y,
    nx = x;
  while (true) {
    const nny = ny + dy;
    const nnx = nx + dx;
    if (!isMovable(nny, nnx)) return [ny, nx];
    if (board[nny][nnx]) return [nny, nnx];
    ny = nny;
    nx = nnx;
  }
};

function solution(board, r, c) {
  let cards = [];
  let positions = {};

  // board에 존재하는 카드
  for (let i = 0; i < 4; i++) {
    for (let j = 0; j < 4; j++) {
      if (board[i][j] && !cards.includes(board[i][j])) cards.push(board[i][j]);
      if (board[i][j])
        positions[board[i][j]] = (positions[board[i][j]] || []).concat([
          [i, j],
        ]);
    }
  }
  // 모든 카드 제거 순서 찾기
  let perm = getPerm(cards, cards.length);

  // 카드 제거 순서대로 최소 횟수 찾기

  for (let i = 0; i < perm.length; i++) {
    let [sr, sc] = [r, c];
    let order = perm[i];

    for (let target of order) {
      // 1. 현재 위치에서 가까
    }
  }

  var answer = 0;
  return answer;
}
